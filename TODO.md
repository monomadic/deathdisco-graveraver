# TODO

Cleanup backlog after the prototype/index removal and structural audit work.

## Done

- [x] Remove prototype skin sources and keep `src/skin.xml` as the real skin root.
- [x] Remove unused class islands, orphan XML files, and empty include targets.
- [x] Add structural auditing to `just check` via `scripts/audit-structure.py`.
- [x] Keep one contributor guide: `CLAUDE.md`, with `AGENTS.md` symlinked to it.
- [x] Make bare `just`, linting, generation, builds, installs, and settings repair explicit about their side effects.
- [x] Remove inactive debug, warning, sandbox, window-control, and commented transport blocks; replace placeholder knob actions and stale mode checks.
- [x] Remove the unused `macros.dtd` layer and keep the single startup action visible in `src/skin.xml`.
- [x] Register every concrete skin variable and audit registry coverage plus supported `@$skin_mode` values.

## Next Cleanup Tasks

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

- [ ] Extract shared topbar rack-toggle controls.
  - The MIXER/VIDEO/EFFECTS toggle group is duplicated between
    `components/topbar/pro-utilities.xml` and
    `components/topbar/performance-utilities.xml`, and the per-button action
    strings recur again (with PADS) in `components/topbar/stack-utilities.xml`.
    Fold the identical Pro/Performance group into one reusable class.

- [ ] Normalize repeated geometry constants.
  - Repeated values include canvas size, topbar/bottombar heights, deck heights, browser offsets, and rack/deck widths.
  - Prefer local placeholders or clearly named helper defines over another opaque root include layer.

- [ ] Reduce layout-add touch points.
  - Adding a new layout currently requires changes across `src/skin.xml`, `src/layouts/base.xml`, topbar controls, and the layout files.
  - Create an explicit, visible layout-mode switch pattern so new layouts can be added quickly without reintroducing a confusing `src/index.xml`.

- [ ] Consider generators for repeated visual ladders and matrices.
  - Candidate areas: VU meter LEDs, sampler rows, and the `AREA_WAVES`
    wavesize ladder in `waveform-support.xml`.
  - Prefer VDJ `define` + `placeholders` first (see the waveform split);
    reach for a generator only when rungs need computed arithmetic, and have
    `just check` verify the generated output like browser positions.
