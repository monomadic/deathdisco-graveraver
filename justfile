set shell := ["zsh", "-eu", "-o", "pipefail", "-c"]

skin_name := "DeathDisco GraveRaver v1"
src_dir := "src"
assets_dir := "assets"
build_dir := "build"

default: install

build:
    mkdir -p "{{build_dir}}"
    xmllint --noout --xinclude "{{src_dir}}/skin.xml"
    xmllint --xinclude "{{src_dir}}/skin.xml" > "{{build_dir}}/skin.xml"

install: build
    install_root="$HOME/Library/Application Support/VirtualDJ/Skins"; \
    install_path="$install_root/{{skin_name}}"; \
    mkdir -p "$install_path"; \
    if [[ -d "{{assets_dir}}" ]]; then rsync -a --delete "{{assets_dir}}/" "$install_path/"; fi; \
    cp -f "{{build_dir}}/skin.xml" "$install_path/skin.xml"

watch:
    # watchexec v2+ syntax using --filter (more portable than --exts)
    watchexec \
      --clear \
      --restart \
      --watch "{{src_dir}}" \
      --watch "{{assets_dir}}" \
      --ignore "{{build_dir}}" \
      --ignore .git \
      --filter 'glob:**/*.xml' \
      --filter 'glob:**/*.{png,jpg,jpeg,bmp,svg}' \
      -- just install

clean:
    rm -rf "{{build_dir}}"
