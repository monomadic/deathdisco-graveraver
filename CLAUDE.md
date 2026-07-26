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
- `src/components/containers/`: larger reusable container regions — `pad-page.xml`
  and `waveform/` container surfaces.
- `src/components/topbar/`, `src/components/bottombar/`: the per-bar component
  classes (one responsibility region per file, plus an `index.xml` hub). They are
  loaded onto the bars by the bar layouts via VirtualDJ classes.
- `src/components/center-panel/`: the Pro mixer-mode center column. `index.xml` is the hub; `center-panel.xml` holds the `MIXER`/`MIXER_4DECKS` shells and shared channel-strip helpers; each tab pane lives in its own file (`eq-mixer.xml`, `sampler.xml`, `wave-mixer.xml`, `master-mixer.xml`).
- `src/layouts/base.xml`: top-level layout assembly.
- `src/layouts/topbar.xml`, `src/layouts/bottombar.xml`: the shared top/bottom
  bars. Each is a layout that owns *which* component appears *where/when* on the
  bar and loads the `src/components/topbar` / `src/components/bottombar` classes;
  they are layered onto every screen mode.
- `src/layouts/pro/`, `src/layouts/performance/`, `src/layouts/stack/`: mode-specific layout shells.
- `src/layouts/browser/`: browser panel layouts; `browser-positions.generated.xml` is generated — edit `scripts/gen-browser-positions.py` instead of patching it by hand.
- `assets/`: installable skin assets copied during build/install.

## XML Conventions

- Define reusable classes with uppercase names: `<define class="TRACK_INFO_PRO">`.
- Reference classes with lowercase names: `<panel class="track_info_pro">`.
- Keep layout-only helpers near the layout that owns them.
- Add reusable components to the relevant index, usually `src/components/index.xml` or a nested index such as `src/components/buttons/index.xml`.
- If an XInclude target becomes empty, remove the include and the file.

### Layouts, components, and the two composition mechanisms

There are two distinct ways files come together, and they are not
interchangeable:

- **XInclude (`xi:include`) assembles the class *library*.** The includes under
  `src/components/index.xml` (and its nested hubs) pull every `<define>` into one
  flat pool of classes at build time. Use XInclude to make a definition
  *available*, not to place UI on screen. `xpointer(/defs/*)` pulls the defines;
  `xpointer(/module/*)` pulls a layout module's on-screen elements.
- **VirtualDJ classes (`class="…"`) compose the UI at runtime.** A layout draws a
  component by *referencing* its class, e.g. `<panel class="topbar_master_meters"
  name="master_options" x="+802+…" y="8"/>`. VirtualDJ inlines the define's
  contents into that panel when it renders.

When a layout references a component this way, responsibilities split cleanly:

- The **reference** (in the layout) owns *where/whether*: `x`/`y`, `name`,
  `visibility`, `condition`. Sibling order still matters — relative offsets
  (`y="+5"`, `x="+802+…"`) chain from the previous sibling.
- The **define** (the component) owns *what*: its inner elements, positioned
  relative to the reference's origin.

A `<define>` may contain a whole region (many elements), and the idiomatic way to
place it is a single `<panel class="…">` reference — see `EQ_MIXER_PANE`
(`center-panel/eq-mixer.xml`) and the bar components under
`src/components/topbar` / `src/components/bottombar`. Referencing a group-shaped
define as a `<panel>` is expected; the panel is a transparent container, so the
region renders exactly as if its elements sat inline.

- Bars/screen modes are **layouts** (`src/layouts/`): they compose components via
  classes and are included into `skin.xml` as modules.
- Their reusable pieces are **components** (`src/components/…`): each a `<define>`
  registered through an `index.xml` hub. Do not compose an on-screen bar by
  XInclude-flattening fragments — load the pieces as classes so the layout reads
  as "which component, where, when".

## Audits

- `scripts/audit-class-casing.py` enforces class-definition/reference casing and catches missing class definitions.
- `scripts/audit-structure.py` catches unused definitions, unreachable class islands, unlinked XML files, missing or empty XInclude targets, unexpected duplicate definitions, and new always-hidden blocks.
- `scripts/audit-state-vars.py` requires every concrete skin variable to be documented in `docs/STATE.md` and restricts `@$skin_mode` to Pro, Performance, and Stack.
- Known duplicate class definitions are deliberate color-scheme variants. Add new duplicates only with a clear reason and update the structural audit allowlist.

## Editing Notes

- Do not edit generated XML as the durable source of truth.
- Keep source changes surgical when fixing a visual/layout bug.
- The worktree may contain unrelated user changes. Do not revert or rewrite files outside the current task.
- After structural or layout changes, run `just check`. For visual behavior changes, follow with `just install` and inspect the skin in VirtualDJ.
