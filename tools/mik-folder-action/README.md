# Mixed In Key to Lexicon Folder Action

This installs a macOS Folder Action that:

1. Watches a drop folder for `flac`, `aac`, `m4a`, `wav`, and `mp3` files.
2. Opens supported files in Mixed In Key.
3. Waits for Mixed In Key to write an `InitialKey`/key tag.
4. Optionally waits for cue-like tags.
5. Copies the processed file into `$HOME/Music/Downloads` for Lexicon.
6. Shows a macOS alert when the copied file is ready.

## Install

```sh
tools/mik-folder-action/install-folder-action.sh
```

The default drop folder is:

```text
$HOME/Music/Mixed In Key Drop
```

Pass a folder path to attach the action somewhere else:

```sh
tools/mik-folder-action/install-folder-action.sh "$HOME/Music/To Process"
```

## Configure

Edit:

```text
$HOME/.config/mik-folder-action/env
```

Useful settings:

```sh
MIK_LEXICON_INCOMING="$HOME/Music/Downloads"
MIK_APP_NAME="Mixed In Key 11"
MIK_REQUIRE_CUE_TAGS=0
MIK_AUTOCUE_SCRIPT=""
```

Mixed In Key 11 may not write cue points into file tags in every workflow. Keep
`MIK_REQUIRE_CUE_TAGS=0` to copy once the key tag is present, after a short
grace period for cue tags. Set it to `1` if you want the action to wait for
cue-like tags and fail on timeout when they do not appear.

To add your own auto-cue pass later, point `MIK_AUTOCUE_SCRIPT` at an executable
script. It will receive the source audio file path as its first argument and run
after Mixed In Key tags are detected, before the file is copied to Lexicon.

Logs are written to:

```text
$HOME/Library/Logs/MixedInKeyFolderAction/mik-to-lexicon.log
```
