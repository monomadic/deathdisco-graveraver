# Skin State Registry

This registry covers every concrete GraveRaver variable referenced by the XML.
It is checked by `scripts/audit-state-vars.py`; add a row here whenever a new
skin variable is introduced.

`@$…` names are skin-global state persisted by VirtualDJ. Unset numeric values
are treated as `0` by the existing conditions. `@…` names are local/deck state;
the skin does not rely on them surviving a reload. “Reload” means writers call
`load_skin` because the value changes structural layout or definitions.

Compatibility names are kept because renaming persisted state can discard a
user's saved choice. A clearer meaning belongs here before any alias or migration
is attempted.

## Layout and browser state

| Variable | Values / fallback | Purpose and main owners | Reload | Compatibility |
| --- | --- | --- | --- | --- |
| `@$skin_mode` | `0` Pro, `1` Performance, `2` Stack; fallback `0` | Written by topbar mode buttons; read by `skin.xml`, layout bases, menus, and topbar sections. | Yes | No |
| `@$layout_4deck` | `0` two-deck/swap, `1` full four-deck; fallback `0` | Deck-density switch written by topbar and read across every layout. | Yes | No |
| `@$4decks` | `0` two active decks, `1` four-deck engine; fallback `0` | Legacy engine/deck-count companion to `layout_4deck`; read by waveform and deck definitions. Current topbar writers set it to `1` for both density buttons. | Yes | Yes: leading digit and overlapping responsibility |
| `@$performance_layout` | `0` vertical, `1` horizontal; fallback `0` | Performance topbar cycle; read by `layouts/performance/base.xml`. | Yes | No |
| `@$hide_pro_mixer` | `0` mixer, `1` extended; fallback `0` | Pro topbar toggle; selects the Pro center-mixer variant. | Yes | No |
| `@$deck_stack` | `0` expanded waveform, `1` stack controls; fallback `0` | Stack topbar PADS toggle; read by stack deck strips. | No | Name is less specific than behavior |
| `@$browser_zoom_mode` | `0` explicit browser zoom only, `1` also follow browser-active state; fallback `0` | Read by all layout bases; no writer currently exists in this skin. | No | Retained external/legacy control |
| `@$bottombar_mode` | `0` browser tools, `1` custom buttons; fallback `0` | Written by topbar options and bottombar toggle; read by `bottombar.xml`. | No | No |
| `@$hide_crossfader` | `0` show, `1` hide; fallback `0` | “Hide Transport” option for vertical controls; name no longer matches the whole affected surface. | No | Yes: historical name |
| `@$dd_bordermode` | `0` normal, `1` show keyboard/selected-deck borders; fallback `0` | Topbar “Keyboard Mode”; read by deck and stack selection borders. | No | Historical `dd` prefix |

## Waveform state

| Variable | Values / fallback | Purpose and main owners | Reload | Compatibility |
| --- | --- | --- | --- | --- |
| `@$hide_main_waveforms` | `0` show, `1` hide; fallback `0` | Topbar option; selects main layout shells and rack placement. | Yes | No |
| `@$hide_zoom_waveforms` | `0` show, `1` hide; fallback `0` | Topbar/browser-zoom option; selects mini-deck shells and geometry. | Yes | No |
| `@$infntywavesize` | `0…13`, smallest to largest; fallback `0` | Infinity wave size, cycled by main waveform controls and read by waveform/layout geometry. | No | Yes: compact spelling |
| `@$4waveforms` | `0` left/right active decks, `1` all four decks; fallback `0` | Waveform menus and selectors; read by main, center, and vertical waveform variants. | No | Yes: leading digit |
| `@$mirror_waveforms` | `0` normal, `1` mirrored; fallback `0` | Waveform option menus; read by Beats renderers. | No | No |
| `@$split_waveform` | `0` unified, `1` split; fallback `0` | Read by main waveform rendering and menus; no writer currently exists in this skin. | No | Retained external/legacy control |
| `@$wave_grid_mode` | `0` grid off variant, `1` grid on variant; fallback `0` | Read by scratch waveform matrices; no writer currently exists in this skin. | No | Retained external/legacy control |
| `@$wave_order` | `0` 3-1-2-4, `1` 1-2-3-4, `2` 1-3-4-2; fallback `0` | Waveform menus; read by four-deck rendering matrices. | No | No |
| `@$waveform_position` | `0` above, `1` below; fallback `0` | Main waveform menu; selects normal and browser-zoom layout shells. | Yes | No |
| `@$waves_show_background` | `0` show colored background, `1` suppress it; fallback `0` | Waveform option menus; read by scratchwave visibility. | No | Negative behavior is not obvious from name |
| `@$shapes_color` | `0` VirtualDJ-like, `1` Pioneer-like, `2` Denon-like; fallback `0` | Waveform color menus; read by color definitions. | Yes | No |
| `@$Beat_Marker` | `0` off, `1` 32 beats, `2` 64 beats, `3` 128 beats/32 bars; fallback `0` | Song-position waveform menu and beat markers. | No | Yes: inconsistent casing; means beat marker |
| `@$show_bar_counter` | `0` hide, `1` show; fallback `0` | Waveform menus; read by horizontal beat-counter overlays. | No | No |
| `@$show_bar_counter_vert` | `0` hide, `1` show; fallback `0` | Vertical control menu; read by vertical bar counters. | No | Abbreviated suffix |

## Racks, mixer, and display state

| Variable | Values / fallback | Purpose and main owners | Reload | Compatibility |
| --- | --- | --- | --- | --- |
| `@$rack_mode` | `0` multi-rack, `1` single-rack; fallback `0` | Topbar rack mode menu and mutually-exclusive rack buttons. | Mixed | No |
| `@$show_fx_rack` | `0` hide, `1` show; fallback `0` | Topbar rack buttons; read by rack surfaces and generated browser geometry. | Yes | No |
| `@$show_mixer_rack` | `0` hide, `1` show; fallback `0` | Topbar rack buttons; read by rack surfaces and generated browser geometry. | Yes | No |
| `@$show_video_rack` | `0` hide, `1` show; fallback `0` | Topbar rack buttons; read by rack surfaces and generated browser geometry. | Yes | No |
| `@$show_pads_rack` | Writers clear to `0`; fallback `0` | Legacy single-rack exclusivity flag. No current reader or enable writer exists. | Yes | Candidate removal after settings compatibility check |
| `@$show_zoom_racks` | `0` hide, `1` show; fallback `0` | Topbar browser-zoom option; read by mini layout geometry. | Yes | No |
| `@$show_center_fx_rack` | `0` center mixer, `1` center effects; fallback `0` | Center waveform/mixer menus and rack toggle; read by center rack container. | No | No |
| `@$show_left_mixer_rack` | `0` microphone, `1` headphones; fallback `0` | Mixer menus and left rack toggle; read by left extended rack. | No | Name describes location, not content |
| `@$show_right_mixer_rack` | `0` master, `1` record/broadcast; fallback `0` | Mixer menus and right rack toggle; read by right extended rack. | No | Name describes location, not content |
| `@$hntnhvumetercolors` | `0` standard, `1` alternate VU colors; fallback `0` | Mixer/waveform menus; read by meter color definitions. | No | Yes: Haunting VU meter colors; old skin name is redundant |
| `@$show_peak_meter` | `0` standard, `1` peak display; fallback `0` | Mixer/waveform menus; read by meter components. | No | No |
| `@$show_drop_menus` | `0` show dropdown affordances, `1` hide; fallback `0` | Mixer/waveform menus; read by dropdown visibility. | No | Inverted value semantics |
| `@$show_scratch_buttons` | `0` hide, `1` show; fallback `0` | Vertical controls menu and scratch controls. | No | No |
| `@$show_cover_title` | `0` hide cover/title treatment, `1` show; fallback `0` | Main deck menu and track-info layouts. | No | No |
| `@$show_battery` | `0` hide, `1` show; fallback `0` | Topbar options and battery display. | No | No |
| `@$color_scheme` | `0` Default, `1` Dark, `2` Darker, `3` Night, `4` Day; fallback `0` | Topbar scheme menu; read by colors and buttons. | Yes | No |
| `@$deck_colors` | `0` per-deck, `1` neutral; fallback `0` | Topbar scheme menu; read by deck color definitions. | Yes | No |
| `@$jog_type` | `0` needle, `1` text, `2` sync status, `3` cover art; fallback `0` | Topbar and jog menus; read by jogwheel components. | No | No |
| `@$jog_display_mode` | `0` jog mode, `1` loop size, `2` elapsed, `3` remaining; fallback `0` | Jog text submenu; read by jogwheel text. | No | No |
| `@$jog_bpm_digits` | `0` one decimal, `1` two decimals; fallback `0` | Topbar BPM menu; read by jog and track BPM text. | Yes | No |
| `@$bpm_hide_options` | `0` show BPM, `1` mask BPM; fallback `0` | Topbar BPM menu; read by jog and track BPM text. | No | Awkward historical name |
| `@$phrasecircle` | `0` phrase bars, `1` phrase circles; fallback `0` | Topbar options; read by phrase indicators. | No | No |
| `@$hauntinstimesdisplay` | `0…2`, three track-time display modes; fallback `0` | Cycled from track-info components and read by their time zones. | No | Yes: Haunting-era spelling/name |

## Deck-local state

| Variable | Values / fallback | Purpose and main owners | Reload | Compatibility |
| --- | --- | --- | --- | --- |
| `@deck_mode` | `0` jog/transport, `1` pads, `2` saved loops; fallback `0` | Cycled per Stack deck and read by its control panel. | No | No |
| `@fxrackpanel` | `0` FX banks, nonzero stem FX; fallback `0` | Toggled per deck by rack controls; read by effects racks. | No | No |
| `@hntnhtxtscroll` | boolean; fallback `0` | Per-deck title text scrolling in Stack track info. | No | Yes: Haunting-era prefix |
| `@infospannelmode` | `0` grid, `1` loops, `2` hot cues, `3` timecode/line-in, `4` custom buttons; fallback `0` | Info panel mode, written by deck menus/cycles and read by mini/stack info panels. | No | Yes: persisted spelling means info panel mode |

## Compatibility policy

- Do not rename an existing `@$…` variable in place. Add a migration or alias
  only after confirming how VirtualDJ persists and initializes both names.
- New variables use lower snake case and a descriptive, non-branded name.
- A closed enum must list every supported numeric value here and in the state
  audit when it controls top-level structure.
- Writerless variables are documented as such; do not infer an in-skin control.
- `load_skin` should be used only when the current rendering structure requires
  it, and that requirement should remain visible in the writer action.
