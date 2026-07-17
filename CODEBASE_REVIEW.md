# GraveRaver Skin Codebase Review

Review date: 2026-07-16
Corrected: 2026-07-18

This is an architectural and maintainability review of the current skin source.
The corrective pass began the documentation-only part of P0; it did not change
skin behavior or XML source structure.

## Overview

### Current health

The repository is in a better structural state than its file sizes initially
suggest:

- `src/skin.xml` is the sole entrypoint.
- The XInclude graph is complete: all 65 XML files are reachable.
- `just check` passes with 163 class definitions, 1,222 references, no unused
  definitions, no unreachable definitions, and no unlinked XML files.
- Class casing and missing class references are audited.
- Generated browser geometry has a clear source script and a freshness check.
- Build output is ignored, and `just install` provides a repeatable bridge from
  source to the live VirtualDJ skin.
- Recent center-panel and rack refactors show a good direction: stable assembly
  classes with smaller responsibility-focused files behind them.

The main problem is therefore not broken structure. It is that valid behavior is
encoded in large files, repeated matrices, implicit state, and long geometry
expressions that make the code difficult to understand and risky to change.

### Architecture as it exists today

The code has four useful layers:

1. `src/skin.xml`, the sole entrypoint, owns the skin metadata, global includes,
   layout-definition includes, and final module layering.
2. `src/components/` owns reusable classes, with partial domain hubs for
   buttons, the Pro center panel, racks, and waveform containers.
3. `src/layouts/` composes those classes into Pro, Performance, Stack, and
   browser/mini surfaces.
4. `scripts/` validates, generates, builds, minifies, and repairs persisted
   VirtualDJ panel state.

That conceptual model is sound, but the directory tree and include hubs do not
express it consistently. `components/index.xml` directly lists individual
components, waveform files, center-panel files, and rack files; `skin.xml`
directly lists most layout definitions; topbar and bottombar are shared
containers layered into every layout; and some domain folders have an
`index.xml` while others do not.

### Main sources of confusion

#### 1. The repository front door has drifted

The intended model is one contributor guide exposed under both tool-specific
names: Claude requires `CLAUDE.md`, while other agents look for `AGENTS.md`.
Before this corrective pass only `CLAUDE.md` existed, and `TODO.md` named the
nonexistent `src/components/containers/topbar/panel.xml`.

P0 has now begun by keeping `CLAUDE.md` as the canonical file, symlinking
`AGENTS.md` to it, identifying `src/skin.xml` as the sole entrypoint, and fixing
the stale topbar path. This matters because these are the first files a
contributor is expected to trust.

#### 2. Several files mix too many responsibilities

The largest hand-written files are:

- `center-waveform.xml`: 1,464 lines / about 115 KB.
- `main-waveform.xml`: 1,012 lines / about 77 KB.
- `topbar.xml`: 894 lines / about 61 KB.
- `meters.xml`: 502 lines.

`topbar.xml` currently contains mode switching, deck-count controls, global sync
settings, the large application options menu, Pro/Performance/Stack controls,
phrase indicators, status lights, master meters, CPU/battery/clock displays,
sandbox code, and platform-specific window controls.

The waveform files combine waveform rendering, deck-order permutations,
dropzones, beat counters, settings menus, mixer menus, zoom controls, and
multiple two-/four-deck variants.

#### 3. State is pervasive but mostly undocumented

The XML uses 47 concrete persistent `@$...` variables. `globals.xml` documents
six of them. Important state families are spread across the topbar, layouts,
waveform files, rack files, meters, and browser surfaces.

Several persisted identifiers are compact, historically branded, or
inconsistently cased, but their meanings are known:

- `@$infntywavesize`: infinity wave size
- `@infospannelmode`: info panel mode
- `@$hntnhvumetercolors`: Haunting VU meter colors; “Haunting” was the skin's
  former name and is now a redundant prefix
- `@$Beat_Marker`: beat marker

The problem is discoverability and legacy naming, not unknown intent. These
names should not be casually corrected because VirtualDJ may persist their
values; document them as compatibility identifiers and introduce clearer
aliases only with a proven migration strategy.

#### 4. Geometry is duplicated as arithmetic rather than expressed as concepts

The same underlying dimensions recur throughout the repository:

- 1920 × 1080 canvas
- topbar/layout offsets
- 800/765-pixel Pro deck widths
- 355/465/333-pixel deck heights
- 80/86/140-pixel rack heights
- the 14-step waveform ladder from 121 to 381 pixels

The waveform ladder is represented independently in waveform sizing, Pro deck
positioning, browser overlays, mini-deck positioning, rack positioning, and the
browser-position generator. This is the highest-risk form of duplication
because every copy can remain syntactically valid while drifting visually.

#### 5. Repeated UI logic is hidden inside large blocks

Examples include:

- The center-waveform options and mixer menus are effectively duplicated in
  both large center-waveform definitions.
- The same Mixer/Video/Effects rack-toggle actions appear in the Pro,
  Performance, and Stack topbar sections.
- The topbar has hand-written LED ladders despite the repository already having
  dedicated meter components.
- `meters.xml` contains three manually expanded LED variants.
- Sampler page selection repeats the same eight-page expression for key, mode,
  edit, and related operations.
- Four-deck waveform orders repeat large 1234/3124/1342 rendering matrices.

#### 6. Disabled and compatibility code has no lifecycle

The structural audit intentionally allowlists three literal
`visibility="false"` blocks. There is also a sandbox group using
`visibility="can_sandbox ? false"`, which is not caught by the literal audit and
appears semantically dead.

Other unresolved markers include:

- disabled transport warning indicators
- disabled layout rulers
- disabled macOS window controls
- commented Pro four-deck transport panels
- temporary rack compatibility wrappers
- several `rgclick="temporary"` placeholder actions
- stale skin-mode checks for modes 4 and 5 even though the current modes are
  0, 1, and 2
- an unused DTD entity that duplicates the current `oninit` action

The problem is not that temporary code exists; it is that the intended outcome
and removal condition are not recorded.

#### 7. Current audits prove structure, not intent

The existing checks are valuable, but they do not detect:

- misspelled or unregistered persistent variables
- references to unsupported skin-mode values
- semantically always-false expressions
- duplicated menus or long action strings
- duplicated color definitions
- geometry ladders drifting between files
- changes to generator logic beyond exact output matching
- behavior regressions visible only in VirtualDJ

The structural audit also parses XML relationships with regular expressions.
That is adequate for the current controlled format, but it should be treated as
a focused convention checker rather than a general XML model.

#### 8. Command behavior is more mutating than its names imply

The bare `just` command defaults to `install`, which writes into the user's
VirtualDJ skin directory. `just lint` also runs `generate`, which can rewrite a
tracked generated file. These behaviors are valid for a local workflow but are
surprising defaults for a new contributor.

The pad repair commands are sensibly dry-run-first and create a backup when
applied, but their external effect on VirtualDJ's `settings.xml` should be more
prominent in the command documentation.

### Recommended direction

The safest cleanup strategy is incremental:

- Preserve `src/skin.xml` as the sole entrypoint and keep `topbar.xml`,
  `bottombar.xml`, and the current layout base files as visible assembly
  surfaces.
- Split implementation behind those assembly surfaces rather than performing
  a large directory move first.
- Document state and geometry before consolidating them.
- Extract exact duplicate UI blocks before redesigning behavior.
- Generate only mechanical matrices whose source representation is clearly
  easier to review than the expanded XML.
- Keep every structural batch small enough to validate with `just check`,
  `just install`, and a focused live layout matrix in VirtualDJ.

A useful eventual shape would be:

```text
src/
  skin.xml
  globals.xml
  components/
    index.xml
    buttons/index.xml
    center-panel/index.xml
    racks/index.xml
    containers/
      topbar.xml              # stable shared-container assembly
      topbar/*.xml            # responsibility-focused fragments
      waveform/index.xml
      waveform/main/*.xml
      waveform/center/*.xml
  layouts/
    definitions.xml           # explicit layout-definition hub
    base.xml                  # visible module assembly
    browser/index.xml
    pro/
    performance/
    stack/
scripts/
  geometry.py or geometry data
  generators/
  audits/
docs/
  architecture.md
  state.md
  validation.md
```

This is a target shape, not a recommendation to move everything in one commit.

## Prioritized tasks

### P0 — Make the current system truthful and safe to navigate

#### 1. Repair the repository front door

Keep `CLAUDE.md` as the canonical guide and expose the same content through an
`AGENTS.md` symlink. Update stale paths and make that one file the authoritative
source map. Update `TODO.md` so its targets match the current tree.

Status: started 2026-07-18. The guide/symlink decision, sole-entrypoint wording,
container roles, generated browser filename, and stale TODO topbar path are now
aligned.

Include:

- the real generated browser filename
- `src/skin.xml` as the sole entrypoint
- topbar and bottombar as shared containers shown on every layout
- the role of `components/index.xml`, layout definitions, and final modules
- which commands mutate source, build output, the installed skin, or VirtualDJ
  settings
- the required source → check → install → live validation loop

Done when a new contributor can locate the root, a component, a layout, a
generated file, and the live install path without searching commit history.

#### 2. Make command mutation explicit

Change the default `just` target to a non-mutating `help` or `check` target.
Keep `install` explicit. Make `lint` verify generated output rather than
silently regenerate it; reserve generation for `generate`, `build`, or an
explicit update command.

Add short descriptions for:

- read-only checks
- source-generating commands
- build-directory writes
- VirtualDJ skin installation
- VirtualDJ settings repair

Done when command names and default behavior accurately signal their side
effects.

#### 3. Audit and resolve stale/disabled code before moving it

Review every currently allowlisted or disguised disabled block and classify it
as one of:

- active feature to restore
- debug tool to isolate behind a deliberate debug switch/include
- compatibility shim with a named consumer and removal condition
- dead code to delete

Start with:

- `layouts/base.xml` rulers
- transport warning indicators
- disabled macOS window controls
- the sandbox group
- commented Pro four-deck transport panels
- `PRO_RACKS` and `RACKS_STACK` compatibility comments/wrappers
- `rgclick="temporary"`
- skin-mode checks for modes 4 and 5
- `macros.dtd` versus the duplicated literal `oninit` action

Do not combine this with visual redesign. The goal is to establish what is
intentional before files are split.

#### 4. Create a persistent-state registry and compatibility policy

Document every concrete `@$...` and `@...` skin variable with:

- purpose
- allowed values
- default/fallback behavior
- writers
- main readers
- whether changing it requires `load_skin`
- whether it is persisted by VirtualDJ
- whether its current name is a compatibility name

Group variables by layout, browser, waveform, rack, meter, jog, and display
state. Add an audit that flags unregistered variables and unknown values for
closed enums such as `@$skin_mode`.

Do not rename historical identifiers until a migration strategy is proven.
Seed the registry with the known meanings of infinity wave size, info panel
mode, Haunting VU meter colors, and beat marker so their legacy spelling or
branding is no longer mistaken for unknown state.

### P1 — Reduce the largest and most duplicated maintenance surfaces

#### 5. Split the shared `topbar.xml` container by responsibility

Keep `src/components/containers/topbar.xml` as the shared container assembly,
but compose it from focused fragments such as:

- background and mode switcher
- deck count and global sync controls
- application/options menu
- Pro controls
- Performance controls
- Stack controls
- phrase indicators
- status/action indicators
- master meters, CPU, battery, and clock
- platform window controls

Extract shared rack-toggle controls so Pro, Performance, and Stack do not carry
three copies of the same long action strings.

Done when `topbar.xml` communicates layering/order at a glance and no fragment
needs knowledge of unrelated topbar responsibilities.

#### 6. Extract shared waveform and mixer option components

The waveform type/color/needle/order menu and the mixer options menu are
duplicated across center and main waveform surfaces. Define each menu once as a
reusable class with position/visibility placeholders where necessary.

Also extract the shared zoom control pair and any repeated 2/4-wave selector.

Do this before splitting the rendering matrices; it is a smaller, readily
verifiable reduction in duplication.

#### 7. Split the giant waveform files by rendering responsibility

Keep `main-waveform.xml` and `center-waveform.xml` as stable include/definition
hubs. Move coherent blocks behind them:

- Beats and mirrored Beats renderers
- Scratch/Shapes renderers
- two-deck and four-deck dropzones
- deck-order matrices
- beat-counter overlays
- split-wave/grid variants
- settings and zoom controls

For `center-waveform.xml`, explicitly model the relationship between
`WAVEFORM_HORIZONTAL_CENTER` and `WAVEFORM_HORIZONTAL_CENTER4`; their shared
menus and four-deck order matrices should not remain duplicated.

Done when each file can be understood without scrolling across unrelated
rendering modes and the public class names remain unchanged.

#### 8. Establish one source for waveform ladders and rack geometry

Expand the successful browser-position generator pattern into a small,
well-documented geometry source that owns:

- the 14 waveform sizes
- rack heights and gaps
- common canvas/bar/deck dimensions
- generated position ladders for browser overlays, Pro deck placement,
  mini-deck placement, and rack placement where mechanical expansion is
  unavoidable

Prefer named data and small generators over DTD entities containing opaque
arithmetic. Generated files must:

- identify their source
- be deterministic
- be freshness-checked by `just check`
- remain readable enough to diagnose runtime behavior

Do not generate free-form layout composition; generate only repeated tables.

#### 9. Add explicit domain include hubs

Introduce clear hubs such as:

- `components/racks/index.xml`
- `components/containers/waveform/index.xml`
- `layouts/browser/index.xml`
- `layouts/definitions.xml`

Then make `components/index.xml` and `skin.xml` describe domains rather than
enumerating most leaf files. Keep `src/skin.xml` as the visible root and avoid a
generic hidden `src/index.xml`.

This should reduce layout-add touch points and make ownership obvious without
deepening the tree unnecessarily.

#### 10. Consolidate mechanical UI ladders

After the geometry and waveform work is stable, address other high-volume
mechanical repetition:

- VU LED ladders in `meters.xml`
- the topbar master/CPU/battery meter ladders
- sampler page offset expressions
- repeated four-deck order tables

Choose between a reusable XML class and generation based on whether the
difference is semantic:

- use a class when the same UI structure is reused with different parameters
- use generation when the runtime requires many explicitly expanded rows

### P2 — Strengthen conventions and regression protection

#### 11. Extend audits from reachability to repository conventions

Add focused checks for:

- registered persistent variables
- valid values for known layout enums
- stale path references in repository docs
- generated-file headers and freshness
- literal and simple semantically dead visibility expressions
- compatibility markers without an owner/removal note
- placeholder names and class names that violate the chosen naming convention

Keep these checks narrow and explainable. Avoid pretending to fully validate
VDJScript without a reliable parser or VirtualDJ runtime.

#### 12. Add tests for the Python tooling

Add small fixture-based tests for:

- browser-position generation order and boundary values
- structure-audit include reachability and duplicate handling
- class-casing checks
- pad-panel repair token selection and settings backup behavior
- minifier comment/whitespace handling

The current scripts are important enough that changes to the safety net itself
should not rely only on running it against the current repository.

#### 13. Normalize naming and comments without breaking persisted state

Define conventions for:

- file names
- public class names
- private/helper class names
- group/panel names
- placeholders
- persistent variables
- comments that explain why rather than restating the XML

Fix local typos such as `mirroredtwave` when they are not persisted/public.
For persisted or externally referenced names, document the compatibility name
and defer renaming until migration is safe.

Remove comments that refer to old structures, empty wrapper comments, and
comments that merely repeat the next tag.

#### 14. Define a live validation matrix

Create a short checklist for structural and visual refactors covering the
combinations most likely to drift:

- Pro mixer and extended variants
- two-deck swap and full four-deck
- waves above, below, and hidden
- minimum and maximum waveform sizes
- browser zoom on/off
- single- and multi-rack combinations
- Performance vertical/horizontal
- Stack mode
- macOS/Windows-only topbar branches where available

Every structural batch should finish with:

1. `just check`
2. `git diff --check`
3. `just install`
4. focused inspection in VirtualDJ using the affected matrix rows

#### 15. Review color/theme ownership separately

`colors.xml` is manageable in size but mixes shape palettes, deck colors,
monochrome/day variants, master colors, and general UI tokens. It also relies
on repeated conditional color definitions.

After higher-risk layout work, split it into explicit palette families or add a
small color index. Extend auditing only after confirming how VirtualDJ resolves
conditional duplicate color definitions. This is lower priority because the
current class and layout structure presents a greater maintenance risk.

## Suggested execution order

The recommended implementation sequence is:

1. Tasks 1–4: truthful docs, safer commands, stale-code decisions, state map.
2. Tasks 5–6: topbar assembly and exact menu/action extraction.
3. Tasks 7–8: waveform split and shared geometry generation.
4. Tasks 9–10: include hubs and remaining mechanical ladders.
5. Tasks 11–15: stronger audits, tool tests, naming, validation, and colors.

This order front-loads low-risk clarity work, then removes exact duplication
before attempting broader structural consolidation.
