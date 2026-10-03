# TODO

Cleanup backlog after the prototype/index removal and structural audit work.

## Done

- [x] Remove prototype skin sources and keep `src/skin.xml` as the real skin root.
- [x] Remove unused class islands, orphan XML files, and empty include targets.
- [x] Add structural auditing to `just check` via `scripts/audit-structure.py`.
- [x] Keep one contributor guide: `CLAUDE.md`, with `AGENTS.md` symlinked to it.
- [x] Make bare `just`, linting, generation, builds, and installs explicit about their side effects.
- [x] Remove inactive debug, warning, sandbox, window-control, and commented transport blocks; replace placeholder knob actions and stale mode checks.
- [x] Remove the unused `macros.dtd` layer and keep the single startup action visible in `src/skin.xml`.
- [x] Register every concrete skin variable and audit registry coverage plus supported `@$dd_skin_mode` values.

## Next Cleanup Tasks

- [x] Strengthen build validation: run audits and fixture tests before building,
  read multiline XML actions, require reloads in the same branch as structural
  writes, and reject undeclared macro tokens while preserving runtime inputs.

- [x] Split the giant waveform files.
  - `main-waveform.xml` (1012 -> 427 lines) and `center-waveform.xml`
    (1464 -> 334 lines) now build their repeated scratchwave/rhythmzone/counter
    matrices from parameterized defines in `main-waveform-shared.xml` and
    `center-waveform-shared.xml`.
  - Approach: the helper defines are `macro="true"` build-time templates
    expanded by `scripts/expand-skin-macros.py` during `just build`, so
    VirtualDJ only ever sees plain expanded XML. (Relying on VDJ's runtime
    define/placeholder engine for these broke rendering.) Generators stay
    reserved for arithmetic ladders (browser positions).
  - The macro-expanded build was machine-verified canonically identical to
    the pre-refactor build, so rendering must match the last known-good
    skin; confirm in VirtualDJ after `just install`.

- [ ] Waveform follow-ups surfaced by the refactor (deliberate behavior
  changes, need visual confirmation in VirtualDJ):
  - The bottom-half (deck 2/4) center scratchwaves use `shapemirrored="up"`
    and one deck-4 variant uses cue mask height 12 where every sibling uses
    15; they were left verbatim in `center-waveform.xml`. Decide whether the
    differences are intentional and either fold them into
    `center_scratch_pair` placeholders or normalize them.
  - The two `wave_options` menus in `center-waveform.xml` differ by three
    4-deck menu items and stay duplicated; unifying them means showing those
    items (visibility-guarded) in the forced-4-deck variant too.

- [x] Treat the top and bottom bars as layouts and split them into components.
  - The bars are layout objects, so `topbar` and `bottombar` moved out of
    `src/components/containers/` to `src/layouts/topbar.xml` and
    `src/layouts/bottombar.xml`. Each layout owns which component appears
    where/when on the bar (position / name / visibility / condition) and loads
    the pieces via VirtualDJ classes — not xmllint XInclude flattening.
  - The topbar's responsibility regions became component classes under
    `src/components/topbar/` (mode-switcher, deck-count, global-settings,
    utility-actions, options-menu, browser-button, waves-button,
    pro/performance/stack utilities, status-lights, master-meters,
    window-controls). The bottombar's two views became
    `src/components/bottombar/` (browser-tools, custom-buttons). Both have an
    `index.xml` hub included from `src/components/index.xml`.
  - Verification: a per-bar reconstruction (inlining each define body back
    under its reference's attributes) is byte-identical to the original bar
    tree; the only runtime change is the `<group>`→`<panel class>` container,
    which is the same pattern the skin already uses everywhere (e.g.
    `EQ_MIXER_PANE`). This changes the render path, so confirm live in
    VirtualDJ after `just install`.

- [x] Extract shared Pro/Performance topbar rack-toggle controls.
  - Both now load `TOPBAR_RACK_TOGGLES` from `components/topbar/rack-toggles.xml`.
    Reconstructed XML matches the former inline groups. Installed and inspected
    in VirtualDJ, including opening/closing the Performance Mixer rack.
  - 2026-10-03: Stack now uses the same generated `TOPBAR_RACK_TOGGLES` with
    its palette/spacing passed as placeholders; no duplicated actions remain.

- [ ] Normalize repeated geometry constants.
  - Completed first slice: `scripts/skin_geometry.py` owns waveform heights,
    browser waveform offsets, rack heights/gaps, and rack combinations for the
    generated browser tables and `AREA_WAVES` ladder. All outputs are checked
    by `just check`; tests cover every wave size and rack combination.
  - Remaining: Pro deck offsets, browser overlays/mini layouts, and rack shells
    still repeat geometry. Migrate these separately with expanded XML comparisons.
  - Overflow is now prevented at the source: rack toggles are generated with a
    browser-fit guard (`skin_geometry.BROWSER_MIN_HEIGHT`, 120px) and render
    dimmed/inert when showing the rack would overflow. The wave-size buttons are
    not guarded, so growing the wave with racks open can still overflow.
  - Repeated values include canvas size, topbar/bottombar heights, deck heights, browser offsets, and rack/deck widths.
  - Prefer local placeholders or clearly named helper defines over another opaque root include layer.

- [ ] Reduce layout-add touch points.
  - Adding a new layout currently requires changes across `src/skin.xml`, `src/layouts/base.xml`, topbar controls, and the layout files.
  - Create an explicit, visible layout-mode switch pattern so new layouts can be added quickly without reintroducing a confusing `src/index.xml`.

- [ ] Consider generators for repeated visual ladders and matrices.
  - VU meter LEDs are generated (`meters.generated.xml`, 2026-10-03). Sampler
    rows remain a candidate. The `AREA_WAVES` wavesize
    ladder is now generated in `waveform-sizes.generated.xml`.
  - Prefer VDJ `define` + `placeholders` first (see the waveform split);
    reach for a generator only when rungs need computed arithmetic, and have
    `just check` verify the generated output like browser positions.

## 2026-10-03 lint-driven fixes

- [x] `query="on/off"` (not a verb) replaced on 16 buttons with `off` or the
  real toggle state (`var '@$dd_…'`).
- [x] `&&` removed from actions and visibilities (it never guards; both sides
  run). Visibilities now use `a ? b : false`.
- [x] Writerless `@$dd_browser_zoom_mode` legacy branch deleted; layouts read
  `browser_zoom` directly.
- [x] `just check` runs the reference VDJScript linter (`just lint-script`).
- [ ] Remaining lint warnings to decide on: `rightclick="temporary"` in
  `components/pitch.xml` (unknown verb) and the literal colour branches in
  `effects-racks.xml:107` (`color` ternary with quoted hex literals).
- [ ] Live-verify clicking the rack toggles in Pro, Performance and Stack and the
  dimmed state at wave size 13 (rendering/positions verified; clicks not yet).
