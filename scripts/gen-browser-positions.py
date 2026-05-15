#!/usr/bin/env python3
"""
Generates src/defs/classes/containers/browser/performance-browser.generated.xml

This file encodes browser panel position/size for every combination of:
  - 2 class variants: browser_performance / browser_performance_mini
  - 2 utility bar states: @$show_utility_bar 0 / 1
  - 8 rack combinations: any subset of fx (80px), mixer (86px), video (140px) racks active
  - 14 waveform sizes: @$infntywavesize 0–13 (step = 20px)

VirtualDJ evaluates <pos> elements in order and applies the first whose condition
matches, so rack combos are listed most-specific-first (3 racks → 2 racks → 1 → 0).

Layout constants (all in px):
  DECK_H       432   total height of the deck area above the browser
  TOPBAR_H      66   top bar
  PADDING_TOP   10
  PADDING_MID   12
  BROWSER_Y_FULL  16   bottom gap for full browser
  BROWSER_Y_MINI 348   bottom gap for mini browser
  UTILITY_EXTRA  38   extra y offset when utility bar is visible
  WAVESIZE_BASE   7   y offset for wavesize=0  (step: +20 per size unit)
  HEIGHT_BASE   121   height constant for wavesize=0 (step: -20 per size unit)

Do not edit the generated file — edit this script instead.
"""

import textwrap
from pathlib import Path

OUTPUT = Path(__file__).parent.parent / "src/defs/classes/containers/browser/performance-browser.generated.xml"

# Rack combos ordered most-specific-first.
# Each entry: (rack_condition_prefix, y_rack_terms, h_rack_terms)
# Conditions use VDJ's `?` as AND; first match wins at runtime.
RACK_COMBOS = [
    (
        "var_equal '@$show_fx_rack' 1 ? var_equal '@$show_mixer_rack' 1 ? var_equal '@$show_video_rack' 1",
        "+80+2+86+2+140+2",
        "-80-2-86-2-140-2",
    ),
    (
        "var_equal '@$show_mixer_rack' 1 ? var_equal '@$show_video_rack' 1",
        "+86+2+140+2",
        "-86-2-140-2",
    ),
    (
        "var_equal '@$show_fx_rack' 1 ? var_equal '@$show_video_rack' 1",
        "+80+2+140+2",
        "-80-2-140-2",
    ),
    (
        "var_equal '@$show_mixer_rack' 1 ? var_equal '@$show_fx_rack' 1",
        "+80+2+86+2",
        "-80-2-86-2",
    ),
    (
        "var_equal '@$show_video_rack' 1",
        "+140+2",
        "-140-2",
    ),
    (
        "var_equal '@$show_mixer_rack' 1",
        "+86+2",
        "-86-2",
    ),
    (
        "var_equal '@$show_fx_rack' 1",
        "+80+2",
        "-80-2",
    ),
    (
        "",  # no racks active
        "",
        "",
    ),
]

# The four define variants and how they differ.
DEFINES = [
    dict(
        cls="browser_performance",
        ubar_cond="var_equal '@$show_utility_bar' 0",
        x_attr="",
        y_tail="-66-10-12-16",
        bg_bordercolor="transparent",
        bg_bordersize="0",
    ),
    dict(
        cls="browser_performance",
        ubar_cond="var_equal '@$show_utility_bar' 1",
        x_attr='x="+0" ',
        y_tail="-66+38-10-12-16",
        bg_bordercolor="xf_progressbackground",
        bg_bordersize="3",
    ),
    dict(
        cls="browser_performance_mini",
        ubar_cond="var_equal '@$show_utility_bar' 0",
        x_attr="",
        y_tail="-66-10-12-348",
        bg_bordercolor="xf_progressbackground",
        bg_bordersize="3",
    ),
    dict(
        cls="browser_performance_mini",
        ubar_cond="var_equal '@$show_utility_bar' 1",
        x_attr='x="+2" ',
        y_tail="-66+38-10-12-348",
        bg_bordercolor="xf_progressbackground",
        bg_bordersize="3",
    ),
]

STATIC_CONTENT = """\
    <background color="xf_progressbackground" bordercolortop="xf_progressbackground" bordercolor="{bg_bordercolor}" bordersize="{bg_bordersize}"/>
    <colors>
      <separators background="button_background" line="button_background" text="needle"/>
      <toolbars background="xf_background" text="needle" iconbackground="xf_progressbackground" backgroundselected="br_coloron" backgroundmouseover="br_slcolor" icon="textoff" border="browser_iconbuttonoff"/>
      <lists background="br_background" stripes="br_stripes" over="xf_progressbackground" overstripes="br_stripes" focus="br_focus" selected="br_slcolor" overtext="needle" text="br_textoff" selectedtext="#ffffff" focustext="#ffffff" automix="br_automix" livefeedback="red" download="#009d9d" scan="#29c814" button="br_stripes" buttonover="button_background2" buttonselected="needle" buttonactive="textoff2" insert="red"/>
      <grids background="br_stripes" over="br_stripes" selected="br_slcolor" focus="br_focus" text="br_textoff" overtext="needle" selectedtext="#ffffff" focustext="#ffffff" stripes="br_stripes" overstripes="br_stripes" selectedstripes="br_stripes" focusstripes="br_stripes" label="needle"/>
      <columns background="br_tb_background" text="br_textoff"/>
      <scrollbars background="tab_menu" button="needle"/>
      <info background="xf_background" stripes="button_background" text="needle" label="br_textoff" artist="textoff2" title="needle"/>
      <search background="xf_progressbackground" border="browser_iconbuttonoff" selected="br_focus" text="needle" cursor="red"/>
      <prelisten background="xf_background" border="panel_background" selected="textdarker" cursor="red" button="needle" buttonbackground="button_background" buttonselected="green"/>
      <plugins background="br_background" text="textoff2" title="xf_background" titletext="texton2">
        <buttons over_deck1="waveform_active1" over_deck2="waveform_active2" over_deck3="waveform_active3" over_deck4="waveform_active4" selected_deck1="waveform_active1" selected_deck2="waveform_active2" selected_deck3="waveform_active3" selected_deck4="waveform_active4" up="button_background" over="br_focus" selected="br_focus" border="transparent" border_selected="transparent" text="needle"/>
        <sliders background="knobprogressoff" needle="needle" deck1="waveform_active1" deck1_disabled="knobfilloff" deck2="waveform_active2" deck2_disabled="knobfilloff" deck3="waveform_active3" deck3_disabled="knobfilloff" deck4="waveform_active4" deck4_disabled="knobfilloff" on="br_focus" on_disabled="knobfilloff"/>
      </plugins>
    </colors>
    <button>
      <up color="browser_iconbuttonoff" border="browser_iconbuttonoff" border_size="2" width="60" height="60"/>
      <over color="browser_iconbuttonactive" border="browser_iconbuttonoff" border_size="2" width="60" height="60"/>
      <down color="browser_iconbuttonactive" border="browser_iconbuttonoff" border_size="2" width="60" height="60"/>
      <selected color="browser_iconbuttonactive" border="browser_iconbuttonoff" border_size="2" width="60" height="60"/>
      <active color="browser_iconbuttonactive" border="browser_iconbuttonoff" border_size="2" width="60" height="60"/>
      <menu shape="circle" color="textdarker" border="button_background2" border_size="7" width="32" height="32"/>
      <menuover shape="circle" color="green" border="button_background" border_size="7" width="32" height="32"/>
    </button>
    <fontsearch size="18"/>
    <font name="Arial" size="20"/>
    <fontheader size="16"/>
    <fontgridtitle size="18"/>
    <fonttoolbar size="14"/>"""


def pos_elements(x_attr, y_tail):
    """Yield all 112 <pos> lines for one define block (8 rack combos × 14 wavesizes)."""
    for rack_cond, y_rack, h_rack in RACK_COMBOS:
        for n in range(13, -1, -1):
            wavesize_y = 7 + n * 20       # 267 at n=13, 7 at n=0
            height_base = 121 + n * 20    # 381 at n=13, 121 at n=0

            y = f"+[HEIGHT]+{wavesize_y}-432{y_rack}{y_tail}"
            height = f"+[HEIGHT]-{height_base}{h_rack}"

            if rack_cond:
                condition = f"{rack_cond} ? var_equal '@$infntywavesize' {n}"
            else:
                condition = f"var_equal '@$infntywavesize' {n}"

            yield (
                f'    <pos {x_attr}y="{y}" width="1920"'
                f' height="{height}" condition="{condition}"/>'
            )


def generate():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        "<!-- Generated by scripts/gen-browser-positions.py — do not edit directly -->",
        "<defs>",
    ]

    for d in DEFINES:
        lines.append(
            f'  <define class="{d["cls"]}" showzoom="yes"'
            f' placeholders="*height" condition="{d["ubar_cond"]}">'
        )
        lines.extend(pos_elements(d["x_attr"], d["y_tail"]))
        lines.append(
            STATIC_CONTENT.format(
                bg_bordercolor=d["bg_bordercolor"],
                bg_bordersize=d["bg_bordersize"],
            )
        )
        lines.append("  </define>")

    lines.append("</defs>")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    OUTPUT.write_text(generate())
    print(f"Written {OUTPUT} ({OUTPUT.stat().st_size} bytes)")
