set shell := ["zsh", "-eu", "-o", "pipefail", "-c"]

skin_name := "DeathDisco Grave Raver v1"
src_dir := "src"
assets_dir := "assets"
build_dir := "build"

# [read-only] List available recipes and their effects.
default: help

# [read-only] List available recipes and their effects.
help:
    @just --list

# [writes source] Regenerate checked-in browser position XML.
generate:
    python3 scripts/gen-browser-positions.py

# [read-only] Verify generated XML, lint the skin, and run all audits.
check: lint audit

# [read-only] Fail when generated browser position XML is stale.
verify-generated:
    python3 scripts/gen-browser-positions.py --check

# [read-only] Run class, structural, and state audits.
audit: audit-classes audit-structure audit-state

# [read-only, internal] Audit class definition/reference casing.
audit-classes:
    python3 scripts/audit-class-casing.py

# [read-only, internal] Audit includes, reachability, and structural conventions.
audit-structure:
    python3 scripts/audit-structure.py

# [read-only, internal] Audit registered skin variables and closed enums.
audit-state:
    python3 scripts/audit-state-vars.py

# [read-only] Preview VirtualDJ pad panel state repairs.
repair-pad-state:
    python3 scripts/repair-vdj-pad-panels.py

# [writes VirtualDJ settings] Back up and repair persisted pad panel state.
repair-pad-state-apply:
    python3 scripts/repair-vdj-pad-panels.py --apply

# [read-only] Verify generated XML and expand/lint the skin entrypoint.
lint: verify-generated
    xmllint --noout --xinclude --loaddtd --noent "{{src_dir}}/skin.xml"

# [writes source + build] Regenerate source and build the minified skin.
build: generate lint
    mkdir -p "{{build_dir}}"
    if [[ -d "{{assets_dir}}" ]]; then rsync -a --delete "{{assets_dir}}/" "{{build_dir}}/"; fi
    xmllint --format --xinclude --loaddtd --noent "{{src_dir}}/skin.xml" --output "{{build_dir}}/skin.xml"
    python3 scripts/expand-skin-macros.py "{{build_dir}}/skin.xml"
    python3 scripts/minify-skin.py "{{build_dir}}/skin.xml"

# [writes source + build + VirtualDJ skin] Build and install the live skin.
install: build
    install_root="$HOME/Library/Application Support/VirtualDJ/Skins"; \
    install_path="$install_root/{{skin_name}}"; \
    mkdir -p "$install_path"; \
    if [[ -d "{{assets_dir}}" ]]; then rsync -a --omit-dir-times --delete --exclude skin.xml "{{assets_dir}}/" "$install_path/"; fi; \
    cmp -s "{{build_dir}}/skin.xml" "$install_path/skin.xml" || cp -f "{{build_dir}}/skin.xml" "$install_path/skin.xml"

# [continuously installs] Rebuild and install whenever source or assets change.
watch:
    watchexec \
      --clear \
      --watch "{{src_dir}}" \
      --watch "{{assets_dir}}" \
      --exts xml,png,jpg,jpeg,bmp,svg \
      --ignore "{{build_dir}}" \
      --ignore .git \
      -- just install

# [deletes build] Remove local build output.
clean:
    rm -rf "{{build_dir}}"
