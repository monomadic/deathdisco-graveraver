# TODO

Cleanup backlog after the prototype/index removal and structural audit work.

## Done

- [x] Remove prototype skin sources and keep `src/skin.xml` as the real skin root.
- [x] Remove unused class islands, orphan XML files, and empty include targets.
- [x] Add structural auditing to `just check` via `scripts/audit-structure.py`.
- [x] Keep one contributor guide: `CLAUDE.md`, with `AGENTS.md` symlinked to it.
- [x] Make bare `just`, linting, generation, builds, installs, and settings repair explicit about their side effects.

## Next Cleanup Tasks

- [ ] Split the giant waveform files.
  - Main targets: `src/components/containers/waveform/center-waveform.xml` and `src/components/containers/waveform/main-waveform.xml`.
  - Look for repeated waveform/dropzone/menu matrices that can become smaller includes, shared helper defines, or generated XML.

- [ ] Split the topbar by responsibility.
  - Main target: `src/components/containers/topbar.xml`.
  - Suggested pieces: layout switcher, global settings, browser/options menu, Pro utilities, Performance utilities, Stack utilities.
  - Keep `topbar.xml` as the shared topbar container, but make it read like an assembly file. `src/skin.xml` remains the sole entrypoint.

- [ ] Resolve stale compatibility and disabled-code cruft.
  - Review comments such as temporary compatibility aliases in rack files.
  - Decide whether the disabled warning/debug blocks should become real features, debug-only includes, or be deleted.

- [ ] Normalize repeated geometry constants.
  - Repeated values include canvas size, topbar/bottombar heights, deck heights, browser offsets, and rack/deck widths.
  - Prefer local placeholders or clearly named helper defines over another opaque root include layer.

- [ ] Fix the macro story.
  - Either use the existing `src/macros.dtd` entity macros where they help, or remove the unused macro layer.
  - Avoid leaving preprocessor-only indirection that is not actively earning its keep.

- [ ] Reduce layout-add touch points.
  - Adding a new layout currently requires changes across `src/skin.xml`, `src/layouts/base.xml`, topbar controls, and the layout files.
  - Create an explicit, visible layout-mode switch pattern so new layouts can be added quickly without reintroducing a confusing `src/index.xml`.

- [ ] Consider generators for repeated visual ladders and matrices.
  - Candidate areas: VU meter LEDs, waveform variants, sampler rows, and browser/deck position tables.
  - Generated output should have a source script and be checked by `just check`.
