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
