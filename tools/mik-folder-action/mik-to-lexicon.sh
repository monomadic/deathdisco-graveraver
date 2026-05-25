#!/usr/bin/env bash
set -uo pipefail

PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

CONFIG_FILE="${MIK_FOLDER_ACTION_CONFIG:-$HOME/.config/mik-folder-action/env}"
if [[ -f "$CONFIG_FILE" ]]; then
  # shellcheck disable=SC1090
  . "$CONFIG_FILE"
fi

DEST_DIR="${MIK_LEXICON_INCOMING:-$HOME/Music/Downloads}"
MIXED_IN_KEY_APP="${MIK_APP_NAME:-Mixed In Key 11}"
POLL_SECONDS="${MIK_POLL_SECONDS:-10}"
STABLE_POLL_SECONDS="${MIK_STABLE_POLL_SECONDS:-2}"
TIMEOUT_SECONDS="${MIK_TIMEOUT_SECONDS:-1800}"
CUE_GRACE_SECONDS="${MIK_CUE_GRACE_SECONDS:-45}"
REQUIRE_CUE_TAGS="${MIK_REQUIRE_CUE_TAGS:-0}"
AUTOCUE_SCRIPT="${MIK_AUTOCUE_SCRIPT:-}"

LOG_DIR="$HOME/Library/Logs/MixedInKeyFolderAction"
LOG_FILE="$LOG_DIR/mik-to-lexicon.log"

mkdir -p "$LOG_DIR"

log() {
  printf '%s %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >>"$LOG_FILE"
}

alert() {
  local title="$1"
  local message="$2"
  /usr/bin/osascript - "$title" "$message" <<'OSA' >/dev/null 2>&1 || true
on run argv
  display alert (item 1 of argv) message (item 2 of argv) buttons {"OK"} default button "OK"
end run
OSA
}

notify() {
  local title="$1"
  local message="$2"
  /usr/bin/osascript - "$title" "$message" <<'OSA' >/dev/null 2>&1 || true
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
OSA
}

is_audio_file() {
  local file="$1"
  local ext
  ext="$(printf '%s' "${file##*.}" | tr '[:upper:]' '[:lower:]')"
  case "$ext" in
    flac | aac | m4a | wav | mp3) return 0 ;;
    *) return 1 ;;
  esac
}

collect_audio_files() {
  local item
  for item in "$@"; do
    if [[ -d "$item" ]]; then
      /usr/bin/find "$item" -type f \( \
        -iname '*.flac' -o \
        -iname '*.aac' -o \
        -iname '*.m4a' -o \
        -iname '*.wav' -o \
        -iname '*.mp3' \
      \) -print0
    elif [[ -f "$item" ]] && is_audio_file "$item"; then
      printf '%s\0' "$item"
    fi
  done
}

wait_until_file_stable() {
  local file="$1"
  local previous=""
  local current=""
  local stable_deadline=$((SECONDS + 120))

  while (( SECONDS < stable_deadline )); do
    current="$(/usr/bin/stat -f '%z:%m' "$file" 2>/dev/null)" || return 1
    if [[ "$current" == "$previous" ]]; then
      return 0
    fi
    previous="$current"
    sleep "$STABLE_POLL_SECONDS"
  done

  return 1
}

metadata_snapshot() {
  local file="$1"
  "$EXIFTOOL_BIN" -m -api largefilesupport=1 -ee -G1 -s "$file" 2>/dev/null || true
}

has_key_tag() {
  awk -F':' '
    {
      left = $1
      value = $0
      sub(/^[^:]*:[ \t]*/, "", value)
      gsub(/^\[[^]]+\][ \t]*/, "", left)
      gsub(/[ \t]/, "", left)
      tag = tolower(left)
      if ((tag == "initialkey" || tag == "key" || tag == "tkey") && value !~ /^[ \t]*$/) {
        found = 1
      }
    }
    END { exit(found ? 0 : 1) }
  '
}

has_cue_tag() {
  awk -F':' '
    {
      left = $1
      line = tolower($0)
      gsub(/^\[[^]]+\][ \t]*/, "", left)
      gsub(/[ \t]/, "", left)
      tag = tolower(left)
      if (tag ~ /(cue|hotcue|marker|beatgrid|serato|traktor|rekordbox)/) {
        found = 1
      }
      if (line ~ /(serato markers|mixed in key cue|hot cue|cue point|beatgrid|rekordbox)/) {
        found = 1
      }
    }
    END { exit(found ? 0 : 1) }
  '
}

extract_key_value() {
  local file="$1"
  "$EXIFTOOL_BIN" -s3 -InitialKey -Key "$file" 2>/dev/null | awk 'NF { print; exit }'
}

open_in_mixed_in_key() {
  local file="$1"
  /usr/bin/open -a "$MIXED_IN_KEY_APP" "$file"
}

wait_for_mik_tags() {
  local file="$1"
  local deadline=$((SECONDS + TIMEOUT_SECONDS))
  local key_seen_at=0
  local meta=""
  local key_found=0
  local cue_found=0

  while (( SECONDS < deadline )); do
    meta="$(metadata_snapshot "$file")"

    if printf '%s\n' "$meta" | has_key_tag; then
      key_found=1
      if (( key_seen_at == 0 )); then
        key_seen_at=$SECONDS
        log "Key tag detected for $file"
      fi
    fi

    if printf '%s\n' "$meta" | has_cue_tag; then
      cue_found=1
      log "Cue-like tag detected for $file"
    fi

    if (( key_found == 1 )); then
      if (( cue_found == 1 )); then
        wait_until_file_stable "$file" && {
          printf 'key and cue tags'
          return 0
        }
      elif [[ "$REQUIRE_CUE_TAGS" != "1" ]] && (( SECONDS - key_seen_at >= CUE_GRACE_SECONDS )); then
        wait_until_file_stable "$file" && {
          printf 'key tag; cue tags not detected'
          return 0
        }
      fi
    fi

    sleep "$POLL_SECONDS"
  done

  if (( key_found == 1 )); then
    printf 'timed out after key tag; cue tags not detected'
    return 2
  fi

  printf 'timed out waiting for key tag'
  return 1
}

copy_unique() {
  local source="$1"
  local target_dir="$2"
  local name base ext candidate n

  name="$(basename "$source")"
  base="$name"
  ext=""
  if [[ "$name" == *.* ]]; then
    base="${name%.*}"
    ext=".${name##*.}"
  fi

  candidate="$target_dir/$name"
  n=1
  while [[ -e "$candidate" ]]; do
    candidate="$target_dir/$base $n$ext"
    n=$((n + 1))
  done

  /bin/cp -p "$source" "$candidate"
  printf '%s' "$candidate"
}

run_autocue_if_configured() {
  local file="$1"

  if [[ -z "$AUTOCUE_SCRIPT" ]]; then
    return 0
  fi

  if [[ ! -x "$AUTOCUE_SCRIPT" ]]; then
    log "Auto-cue script is configured but not executable: $AUTOCUE_SCRIPT"
    return 1
  fi

  log "Running auto-cue script for $file: $AUTOCUE_SCRIPT"
  "$AUTOCUE_SCRIPT" "$file"
  wait_until_file_stable "$file"
}

process_file() {
  local file="$1"
  local status=""
  local copied_to=""
  local key_value=""

  log "Processing $file"

  if [[ ! -d "$DEST_DIR" ]]; then
    mkdir -p "$DEST_DIR" || {
      alert "Mixed In Key Folder Action" "Could not create Lexicon incoming folder: $DEST_DIR"
      return 1
    }
  fi

  wait_until_file_stable "$file" || {
    alert "Mixed In Key Folder Action" "File did not become stable before analysis:\n$file"
    return 1
  }

  if ! open_in_mixed_in_key "$file"; then
    alert "Mixed In Key Folder Action" "Could not open this file in $MIXED_IN_KEY_APP:\n$file"
    return 1
  fi

  log "Opened in $MIXED_IN_KEY_APP: $file"

  status="$(wait_for_mik_tags "$file")"
  case "$?" in
    0) ;;
    2)
      if [[ "$REQUIRE_CUE_TAGS" == "1" ]]; then
        alert "Mixed In Key Folder Action" "Timed out waiting for cue tags after the key tag was written:\n$file"
        return 1
      fi
      ;;
    *)
      alert "Mixed In Key Folder Action" "Timed out waiting for Mixed In Key tags:\n$file"
      return 1
      ;;
  esac

  if ! run_autocue_if_configured "$file"; then
    alert "Mixed In Key Folder Action" "Auto-cue script failed for:\n$file"
    return 1
  fi

  copied_to="$(copy_unique "$file" "$DEST_DIR")" || {
    alert "Mixed In Key Folder Action" "Could not copy file to Lexicon incoming:\n$file"
    return 1
  }

  key_value="$(extract_key_value "$copied_to")"
  log "Copied to $copied_to ($status)"

  if [[ -n "$key_value" ]]; then
    notify "Track ready for Lexicon" "$(basename "$copied_to") copied with key $key_value"
    alert "Track ready for Lexicon" "$(basename "$copied_to") is in:\n$DEST_DIR\n\nDetected: $status\nKey: $key_value"
  else
    notify "Track ready for Lexicon" "$(basename "$copied_to") copied to Lexicon incoming"
    alert "Track ready for Lexicon" "$(basename "$copied_to") is in:\n$DEST_DIR\n\nDetected: $status"
  fi
}

main() {
  local file
  local processed=0
  local failed=0

  EXIFTOOL_BIN="${EXIFTOOL_BIN:-$(command -v exiftool || true)}"
  if [[ -z "$EXIFTOOL_BIN" ]]; then
    alert "Mixed In Key Folder Action" "exiftool was not found. Install it with Homebrew or set EXIFTOOL_BIN in $CONFIG_FILE."
    exit 1
  fi

  if (( $# == 0 )); then
    log "No files passed to folder action"
    exit 0
  fi

  while IFS= read -r -d '' file; do
    processed=$((processed + 1))
    if ! process_file "$file"; then
      failed=$((failed + 1))
      log "Failed: $file"
    fi
  done < <(collect_audio_files "$@")

  if (( processed == 0 )); then
    log "No supported audio files found in folder action input"
  elif (( failed > 0 )); then
    alert "Mixed In Key Folder Action" "$failed of $processed file(s) failed. See:\n$LOG_FILE"
  fi
}

main "$@"
