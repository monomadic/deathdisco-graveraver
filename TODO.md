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

- [ ] Split the topbar by responsibility.
  - Main target: `src/components/containers/topbar.xml`.
  - Suggested pieces: layout switcher, global settings, browser/options menu, Pro utilities, Performance utilities, Stack utilities.
  - Keep `topbar.xml` as the shared topbar container, but make it read like an assembly file. `src/skin.xml` remains the sole entrypoint.

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
