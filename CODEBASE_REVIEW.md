# GraveRaver codebase review

Updated: 2026-10-03. This replaces the historical review and its superseded
paths and recommendations. Remaining implementation tasks live in `TODO.md`.

## Current architecture

`src/skin.xml` is the sole entrypoint. XIncludes assemble the class library;
layouts place runtime components through lowercase class references. Shared
bars live under `src/layouts/`, with their components under `src/components/`.
Keep this separation and avoid introducing another hidden root include layer.

The current checks cover 87 source XML files, 190 class definitions (189 unique),
1,185 references, and 50 registered variables. There are no unused definitions,
unreachable classes, or unlinked XML files. These counts describe the current
source snapshot, not permanent requirements.

## Completed improvements

- Removed the obsolete pad-panel settings repair tool and its command recipes.
- Builds and installs now run the class, structure, and state audits plus tooling
  tests; installation no longer bypasses the audits.
- Reload auditing reads XML attributes regardless of line formatting or quote
  style. Structural writes require a later reload in the same straight-line
  branch. This is a documented convention check, not a complete VDJScript parser.
- Macro templates reject undeclared placeholder tokens. Caller-supplied runtime
  placeholders survive expansion, including names overlapping macro parameters.
- Pro and Performance share `TOPBAR_RACK_TOGGLES`; layouts retain placement.
- `scripts/skin_geometry.py` centralizes waveform ladder dimensions and browser
  rack dimensions/combinations. `scripts/gen-browser-positions.py` emits browser
  position tables, Stack browser tables, and the waveform size ladder.
- Ten regression tests cover reload failures, macro expansion, geometry state
  selection, browser-bottom invariants, and read-only freshness verification.

The geometry refactor preserves the expanded XML. Reconstructing the extracted
rack component also matches the former inline groups; its group-to-panel
composition change was inspected live in Pro and Performance. Full coverage
and outstanding live checks are recorded in `docs/VALIDATION.md`.

## Next priorities

1. Continue sharing geometry in Pro deck positioning, browser overlays/mini
   layouts, and rack shells. Those consumers still repeat dimensions. Preserve
   sibling order and relative-coordinate context, and compare expanded output
   for each small migration.
2. Define behavior when waveform/rack combinations exhaust browser space.
   Pro mixer two-deck with wave size 13 and all racks currently computes browser
   height as 1075-381-312-568 = -186. This predates the refactor and is preserved;
   a behavior fix needs an explicit layout decision and live verification.
3. Finish the live validation matrix, particularly four-deck, extreme wave
   sizes, multiple racks, browser zoom, and window stretching.
4. Review the center-waveform deck-4 cue mask and mirrored-grid differences
   already recorded in `TODO.md`. They are candidates for visual investigation,
   not confirmed defects.
5. Consolidate repeated waveform option menus and remaining Stack rack actions
   only where their behavior matches. Preserve intentional differences.
6. Add focused fixtures for class/structure auditing and minification as those
   tools change. Current tests do not prove every audit or runtime behavior.

Lower-priority cleanup includes LED/sampler repetition and color ownership.
Keep persisted variable identifiers stable and document state in `docs/STATE.md`.
