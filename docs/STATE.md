# Skin State Registry

This registry covers every concrete GraveRaver variable referenced by the XML.
It is checked by `scripts/audit-state-vars.py`; add a row here whenever a new
skin variable is introduced.

Every GraveRaver variable carries the `dd_` prefix, because VirtualDJ keeps all `@$` variables in one pool shared by every skin (the built-in skins read `@$4decks`, `@$4waveforms`, and `@$phrasecircle`). `@$…` names are skin-global state persisted by VirtualDJ. Unset numeric values
are treated as `0` by the existing conditions. `@…` names are local/deck state;
the skin does not rely on them surviving a reload. “Reload” means writers call
`load_skin` because the value changes structural layout or definitions.

Renaming persisted state discards a user's saved choice, so names change only in
a deliberate migration. The one migration so far is the 2026-09-09 `dd_` prefix
pass (see the end of this file).

## Layout and browser state

| Variable | Values / fallback | Purpose and main owners | Reload | Compatibility |
| --- | --- | --- | --- | --- |
| `@$dd_skin_mode` | `0` Pro, `1` Performance, `2` Stack; fallback `0` | Written by topbar mode buttons; read by `skin.xml`, layout bases, menus, and topbar sections. | Yes | No |
| `@$dd_layout_4deck` | `0` two-deck/swap, `1` full four-deck; fallback `0` | Deck-density switch written by topbar and read across every layout. | Yes | No |
| `@$dd_performance_layout` | `0` vertical, `1` horizontal; fallback `0` | Performance topbar cycle; read by `layouts/performance/base.xml`. | Yes | No |
| `@$dd_hide_pro_mixer` | `0` mixer, `1` extended; fallback `0` | Pro topbar toggle; selects the Pro center-mixer variant. | Yes | No |
| `@$dd_stack_controls` | `0` expanded waveform, `1` stack controls; fallback `0` | Stack topbar PADS toggle; read by stack deck strips. | No | No |
| `@$dd_bottombar_mode` | `0` browser tools, `1` custom buttons; fallback `0` | Written by topbar options and bottombar toggle; read by `bottombar.xml`. | No | No |
| `@$dd_hide_transport` | `0` show, `1` hide; fallback `0` | “Hide Transport” option for vertical controls; name no longer matches the whole affected surface. | Yes | No |
| `@$dd_bordermode` | `0` normal, `1` show keyboard/selected-deck borders; fallback `0` | Topbar “Keyboard Mode”; read by deck and stack selection borders. | No | No |

## Waveform state

| Variable | Values / fallback | Purpose and main owners | Reload | Compatibility |
| --- | --- | --- | --- | --- |
| `@$dd_hide_main_waveforms` | `0` show, `1` hide; fallback `0` | Topbar option; selects main layout shells and rack placement. | Yes | No |
| `@$dd_hide_zoom_waveforms` | `0` show, `1` hide; fallback `0` | Topbar/browser-zoom option; selects mini-deck shells and geometry. | Yes | No |
| `@$dd_wave_size` | `0…13`, smallest to largest; fallback `0` | Infinity wave size, cycled by main waveform controls and read by waveform/layout geometry. | Yes | No |
| `@$dd_four_waveforms` | `0` left/right active decks, `1` all four decks; fallback `0` | Waveform menus and selectors; read by main, center, and vertical waveform variants. | No | No |
| `@$dd_mirror_waveforms` | `0` normal, `1` mirrored; fallback `0` | Waveform option menus; read by Beats renderers. | No | No |
| `@$dd_split_waveform` | `0` unified, `1` split; fallback `0` | Read by main waveform rendering and menus; no writer currently exists in this skin. | No | Retained external/legacy control |
| `@$dd_wave_grid_mode` | `0` grid off variant, `1` grid on variant; fallback `0` | Read by scratch waveform matrices; no writer currently exists in this skin. | No | Retained external/legacy control |
| `@$dd_wave_order` | `0` 3-1-2-4, `1` 1-2-3-4, `2` 1-3-4-2; fallback `0` | Waveform menus; read by four-deck rendering matrices. | No | No |
| `@$dd_waveform_position` | `0` above, `1` below; fallback `0` | Main waveform menu; selects normal and browser-zoom layout shells. | Yes | No |
| `@$dd_wave_hide_background` | `0` show colored background, `1` suppress it; fallback `0` | Waveform option menus; read by scratchwave visibility. | No | No |
| `@$dd_shapes_color` | `0` VirtualDJ-like, `1` Pioneer-like, `2` Denon-like; fallback `0` | Waveform color menus; read by color definitions. | Yes | No |
| `@$dd_beat_marker` | `0` off, `1` 32 beats, `2` 64 beats, `3` 128 beats/32 bars; fallback `0` | Song-position waveform menu and beat markers. | No | No |
| `@$dd_show_bar_counter` | `0` hide, `1` show; fallback `0` | Waveform menus; read by horizontal beat-counter overlays. | No | No |
| `@$dd_show_bar_counter_vertical` | `0` hide, `1` show; fallback `0` | Vertical control menu; read by vertical bar counters. | No | No |

## Racks, mixer, and display state

| Variable | Values / fallback | Purpose and main owners | Reload | Compatibility |
| --- | --- | --- | --- | --- |
| `@$dd_rack_mode` | `0` multi-rack, `1` single-rack; fallback `0` | Topbar rack mode menu and mutually-exclusive rack buttons. | Mixed | No |
| `@$dd_show_fx_rack` | `0` hide, `1` show; fallback `0` | Topbar rack buttons; read by rack surfaces and generated browser geometry. | Yes | No |
| `@$dd_show_mixer_rack` | `0` hide, `1` show; fallback `0` | Topbar rack buttons; read by rack surfaces and generated browser geometry. | Yes | No |
| `@$dd_show_video_rack` | `0` hide, `1` show; fallback `0` | Topbar rack buttons; read by rack surfaces and generated browser geometry. | Yes | No |
| `@$dd_show_zoom_racks` | `0` hide, `1` show; fallback `0` | Topbar browser-zoom option; read by mini layout geometry. | Yes | No |
| `@$dd_show_center_fx_rack` | `0` center mixer, `1` center effects; fallback `0` | Center waveform/mixer menus and rack toggle; read by center rack container. | No | No |
| `@$dd_left_rack_headphones` | `0` microphone, `1` headphones; fallback `0` | Mixer menus and left rack toggle; read by left extended rack. | No | No |
| `@$dd_right_rack_record` | `0` master, `1` record/broadcast; fallback `0` | Mixer menus and right rack toggle; read by right extended rack. | No | No |
| `@$dd_vu_alt_colors` | `0` standard, `1` alternate VU colors; fallback `0` | Mixer/waveform menus; read by meter color definitions. | No | No |
| `@$dd_show_peak_meter` | `0` standard, `1` peak display; fallback `0` | Mixer/waveform menus; read by meter components. | No | No |
| `@$dd_hide_drop_menus` | `0` show dropdown affordances, `1` hide; fallback `0` | Mixer/waveform menus; read by dropdown visibility. | No | No |
| `@$dd_show_scratch_buttons` | `0` hide, `1` show; fallback `0` | Vertical controls menu and scratch controls. | No | No |
| `@$dd_show_cover_title` | `0` hide cover/title treatment, `1` show; fallback `0` | Main deck menu and track-info layouts. | No | No |
| `@$dd_show_battery` | `0` hide, `1` show; fallback `0` | Topbar options and battery display. | No | No |
| `@$dd_color_scheme` | `0` Default, `1` Dark, `2` Darker, `3` Night, `4` Day; fallback `0` | Topbar scheme menu; read by colors and buttons. | Yes | No |
| `@$dd_deck_colors` | `0` per-deck, `1` neutral; fallback `0` | Topbar scheme menu; read by deck color definitions. | Yes | No |
| `@$dd_jog_type` | `0` needle, `1` text, `2` sync status, `3` cover art; fallback `0` | Topbar and jog menus; read by jogwheel components. | No | No |
| `@$dd_jog_display_mode` | `0` jog mode, `1` loop size, `2` elapsed, `3` remaining; fallback `0` | Jog text submenu; read by jogwheel text. | No | No |
| `@$dd_jog_bpm_digits` | `0` one decimal, `1` two decimals; fallback `0` | Topbar BPM menu; read by jog and track BPM text. | Yes | No |
| `@$dd_bpm_mask` | `0` show BPM, `1` mask BPM; fallback `0` | Topbar BPM menu; read by jog and track BPM text. | No | No |
| `@$dd_phrase_circle` | `0` phrase bars, `1` phrase circles; fallback `0` | Topbar options; read by phrase indicators. | No | No |
| `@$dd_time_display_mode` | `0…2`, three track-time display modes; fallback `0` | Cycled from track-info components and read by their time zones. | No | No |
| `@$dd_track_stats_time` | `0` remaining, `1` elapsed, `2` total; fallback `0` | Cycled by clicking the time column of `TRACK_INFO_STATS`; read by its label, value, and detail. | No | No |

## Deck-local state

| Variable | Values / fallback | Purpose and main owners | Reload | Compatibility |
| --- | --- | --- | --- | --- |
| `@dd_deck_mode` | `0` jog/transport, `1` pads, `2` saved loops; fallback `0` | Cycled per Stack deck and read by its control panel. | No | No |
| `@dd_fx_rack_panel` | `0` FX banks, nonzero stem FX; fallback `0` | Toggled per deck by rack controls; read by effects racks. | No | No |
| `@dd_title_scroll` | boolean; fallback `0` | Per-deck title text scrolling in Stack track info. | No | No |
| `@dd_info_panel_mode` | `0` grid, `1` loops, `2` hot cues, `3` timecode/line-in, `4` custom buttons; fallback `0` | Info panel mode, written by deck menus/cycles and read by mini/stack info panels. | No | No |

## Compatibility policy

- Do not rename an existing `@$…` variable in place. Add a migration or alias
  only after confirming how VirtualDJ persists and initializes both names.
- New variables use lower snake case with the `dd_` prefix and a descriptive, non-branded name.
- A closed enum must list every supported numeric value here and in the state
  audit when it controls top-level structure.
- Writerless variables are documented as such; do not infer an in-skin control.
- `load_skin` should be used only when the current rendering structure requires
  it, and that requirement should remain visible in the writer action.
- The skin runs the 4-deck engine unconditionally (`<nbdecks value="4"/>` in
  `globals.xml`). Its waveform and track-info visibility chains query decks 3/4,
  which alias onto real decks on a 2-deck engine.

## 2026-09-09 rename

All variables gained the `dd_` prefix in one pass; no migration shim reads the
old names. Old values are simply abandoned. `@$4decks` (shared with the built-in
skins) and the writer-only `@$show_pads_rack` were removed instead of renamed.

| Old | New |
| --- | --- |

| @$skin_mode | `@$dd_skin_mode` |
| @$layout_4deck | `@$dd_layout_4deck` |
| @$performance_layout | `@$dd_performance_layout` |
| @$hide_pro_mixer | `@$dd_hide_pro_mixer` |
| @$deck_stack | `@$dd_stack_controls` |
| @$browser_zoom_mode | removed 2026-10-03 (writerless legacy auto-switch branch deleted; layouts now read `browser_zoom` directly) |
| @$bottombar_mode | `@$dd_bottombar_mode` |
| @$hide_crossfader | `@$dd_hide_transport` |
| @$hide_main_waveforms | `@$dd_hide_main_waveforms` |
| @$hide_zoom_waveforms | `@$dd_hide_zoom_waveforms` |
| @$infntywavesize | `@$dd_wave_size` |
| @$4waveforms | `@$dd_four_waveforms` |
| @$mirror_waveforms | `@$dd_mirror_waveforms` |
| @$split_waveform | `@$dd_split_waveform` |
| @$wave_grid_mode | `@$dd_wave_grid_mode` |
| @$wave_order | `@$dd_wave_order` |
| @$waveform_position | `@$dd_waveform_position` |
| @$waves_show_background | `@$dd_wave_hide_background` |
| @$shapes_color | `@$dd_shapes_color` |
| @$Beat_Marker | `@$dd_beat_marker` |
| @$show_bar_counter | `@$dd_show_bar_counter` |
| @$show_bar_counter_vert | `@$dd_show_bar_counter_vertical` |
| @$rack_mode | `@$dd_rack_mode` |
| @$show_fx_rack | `@$dd_show_fx_rack` |
| @$show_mixer_rack | `@$dd_show_mixer_rack` |
| @$show_video_rack | `@$dd_show_video_rack` |
| @$show_zoom_racks | `@$dd_show_zoom_racks` |
| @$show_center_fx_rack | `@$dd_show_center_fx_rack` |
| @$show_left_mixer_rack | `@$dd_left_rack_headphones` |
| @$show_right_mixer_rack | `@$dd_right_rack_record` |
| @$hntnhvumetercolors | `@$dd_vu_alt_colors` |
| @$show_peak_meter | `@$dd_show_peak_meter` |
| @$show_drop_menus | `@$dd_hide_drop_menus` |
| @$show_scratch_buttons | `@$dd_show_scratch_buttons` |
| @$show_cover_title | `@$dd_show_cover_title` |
| @$show_battery | `@$dd_show_battery` |
| @$color_scheme | `@$dd_color_scheme` |
| @$deck_colors | `@$dd_deck_colors` |
| @$jog_type | `@$dd_jog_type` |
| @$jog_display_mode | `@$dd_jog_display_mode` |
| @$jog_bpm_digits | `@$dd_jog_bpm_digits` |
| @$bpm_hide_options | `@$dd_bpm_mask` |
| @$phrasecircle | `@$dd_phrase_circle` |
| @$hauntinstimesdisplay | `@$dd_time_display_mode` |
| @deck_mode | `@dd_deck_mode` |
| @fxrackpanel | `@dd_fx_rack_panel` |
| @hntnhtxtscroll | `@dd_title_scroll` |
| @infospannelmode | `@dd_info_panel_mode` |
