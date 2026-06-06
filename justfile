set shell := ["zsh", "-eu", "-o", "pipefail", "-c"]

skin_name := "DeathDisco Grave Raver v1"
src_dir := "src"
assets_dir := "assets"
build_dir := "build"
default: install

generate:
    python3 scripts/gen-browser-positions.py

check: verify-generated lint audit

verify-generated:
    python3 scripts/gen-browser-positions.py --check

audit: audit-classes audit-structure

audit-classes:
    python3 scripts/audit-class-casing.py

audit-structure:
    python3 scripts/audit-structure.py

repair-pad-state:
    python3 scripts/repair-vdj-pad-panels.py

repair-pad-state-apply:
    python3 scripts/repair-vdj-pad-panels.py --apply

lint: lint-prod

lint-prod: generate
    xmllint --noout --xinclude --loaddtd --noent "{{src_dir}}/skin.xml"

build: lint-prod
    mkdir -p "{{build_dir}}"
    if [[ -d "{{assets_dir}}" ]]; then rsync -a --delete "{{assets_dir}}/" "{{build_dir}}/"; fi
    xmllint --format --xinclude --loaddtd --noent "{{src_dir}}/skin.xml" --output "{{build_dir}}/skin.xml"
    python3 scripts/minify-skin.py "{{build_dir}}/skin.xml"

install: build
    install_root="$HOME/Library/Application Support/VirtualDJ/Skins"; \
    install_path="$install_root/{{skin_name}}"; \
    mkdir -p "$install_path"; \
    if [[ -d "{{assets_dir}}" ]]; then rsync -a --omit-dir-times --delete --exclude skin.xml "{{assets_dir}}/" "$install_path/"; fi; \
    cmp -s "{{build_dir}}/skin.xml" "$install_path/skin.xml" || cp -f "{{build_dir}}/skin.xml" "$install_path/skin.xml"

watch:
    watchexec \
      --clear \
      --watch "{{src_dir}}" \
      --watch "{{assets_dir}}" \
      --exts xml,png,jpg,jpeg,bmp,svg \
      --ignore "{{build_dir}}" \
      --ignore .git \
      -- just install

clean:
    rm -rf "{{build_dir}}"
