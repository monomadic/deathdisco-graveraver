# Skin validation

Run `just check` and `git diff --check` before installing. `just install` also
runs linting, audits, and tooling tests before writing the installed skin.
For a refactor, compare the expanded XML before and after; account explicitly
for any new runtime class wrapper. XML equivalence does not verify a changed
runtime composition path, so inspect the affected controls in VirtualDJ.

## Live matrix

Use the affected rows for a small change and the full matrix for broad geometry
changes. Record actual coverage rather than treating an untested row as passed.
Note initial mode, deck density, wave placement/size, and rack state, and restore
those choices after testing. Avoid transport or audio-control changes.

| Surface | Variants | Inspect |
| --- | --- | --- |
| Pro | Mixer / extended; two / four decks | Deck bounds, center panel, browser space |
| Performance | Vertical / horizontal; two / four decks | Waveforms, controls, browser alignment |
| Stack | Two / four decks; pads shown / hidden | Deck rows, browser top and bottom |
| Shared racks | None; each single; each pair; all three | Toggle hit areas, selected state, rack/browser reflow |
| Rack selection | Single / multiple rack mode | Single mode excludes other racks; multiple mode retains them |
| Main waveforms | Above / below / hidden; sizes 0 and 13 | Cue labels, deck separation, available browser height |
| Browser zoom | Manual / auto; waves and racks shown / hidden | Correct surface appears and controls remain reachable |
| Deck swap | Left 1/3; right 2/4 | Labels, colors, side-specific controls |
| Window sizing | Native canvas and taller window | Breaklines, browser stretch, no background gaps |
| Platform | macOS / Windows when available | Platform-specific controls and fonts |

## 2026-10-03 refactor verification

- Ten tooling/geometry tests pass. Geometry tests exercise all 14 wave states
  and all eight rack combinations, checking rack offsets, consumed height,
  selection order, and preserved browser bottom edges. Freshness checks reject
  stale or missing outputs without writing them.
- All expanded XML matches the pre-refactor tree after reconstructing the new
  shared rack component and ignoring formatting and XInclude source metadata.
  The intentional runtime difference is replacing two inline groups with panel
  references to that component.
- Installed and inspected Pro mixer two-deck with waves below, Performance
  vertical two-deck, and Stack two-deck. Shared controls render in Pro and
  Performance; the Performance Mixer rack opens and closes, moving the browser.
  Returned to the original Pro mode with racks off.
- Other live matrix combinations, including four-deck, waveform extremes,
  multi-rack selection, resize, and Windows, have not been verified in this pass.
- Existing geometry can exhaust browser space: Pro mixer two-deck, wave size
  13 and all racks yields height -186. The refactor retains this existing
  behavior; the tests verify preserved geometry, not universal positive height.

## Pro two-deck visibility correction

The initial visual pass missed a mismatch: selecting deck 1 changed its transport
and center waveform, but the upper deck body still displayed deck 3. Moving the
side-selection visibility from the `deck_container_pro` class reference to an
enclosing group restored deck 1's title, pads, jog wheel, and transport together.
The two-deck overlays/drop zones now use matching outer visibility groups, so
inactive decks do not leave overlapping load targets. Four-deck composition is
unchanged.

Installed and confirmed Pro two-deck displays decks 1 and 2 after the body fix.
The completed version including drop-zone guards passed `just check` and was
installed. After the user finished operating VirtualDJ, checked all four
two-deck pairings: 1/2, 3/4, 1/4, and 3/2. Selected each side through the
four-deck Wave pane, then returned to two-deck mode. Headers, pads, jog wheels,
and transport colors matched the assigned decks without stale upper bodies.
Restored Pro mixer two-deck with decks 1/2, the Wave pane, and racks off.
This verifies mode-transition rendering; dropping tracks onto the guarded load
targets was not exercised, to preserve the loaded tracks.

## 2026-10-03 lint fixes, generated VU meters and rack toggles

- `just check` passes (13 tests) and `just lint-script` reports 0 errors.
- The generated VU meter file was compared element-by-element against the old
  hand-written `meters.xml`: identical after normalising `+6` / `+6*1`.
- Installed and reloaded in Pro mixer two-deck (wave size 6, racks off):
  topbar RACKS frame, label and three buttons render at the former positions
  (screenshot `virtualdj-api-reference/tests/screenshots/virtualdj-20261003-093947.png`
  and a zoom after the `*frame` fix). An unstarred `frame=true` placeholder made
  the framed group disappear; starring it fixed that.
- Not verified: clicking the toggles (showing/hiding a rack), the dimmed inert
  state at large wave sizes, Performance and Stack rendering of the shared
  component. Background clicks do not reach VirtualDJ's canvas, and
  `vdj_execute` was disabled.

### Follow-up (same day)

- Bug: the first guard emitted `… ? var_smaller … : true ? set … : nothing`, so
  only the last leaf guarded the action; Pro/Performance toggles did nothing
  while Stack (last leaf) worked. VDJScript cannot test a computed ternary, so
  the action/`nothing` pair now sits at every leaf (`rack_fit_script(yes=, no=)`).
- Rack toggles use the Stack palette everywhere (black, lit `#222222`, white
  text); Pro/Performance keep the RACKS frame.
- Wave size +/- buttons in Pro: `condition="[SIZEBUTTONS]"` never matched, so
  the 2/4 buttons took their slot; now `param_equal '[SIZEBUTTONS]' 'true'`.
- Reloaded live in Performance vertical: new palette renders inside the frame.
  Toggle clicks and the Pro +/- buttons still need a manual check.

### Outer cue-label rows (four-deck fixed wave strip), 2026-10-03

Goal: the 20px rows above/below the strip should show only cue labels, not a
duplicate wave. Tried, all rejected:

- Label-row scratchwave with `transparent` or `#00000000` colours: the wave is
  still drawn in stem colours (per-element colours ignored for stem waves).
- No separate row; the wave's scratchwave draws cues outside its box
  (`cue y="-15"`): works at 1080p but the breakline band scales the cue text in
  taller windows.
- Row scratchwave with `<size height="0">`: draws nothing at all.
- Row scratchwave with `<size height="1">` plus a 1px cover: VirtualDJ's UI
  hung at 100% CPU on reload (HTTP still answered). Force-quit required.
- Opaque black (`#000000`) colours: installed but never rendered because the
  UI was already hung; untested.

The source is back at the original transparent-colour row. Next idea to test
after a relaunch: the opaque-black colours, then a `songpos`-style strip.
