# GraveRaver Contributor Guide

Quick orientation for agents working in this VirtualDJ skin repo.

## Start Here

- `src/skin.xml` is the sole skin entrypoint.
- `CLAUDE.md` is the canonical contributor guide; `AGENTS.md` is a symlink to
  this file so Claude and other agents read the same instructions.
- There is intentionally no `src/index.xml`; do not reintroduce a hidden root include layer.
- Remaining cleanup work lives in `TODO.md`.
- Use `rg` for searches and read the local XML before changing shared components.

## Commands

- Bare `just` (or `just help`): list recipes and their effects without writing.
- `just check`: the main read-only verification command — verifies generated browser positions, expands/lints the XML, and runs the class-casing and structural audits.
- `just lint`: read-only generated-file verification and XML expansion/linting.
- `just audit`: class and structural audits only.
- `just generate`: writes `src/layouts/browser/browser-positions.generated.xml`.
- `just build`: regenerates browser positions and writes the built/minified skin under `build/`.
- `just install`: builds and installs the skin into
  `~/Library/Application Support/VirtualDJ/Skins/DeathDisco Grave Raver v1/`.
- `just watch`: continuously rebuilds and installs after changes under `src/` or `assets/`.
- `just repair-pad-state`: dry-run the VirtualDJ pad panel state repair; `just repair-pad-state-apply` backs up and writes VirtualDJ's `settings.xml`.
- `just clean`: deletes local `build/` output.

## Source Map

- `src/skin.xml`: sole entrypoint, containing the root skin metadata and
  top-level XIncludes.
- `src/colors.xml`, `src/globals.xml`: shared color and global definitions.
- `src/components/index.xml`: component include hub.
- `src/components/buttons/index.xml`: button-family include hub.
- `src/components/racks/`: rack components — `effects-racks.xml`, `mixer-racks.xml`, `video-racks.xml`, plus `containers/` for rack shells and positioning.
- `src/components/containers/`: larger reusable regions — `topbar.xml` and
  `bottombar.xml` are shared containers shown on every layout; `pad-page.xml`
  and `waveform/` contain other reusable container surfaces.
- `src/components/center-panel/`: the Pro mixer-mode center column. `index.xml` is the hub; `center-panel.xml` holds the `MIXER`/`MIXER_4DECKS` shells and shared channel-strip helpers; each tab pane lives in its own file (`eq-mixer.xml`, `sampler.xml`, `wave-mixer.xml`, `master-mixer.xml`).
- `src/layouts/base.xml`: top-level layout assembly.
- `src/layouts/pro/`, `src/layouts/performance/`, `src/layouts/stack/`: mode-specific layout shells.
- `src/layouts/browser/`: browser panel layouts; `browser-positions.generated.xml` is generated — edit `scripts/gen-browser-positions.py` instead of patching it by hand.
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
