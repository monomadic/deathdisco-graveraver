# AGENTS

Quick orientation for agents working in this VirtualDJ skin repo.

## Start Here

- The skin root is `src/skin.xml`.
- There is intentionally no `src/index.xml`; do not reintroduce a hidden root include layer.
- Remaining cleanup work lives in `TODO.md`.
- Use `rg` for searches and read the local XML before changing shared components.

## Commands

- `just check` is the main verification command. It checks generated browser positions, expands/lints XML, audits class casing, and runs structural reachability checks.
- `just audit` runs the class and structural audits only.
- `just build` writes the built/minified skin under `build/`.
- `just install` builds and installs the skin into the local VirtualDJ skin directory.

## Source Map

- `src/skin.xml`: root skin file and top-level XIncludes.
- `src/components/index.xml`: component include hub.
- `src/components/buttons/index.xml`: button-family include hub.
- `src/components/containers/`: larger reusable regions such as waveform, mixer, racks, topbar, bottombar, and pad containers.
- `src/components/center-panel/`: the Pro mixer-mode center column. `index.xml` is the hub; `center-panel.xml` holds the `MIXER`/`MIXER_4DECKS` shells and shared channel-strip helpers; each tab pane lives in its own file (`eq-mixer.xml`, `sampler.xml`, `wave-mixer.xml`, `master-mixer.xml`).
- `src/layouts/base.xml`: top-level layout assembly.
- `src/layouts/pro/`, `src/layouts/performance/`, `src/layouts/stack/`: mode-specific layout shells.
- `src/layouts/browser/performance.generated.xml`: generated file; edit `scripts/gen-browser-positions.py` instead of patching this by hand.
- `assets/`: installable skin assets copied during build/install.

## XML Conventions

- Define reusable classes with uppercase names: `<define class="TRACK_INFO_PRO">`.
- Reference classes with lowercase names: `<panel class="track_info_pro">`.
- Keep layout-only helpers near the layout that owns them.
- Add reusable components to the relevant index, usually `src/components/index.xml` or a nested index such as `src/components/buttons/index.xml`.
- If an XInclude target becomes empty, remove the include and the file.

## Audits

- `scripts/audit-class-casing.py` enforces class-definition/reference casing and catches missing class definitions.
- `scripts/audit-structure.py` catches unused definitions, unreachable class islands, unlinked XML files, missing or empty XInclude targets, unexpected duplicate definitions, and new always-hidden blocks.
- Known duplicate class definitions are deliberate color-scheme variants. Add new duplicates only with a clear reason and update the structural audit allowlist.

## Editing Notes

- Do not edit generated XML as the durable source of truth.
- Keep source changes surgical when fixing a visual/layout bug.
- The worktree may contain unrelated user changes. Do not revert or rewrite files outside the current task.
- After structural or layout changes, run `just check`. For visual behavior changes, follow with `just install` and inspect the skin in VirtualDJ.
