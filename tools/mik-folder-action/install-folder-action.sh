#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
WATCH_FOLDER="${1:-$HOME/Music/Mixed In Key Drop}"

HELPER_DIR="$HOME/Library/Application Scripts/com.nom.mik-folder-action"
HELPER_TARGET="$HELPER_DIR/mik-to-lexicon.sh"
CONFIG_DIR="$HOME/.config/mik-folder-action"
CONFIG_TARGET="$CONFIG_DIR/env"
FOLDER_ACTION_DIR="$HOME/Library/Scripts/Folder Action Scripts"
ACTION_NAME="Mixed In Key to Lexicon.scpt"
ACTION_TARGET="$FOLDER_ACTION_DIR/$ACTION_NAME"

mkdir -p "$WATCH_FOLDER" "$HELPER_DIR" "$CONFIG_DIR" "$FOLDER_ACTION_DIR"
WATCH_FOLDER="$(cd "$WATCH_FOLDER" && pwd -P)"

/usr/bin/install -m 755 "$SCRIPT_DIR/mik-to-lexicon.sh" "$HELPER_TARGET"
if [[ ! -f "$CONFIG_TARGET" ]]; then
  /usr/bin/install -m 644 "$SCRIPT_DIR/default.env" "$CONFIG_TARGET"
fi

/usr/bin/osacompile -o "$ACTION_TARGET" "$SCRIPT_DIR/Mixed In Key to Lexicon.applescript"
/usr/bin/osascript "$SCRIPT_DIR/attach-folder-action.applescript" "$WATCH_FOLDER" "$ACTION_TARGET"

printf 'Installed Mixed In Key folder action.\n'
printf 'Drop folder: %s\n' "$WATCH_FOLDER"
printf 'Folder action: %s\n' "$ACTION_TARGET"
printf 'Helper: %s\n' "$HELPER_TARGET"
printf 'Config: %s\n' "$CONFIG_TARGET"
