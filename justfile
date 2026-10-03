set shell := ["zsh", "-eu", "-o", "pipefail", "-c"]

skin_name := "DeathDisco Grave Raver v1"
src_dir := "src"
assets_dir := "assets"
build_dir := "build"
# VDJScript linter from the virtualdj-api-reference checkout (override with VDJ_API_REFERENCE).
vdj_ref := env_var_or_default("VDJ_API_REFERENCE", justfile_directory() / "../virtualdj-api-reference")
vdj_ref_python := if path_exists(vdj_ref / ".venv/bin/python3") == "true" { vdj_ref / ".venv/bin/python3" } else { "python3" }

# [read-only] List available recipes and their effects.
default: help

# [read-only] List available recipes and their effects.
help:
    @just --list

# [writes source] Regenerate browser positions and waveform size XML.
generate:
    python3 scripts/gen-browser-positions.py

# [read-only] Verify generated XML, lint the skin and its VDJScript, and run all audits.
check: lint lint-script audit test

# [read-only] Run regression tests for build and audit tools.
test:
    python3 -B -m unittest discover -s tests

# [read-only] Fail when any generated geometry XML is stale.
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

# [read-only] Verify generated XML, then expand includes and macros into a scratch copy and lint the result.
lint: verify-generated
    set -e; tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT; \
    find "{{src_dir}}" -name '*.xml' -print0 | xargs -0 xmllint --noout; \
    xmllint --xinclude --loaddtd --noent "{{src_dir}}/skin.xml" --output "$tmp/skin.xml"; \
    python3 scripts/expand-skin-macros.py "$tmp/skin.xml"; \
    xmllint --noout "$tmp/skin.xml"

# [read-only] Statically lint every VDJScript in the expanded skin (errors fail; warnings are listed, notes and numeric-opacity visibilities are hidden).
lint-script:
    set -e; linter="{{vdj_ref}}/tools/lint_script.py"; \
    if [[ ! -f "$linter" ]]; then echo "SKIPPED lint-script: $linter not found (set VDJ_API_REFERENCE)"; exit 0; fi; \
    tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT; \
    xmllint --xinclude --loaddtd --noent "{{src_dir}}/skin.xml" --output "$tmp/skin.xml"; \
    python3 scripts/expand-skin-macros.py "$tmp/skin.xml" >/dev/null; \
    "{{vdj_ref_python}}" "$linter" --xml "$tmp/skin.xml" | sed -E 's#^(WARNING|ERROR|NOTE) +/.*/skin.xml:#\1 skin.xml:#' \
      | grep -v '^NOTE ' | grep -v "visibility: '[0-9.]*' is not in the verb table" || true; \
    "{{vdj_ref_python}}" "$linter" --xml "$tmp/skin.xml" >/dev/null

# [writes source + build] Regenerate source and build the minified skin.
build: generate lint audit test
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
