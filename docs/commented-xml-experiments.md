# Commented XML Experiments

Disabled XML removed from active skin files. Keep future experiments here or under `src/prototypes/` so production XML stays readable.

## VirtualDJ Conditions And Group Positioning

Reference summary: see
`../virtualdj-api-reference/Reference/Skin Runtime Findings.md` from the skin
repo root.

The reusable notes from the `TRACK_MODIFIERS_PANEL` mirror experiment were
promoted to the reference repo. Keep this file for GraveRaver-specific retired
XML snippets rather than broadly applicable VirtualDJ runtime behavior.

## src/components/buttons/base.xml

Original line 18:

```xml
<visual type="color" source="cue_color [SOURCE]" visibility="cue_color [SOURCE]">
<tooltip/>
<pos x="+0" y="+[HEIGHT]-3"/>
<size width="[WIDTH]" height="3"/>
</visual>
<button class="button_main" width="[WIDTH]" height="[HEIGHT]" action="hot_cue [SOURCE]" rightclick="delete_cue [SOURCE]" query="get_cue &amp; param_equal [SOURCE]" coloroff="transparent" coloron="transparent" brcoloroff="transparent" brcoloron="transparent" bordersize="0" textaction="get_text '[SOURCE]'" textheight="[HEIGHT]-3" textcolor="textoff2" textcoloron="needle"/>
```

Original line 50:

```xml
<action rgclick="[RIGHTCLICK]"/>
```

## src/components/buttons/hotcues.xml

Original line 39:

```xml
panel number
<button class="button_main" width="28" height="26" action="hot_cue [SOURCE]" rightclick="cue_name [SOURCE]" text="[SOURCE]" textcoloron="needle" textsize="13" coloroff="transparent" coloron="transparent" brcoloroff="transparent" brcoloron="transparent"/>
text
```

Original line 45:

```xml
delete
<button class="button_main" x="+28+191" width="28" height="26" action="delete_cue [SOURCE]" query="on/off" text="X" textsize="12"/>
button color
<visual type="color" source="cue_color [SOURCE]" visibility="cue_color [SOURCE]">
<tooltip></tooltip>
<pos x="+0" y="+0"/>
<size width="3" height="26"/>
</visual>
```

## src/components/buttons/menus.xml

Original line 11:

```xml
<separator visibility="var_equal '@$skin_mode' 2 ? false : var_equal '@$skin_mode' 0 ? false : true"/>
```

Original line 17:

```xml
<separator visibility="var_equal '@$skin_mode' 2 : false"/>
```

Original line 21:

```xml
<separator visibility="var_equal '@$skin_mode' 2"/>
```

Original line 42:

```xml
<separator visibility="setting 'skinOverviewType' 'shapes' ? true : setting 'skinOverviewType' 'auto' ? setting 'skinWaveformType' 'shapes' ? true : false"/>
```

Original line 48:

```xml
<separator/>
```

Original line 60:

```xml
<separator/>
```

Original line 69:

```xml
<separator/>
```

Original line 78:

```xml
<separator/>
```

Original line 97:

```xml
<separator visibility="not var_equal '@$skin_mode' 3"/>
```

## src/components/buttons/pads.xml

Original line 185:

```xml
PUSHED
<visual type="color" source="pad_button_color [SOURCE]" visibility="pad_pushed [SOURCE]">
<size width="124" height="38"/>
</visual>
```

Original line 194:

```xml
main button
<visual y="+0" width="124" height="38">
<off shape="square" color="red"/>
</visual>
```

Original line 201:

```xml
<over color="button_background2" border="#444444" border_size="1" shape="square"/>
```

Original line 270:

```xml
<visual>
<size width="180" height="39"/>
<up color="#666666" shape="square"/>
</visual>
border, undercoat
```

Original line 293:

```xml
<button action="pad [SOURCE]" rightclick="padshift [SOURCE]" visibility="pad_has_action [SOURCE]">
<size width="180" height="39"/>
<off color="#EE000000" border="#44444444" border_size="3" shape="square" radius="3"/>
<over color="#44000000" border="#44444444" border_size="3" shape="square" radius="3"/>
<down color="#44000000" border="#44555555" border_size="3" shape="square" radius="3"/>
<selected color="#AA000000" border="#88888888" border_size="3" shape="square" radius="3"/>
<text dx="+24" width="180-10-10" size="15" weight="" color="white" colorover="white" colordown="white" colorselected="white" action="pad [SOURCE]" align="left" multiline="true"/>
</button>
<button action="pad [SOURCE]" rightclick="padshift [SOURCE]" visibility="pad_has_action [SOURCE] ? constant 0.5 : constant 0:0">
<size width="180" height="39"/>
<off color="#EE000000" border="#444444" border_size="3" shape="square" radius="3"/>
<over color="#44000000" border="#444444" border_size="3" shape="square" radius="3"/>
<down color="#44000000" border="#555555" border_size="3" shape="square" radius="3"/>
<selected color="#AA000000" border="#888888" border_size="3" shape="square" radius="3"/>
</button>
color chip (pushed state)
```

Original line 345:

```xml
PUSHED
<visual type="color" source="pad_button_color [SOURCE]" visibility="pad_pushed [SOURCE]">
<size width="124" height="38"/>
</visual>
```

Original line 354:

```xml
main button
<visual y="+0" width="124" height="38">
<off shape="square" color="red"/>
</visual>
```

Original line 361:

```xml
<over color="button_background2" border="#444444" border_size="1" shape="square"/>
```

Original line 386:

```xml
background
<visual>
<tooltip></tooltip>
<size width="71" height="55"/>
<up color="button_background2" shape="square"/>
</visual>
border
<visual type="color" source="pad_button_color [SOURCE]" visibility="pad [SOURCE] ? constant 1 : constant 0.0">
<tooltip></tooltip>
<size width="71" height="55"/>
</visual>
background
```

Original line 425:

```xml
<visual visibility="pad_pushed [SOURCE]">
<tooltip></tooltip>
<pos x="+6" y="+55-12"/>
<size width="71-12" height="4"/>
<off color="needle" shape="square"/>
</visual>
```

Original line 434:

```xml
background
<visual>
<tooltip/>
<size width="80" height="32"/>
<up color="#333333" shape="square"/>
</visual>
color background
<visual type="color" source="pad_button_color [SOURCE]" visibility="pad [SOURCE] ? constant 1 : constant 0.5">
<tooltip/>
<size width="78" height="30"/>
</visual>
black background
```

Original line 455:

```xml
<up color="button_background2" border="black" border_size="1" shape="square"/>
```

## src/components/control-groups.xml

Original line 8:

```xml
borders
<visual class="gfx_shape" width="40" height="35" coloroff="infos_background" bordercoloroff="panel_background" bordersize="1"/>
<visual class="gfx_shape" width="40" height="432-56-1" coloroff="infos_background" bordercoloroff="panel_background" bordersize="2" visibility="var_equal '@$hide_crossfader' 0 ? var_not_equal '@$layout_4deck' 1"/>
<visual class="gfx_shape" width="40" height="432-56-1+216+2" coloroff="infos_background" bordercoloroff="panel_background" bordersize="2" visibility="var_equal '@$hide_crossfader' 0 ? var_equal '@$layout_4deck' 1"/>
<visual class="gfx_shape" width="40" height="432-56-1+57" coloroff="infos_background" bordercoloroff="panel_background" bordersize="2" visibility="var_equal '@$hide_crossfader' 1 ? var_not_equal '@$layout_4deck' 1"/>
<visual class="gfx_shape" width="40" height="432-56-1+216+2+57" coloroff="infos_background" bordercoloroff="panel_background" bordersize="2" visibility="var_equal '@$hide_crossfader' 1 ? var_equal '@$layout_4deck' 1"/>
```

Original line 38:

```xml
<item text="Wave Gray On Kill" action="setting 'waveGrayOnKill'" check="setting 'waveGrayOnKill'" visibility="setting 'skinwaveformScratchType' 'shapes'"/>
```

Original line 42:

```xml
VU: LEFT
<panel name="vdeck1" visibility="not deck 3 leftdeck">
<deck deck="1">
<panel class="vvu_meter_LEDs" x="+7" y="+60" ledh="8" gap="10" source="get_level" showpeaks="var_equal '@$show_peak_meter' 1"/>
</deck>
</panel>
<panel name="vdeck3" visibility="deck 3 leftdeck">
<deck deck="3">
<panel class="vvu_meter_LEDs" x="+7" y="+60" ledh="8" gap="10" source="get_level" showpeaks="var_equal '@$show_peak_meter' 1"/>
</deck>
</panel>
VU: RIGHT
<panel name="vdeck2" visibility="not deck 4 rightdeck">
<deck deck="2">
<panel class="vvu_meter_LEDs" x="+7+11+4" ledh="8" gap="10" y="+60" source="get_level" showpeaks="var_equal '@$show_peak_meter' 1"/>
</deck>
</panel>
<panel name="vdeck4" visibility="deck 4 rightdeck">
<deck deck="4">
<panel class="vvu_meter_LEDs" x="+7+11+4" y="+60" ledh="8" gap="10" source="get_level" showpeaks="var_equal '@$show_peak_meter' 1"/>
</deck>
</panel>
<slider action="zoom_vertical" dblclick="zoom_vertical 28%" orientation="vertical" frommiddle="false" visibility="var_equal '@$hide_crossfader' 0 ? constant 0.8">
<pos x="+10" y="+200"/>
<size width="20" height="120+216+2" condition="var_equal '@$layout_4deck' 1"/>
<size width="20" height="120"/>
<off color="xf_background" border="textdarker" shape="square"/>
<on color="xf_background" border="textdarker" shape="square"/>
<fader color="needle" width="18" height="7"/>
</slider>
<slider action="zoom_vertical" dblclick="zoom_vertical 28%" orientation="vertical" frommiddle="false" visibility="var_equal '@$hide_crossfader' 1 ? constant 0.8">
<pos x="+10" y="+200"/>
<size width="20" height="120+216+2+57" condition="var_equal '@$layout_4deck' 1"/>
<size width="20" height="120+57"/>
<off color="xf_background" border="textdarker" shape="square"/>
<on color="xf_background" border="textdarker" shape="square"/>
<fader color="needle" width="18" height="7"/>
</slider>
<button class="button_main" x="+6" y="+338" width="40-6-6" height="26" action="swap_decks" coloron="button_background" weight="bold" textcoloron="needle" text="> <" textsize="15" visibility="var_equal '@$hide_crossfader' 0 ? var_not_equal '@$layout_4deck' 1"/>
<button class="button_main" x="+6" y="+338+216+2" width="40-6-6" height="26" action="swap_decks" coloron="button_background" weight="bold" textcoloron="needle" text="> <" textsize="15" visibility="var_equal '@$hide_crossfader' 0 ? var_equal '@$layout_4deck' 1"/>
<button class="button_main" x="+6" y="+338+57" width="40-6-6" height="26" action="swap_decks" coloron="button_background" weight="bold" textcoloron="needle" text="> <" textsize="15" visibility="var_equal '@$hide_crossfader' 1 ? var_not_equal '@$layout_4deck' 1"/>
<button class="button_main" x="+6" y="+338+216+2+57" width="40-6-6" height="26" action="swap_decks" coloron="button_background" weight="bold" textcoloron="needle" text="> <" textsize="15" visibility="var_equal '@$hide_crossfader' 1 ? var_equal '@$layout_4deck' 1"/>
```

Original line 90:

```xml
<panel class="knob" x="+18" y="+14" knobsize="41" knobradius="10" faderradius="9" action="mic_volume" rgclick="mic_volume 62% while_pressed" dblclick="mic_volume 62%" frommiddle="false" fillcolor="br_focus" text="MIC VOL"/>
<button class="button_main" x="+10" y="+74" width="77-10-10" height="26" action="mic" textsize="11" text="ON" coloron="br_focus" bordersize="0"/>
<button class="button_main" x="+10" y="+74+24+12" width="77-10-10" height="26" action="sampler_rec 'mic'" textsize="11" text="REC" coloron="br_focus" bordersize="0"/>
<button class="button_main" x="+10" y="+74+24+12+24+12" width="77-10-10" height="26" radius="4" action="mic_talkover while_pressed" rightclick="mic_talkover" tooltip="Mic Talk-Over (while pressed)\nRight-click: Mic Talk-Over (ON-OFF)" textsize="11" textaction="get_text 'TALK'" coloroff="button_background2" coloron="#ff1467" bordersize="0"/>
<visual class="gfx_shape" y="+240" width="77" height="2" coloroff="skin_background"/>
<panel class="knob" x="+18" y="+236+2+14" knobsize="41" knobradius="10" faderradius="9" action="headphone_volume" rgclick="headphone_volume 50% while_pressed" dblclick="mic_volume 50%" frommiddle="false" fillcolor="br_focus" text="CUE VOL"/>
<panel class="knob" x="+18" y="+236+2+14+60" knobsize="41" knobradius="10" faderradius="9" action="headphone_mix" rgclick="headphone_mix 0% while_pressed" dblclick="headphone_mix 0%" frommiddle="false" fillcolor="br_focus" text="CUE MIX"/>
<visual class="gfx_shape" x="+77/2-10" y="+66-8+122+2" width="21" height="50" coloroff="xf_background"/>
```

## src/components/deck-info.xml

Original line 25:

```xml
INSTRUMENTAL LABEL
<group visibility="stem_pad 'instrumental'">
<pos x="+0" y="+36"/>
<visual visibility="0.8">
<size width="175" height="30"/>
<off shape="square" color="black"/>
</visual>
<visual visibility="0.2">
<pos x="+8" y="+6"/>
<size width="155" height="20"/>
<off shape="square" color="color_instrumental"/>
</visual>
<button action="stem_pad 'instrumental'" border_size="1">
<pos x="+8" y="+6"/>
<size width="155" height="20"/>
<off color="#222222" border="#444444" radius="3"/>
<down color="#222222" border="color_instrumental" radius="3"/>
<selected color="transparent" border="color_instrumental" radius="3"/>
<text fontsize="12" color="#555555" colorselected="color_instrumental" colordown="color_instrumental" align="center" text="INSTRUMENTAL"/>
</button>
</group>
```

Original line 124:

```xml
<group name="phrase_bars">
<button class="button_main" x="+0" y="+0" width="34" height="7" shape="square" query="get_phrase_num 1" coloroff="#222222" brcoloron="infos_background" brcoloroff="infos_background" bordersize="3"/>
<button class="button_main" x="+38" y="+0" width="34" height="7" shape="square" query="get_phrase_num 2" coloroff="#222222" brcoloron="infos_background" brcoloroff="infos_background" bordersize="3"/>
<button class="button_main" x="+38*2" y="+0" width="34" height="7" shape="square" query="get_phrase_num 3" coloroff="#222222" brcoloron="infos_background" brcoloroff="infos_background" bordersize="3"/>
<button class="button_main" x="+38*3" y="+0" width="34" height="7" shape="square" query="get_phrase_num 4" coloroff="#222222" brcoloron="infos_background" brcoloroff="infos_background" bordersize="3"/>
<button class="button_main" x="+0" y="+0" width="34" height="7" shape="square" query="goto_bar 1" coloroff="transparent" brcoloroff="transparent"/>
<button class="button_main" x="+38" y="+0" width="34" height="7" shape="square" query="goto_bar 2" coloroff="transparent" brcoloroff="transparent"/>
<button class="button_main" x="+38*2" y="+0" width="34" height="7" shape="square" query="goto_bar 3" coloroff="transparent" brcoloroff="transparent"/>
<button class="button_main" x="+38*3" y="+0" width="34" height="7" shape="square" query="goto_bar 4" coloroff="transparent" brcoloroff="transparent"/>
</group>
WATCHOS STYLE PHRASE TIMER
<group name="phrase_bars">
<button class="button_main" x="+0" y="+0" width="34" height="10" shape="square" query="goto_bar 1" coloroff="infos_background" brcoloron="infos_background" brcoloroff="infos_background" bordersize="0"/>
<button class="button_main" x="+38" y="+0" width="34" height="10" shape="square" query="goto_bar 2" coloroff="infos_background" brcoloron="infos_background" brcoloroff="infos_background" bordersize="0"/>
<button class="button_main" x="+38*2" y="+0" width="34" height="10" shape="square" query="goto_bar 3" coloroff="infos_background" brcoloron="infos_background" brcoloroff="infos_background" bordersize="0"/>
<button class="button_main" x="+38*3" y="+0" width="34" height="10" shape="square" query="goto_bar 4" coloroff="infos_background" brcoloron="infos_background" brcoloroff="infos_background" bordersize="0"/>
<panel class="phrase_circle" x="-48" y="-2" visibility="leftdeck"/>
<panel class="phrase_circle" x="+126+41" y="-16-2" visibility="rightdeck"/>
</group>
```

Original line 153:

```xml
<visual class="gfx_shape" width="120" height="20" coloroff="xf_progressbackground" bordersize="0" visibility="loaded ? constant 0.8"/>
<textzone visibility="loaded">
<pos x="+10" y="-10"/>
<size width="120-20" height="20*2"/>
<text fontsize="16" weight="" color="needle" align="right" format="`get_bar`.`get_beat_num` bars"/>
</textzone>
```

Original line 163:

```xml
<visual class="gfx_shape" width="120" height="20" coloroff="xf_progressbackground" bordersize="0" visibility="loaded ? constant 0.8"/>
<textzone visibility="loaded">
<pos x="+10" y="-10"/>
<size width="120-20" height="20*2"/>
<text fontsize="16" weight="" color="needle" align="center" format="`get_bar`.`get_beat_num` bars"/>
</textzone>
```

## src/components/deck-widgets.xml

Original line 21:

```xml
LOOP SELECT
<group name="dark_buttons" condition="var_not_equal '@$color_scheme' 4">
<button class="button_main" x="+10" y="+6" width="58" height="24" action="loop_pad_page 1 ? loop_select 0.03125 &amp; loop : loop_pad_page 2 ? loop_select 0.0625 &amp; loop : loop_pad_page 3 ? loop_select 0.125 &amp; loop : loop_pad_page 4 ? loop_select 0.25 &amp; loop : loop_pad_page 5 ? loop_select 0.5 &amp; loop : loop_pad_page 6 ? loop_select 1 &amp; loop" textaction="loop_pad 1" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62" y="+6" width="58" height="24" action="loop_pad_page 1 ? loop_select 0.0625 &amp; loop : loop_pad_page 2 ? loop_select 0.125 &amp; loop : loop_pad_page 3 ? loop_select 0.25 &amp; loop : loop_pad_page 4 ? loop_select 0.5 &amp; loop : loop_pad_page 5 ? loop_select 1 &amp; loop : loop_pad_page 6 ? loop_select 2 &amp; loop" textaction="loop_pad 2" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62+62" y="+6" width="58" height="24" action="loop_pad_page 1 ? loop_select 0.125 &amp; loop : loop_pad_page 2 ? loop_select 0.25 &amp; loop : loop_pad_page 3 ? loop_select 0.5 &amp; loop : loop_pad_page 4 ? loop_select 1 &amp; loop : loop_pad_page 5 ? loop_select 2 &amp; loop : loop_pad_page 6 ? loop_select 4 &amp; loop" textaction="loop_pad 3" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62+62+62" y="+6" width="58" height="24" action="loop_pad_page 1 ? loop_select 0.25 &amp; loop : loop_pad_page 2 ? loop_select 0.5 &amp; loop : loop_pad_page 3 ? loop_select 1 &amp; loop : loop_pad_page 4 ? loop_select 2 &amp; loop : loop_pad_page 5 ? loop_select 4 &amp; loop : loop_pad_page 6 ? loop_select 8 &amp; loop" textaction="loop_pad 4" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10" y="+6+28" width="58" height="24" action="loop_pad_page 1 ? loop_select 0.5 &amp; loop : loop_pad_page 2 ? loop_select 1 &amp; loop : loop_pad_page 3 ? loop_select 2 &amp; loop : loop_pad_page 4 ? loop_select 4 &amp; loop : loop_pad_page 5 ? loop_select 8 &amp; loop : loop_pad_page 6 ? loop_select 16 &amp; loop" textaction="loop_pad 5" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62" y="+6+28" width="58" height="24" action="loop_pad_page 1 ? loop_select 1 &amp; loop : loop_pad_page 2 ? loop_select 2 &amp; loop : loop_pad_page 3 ? loop_select 4 &amp; loop : loop_pad_page 4 ? loop_select 8 &amp; loop : loop_pad_page 5 ? loop_select 16 &amp; loop : loop_pad_page 6 ? loop_select 32 &amp; loop" textaction="loop_pad 6" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62+62" y="+6+28" width="58" height="24" action="loop_pad_page 1 ? loop_select 2 &amp; loop : loop_pad_page 2 ? loop_select 4 &amp; loop : loop_pad_page 3 ? loop_select 8 &amp; loop : loop_pad_page 4 ? loop_select 16 &amp; loop : loop_pad_page 5 ? loop_select 32 &amp; loop : loop_pad_page 6 ? loop_select 64 &amp; loop" textaction="loop_pad 7" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62+62+62" y="+6+28" width="58" height="24" action="loop_pad_page 1 ? loop_select 4 &amp; loop : loop_pad_page 2 ? loop_select 8 &amp; loop : loop_pad_page 3 ? loop_select 16 &amp; loop : loop_pad_page 4 ? loop_select 32 &amp; loop : loop_pad_page 5 ? loop_select 64 &amp; loop : loop_pad_page 6 ? loop_select 128 &amp; loop" textaction="loop_pad 8" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" textcoloron="needle" textsize="14"/>
</group>
<group name="day_buttons" condition="var_equal '@$color_scheme' 4">
<button class="button_main" x="+10" y="+6" width="58" height="24" action="loop_pad_page 1 ? loop_select 0.03125 &amp; loop : loop_pad_page 2 ? loop_select 0.0625 &amp; loop : loop_pad_page 3 ? loop_select 0.125 &amp; loop : loop_pad_page 4 ? loop_select 0.25 &amp; loop : loop_pad_page 5 ? loop_select 0.5 &amp; loop : loop_pad_page 6 ? loop_select 1 &amp; loop" textaction="loop_pad 1" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" bordersize="2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62" y="+6" width="58" height="24" action="loop_pad_page 1 ? loop_select 0.0625 &amp; loop : loop_pad_page 2 ? loop_select 0.125 &amp; loop : loop_pad_page 3 ? loop_select 0.25 &amp; loop : loop_pad_page 4 ? loop_select 0.5 &amp; loop : loop_pad_page 5 ? loop_select 1 &amp; loop : loop_pad_page 6 ? loop_select 2 &amp; loop" textaction="loop_pad 2" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" bordersize="2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62+62" y="+6" width="58" height="24" action="loop_pad_page 1 ? loop_select 0.125 &amp; loop : loop_pad_page 2 ? loop_select 0.25 &amp; loop : loop_pad_page 3 ? loop_select 0.5 &amp; loop : loop_pad_page 4 ? loop_select 1 &amp; loop : loop_pad_page 5 ? loop_select 2 &amp; loop : loop_pad_page 6 ? loop_select 4 &amp; loop" textaction="loop_pad 3" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" bordersize="2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62+62+62" y="+6" width="58" height="24" action="loop_pad_page 1 ? loop_select 0.25 &amp; loop : loop_pad_page 2 ? loop_select 0.5 &amp; loop : loop_pad_page 3 ? loop_select 1 &amp; loop : loop_pad_page 4 ? loop_select 2 &amp; loop : loop_pad_page 5 ? loop_select 4 &amp; loop : loop_pad_page 6 ? loop_select 8 &amp; loop" textaction="loop_pad 4" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" bordersize="2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10" y="+6+28" width="58" height="24" action="loop_pad_page 1 ? loop_select 0.5 &amp; loop : loop_pad_page 2 ? loop_select 1 &amp; loop : loop_pad_page 3 ? loop_select 2 &amp; loop : loop_pad_page 4 ? loop_select 4 &amp; loop : loop_pad_page 5 ? loop_select 8 &amp; loop : loop_pad_page 6 ? loop_select 16 &amp; loop" textaction="loop_pad 5" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" bordersize="2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62" y="+6+28" width="58" height="24" action="loop_pad_page 1 ? loop_select 1 &amp; loop : loop_pad_page 2 ? loop_select 2 &amp; loop : loop_pad_page 3 ? loop_select 4 &amp; loop : loop_pad_page 4 ? loop_select 8 &amp; loop : loop_pad_page 5 ? loop_select 16 &amp; loop : loop_pad_page 6 ? loop_select 32 &amp; loop" textaction="loop_pad 6" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" bordersize="2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62+62" y="+6+28" width="58" height="24" action="loop_pad_page 1 ? loop_select 2 &amp; loop : loop_pad_page 2 ? loop_select 4 &amp; loop : loop_pad_page 3 ? loop_select 8 &amp; loop : loop_pad_page 4 ? loop_select 16 &amp; loop : loop_pad_page 5 ? loop_select 32 &amp; loop : loop_pad_page 6 ? loop_select 64 &amp; loop" textaction="loop_pad 7" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" bordersize="2" textcoloron="needle" textsize="14"/>
<button class="button_main" x="+10+62+62+62" y="+6+28" width="58" height="24" action="loop_pad_page 1 ? loop_select 4 &amp; loop : loop_pad_page 2 ? loop_select 8 &amp; loop : loop_pad_page 3 ? loop_select 16 &amp; loop : loop_pad_page 4 ? loop_select 32 &amp; loop : loop_pad_page 5 ? loop_select 64 &amp; loop : loop_pad_page 6 ? loop_select 128 &amp; loop" textaction="loop_pad 8" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" bordersize="2" textcoloron="needle" textsize="14"/>
</group>
LOOP ACTIVE
<button class="button_main" x="+10" y="+6" width="58" height="24" action="loop_pad 1" coloroff="button_background2" brcoloroff="button_background2" textaction="loop_pad 1" textsize="14" visibility="loop ? true : false"/>
<button class="button_main" x="+10+62" y="+6" width="58" height="24" action="loop_pad 2" coloroff="button_background2" brcoloroff="button_background2" textaction="loop_pad 2" textsize="14" visibility="loop ? true : false"/>
<button class="button_main" x="+10+62+62" y="+6" width="58" height="24" action="loop_pad 3" coloroff="button_background2" brcoloroff="button_background2" textaction="loop_pad 3" textsize="14" visibility="loop ? true : false"/>
<button class="button_main" x="+10+62+62+62" y="+6" width="58" height="24" action="loop_pad 4" coloroff="button_background2" brcoloroff="button_background2" textaction="loop_pad 4" textsize="14" visibility="loop ? true : false"/>
<button class="button_main" x="+10" y="+6+28" width="58" height="24" action="loop_pad 5" coloroff="button_background2" brcoloroff="button_background2" textaction="loop_pad 5" textsize="14" visibility="loop ? true : false"/>
<button class="button_main" x="+10+62" y="+6+28" width="58" height="24" action="loop_pad 6" coloroff="button_background2" brcoloroff="button_background2" textaction="loop_pad 6" textsize="14" visibility="loop ? true : false"/>
<button class="button_main" x="+10+62+62" y="+6+28" width="58" height="24" action="loop_pad 7" coloroff="button_background2" brcoloroff="button_background2" textaction="loop_pad 7" textsize="14" visibility="loop ? true : false"/>
<button class="button_main" x="+10+62+62+62" y="+6+28" width="58" height="24" action="loop_pad 8" coloroff="button_background2" brcoloroff="button_background2" textaction="loop_pad 8" textsize="14" visibility="loop ? true : false"/>
<button class="button_main" x="+10" y="+62" width="58+4+58" height="16" action="loop_pad_page -1" sysicon="arrowleft" iconsize="20" query="on/off" textcolor="textdarker" textcoloron="needle" coloroff="infos_background" coloron="infos_background" bordersize="0"/>
<button class="button_main" x="+10+62+62" y="+62" width="58+4+58" height="16" action="loop_pad_page +1" sysicon="arrowright" iconsize="20" query="on/off" textcolor="textdarker" textcoloron="needle" coloroff="infos_background" coloron="infos_background" bordersize="0"/>
<button class="button_main" x="+10" y="+6+88" width="50" height="30" action="loop_half" sysicon="chevronleft" iconsize="22"/>
<button class="button_main" x="+10+55" y="+6+88" width="134" height="30" action="reloop_exit" query="loop" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" bordersize="1" textsize="12" textcoloron="needle" textaction="get_text 'RELOOP/EXIT'" condition="var_not_equal '@$color_scheme' 4"/>
<button class="button_main" x="+10+55" y="+6+88" width="134" height="30" action="reloop_exit" query="loop" coloroff="button_background2" coloron="button_background2" brcoloroff="button_background2" bordersize="2" textsize="12" textcoloron="needle" textaction="get_text 'RELOOP/EXIT'" condition="var_equal '@$color_scheme' 4"/>
<button class="button_main" x="+10+55+134+5" y="+6+88" width="50" height="30" action="loop_double" sysicon="chevronright" iconsize="22"/>
```

## src/components/display.xml

Original line 16:

```xml
<button class="button_main" x="+0" y="+0" width="110-20" height="17" action="auto_match_bpm" coloroff="infos_background" coloron="infos_background" brcoloroff="infos_background" brcoloron="infos_background" textsize="10" textcolor="textoff3" textcoloron="needle" text="A. MATCH BPM"/>
<button class="button_main" x="+114+8-20" y="+0" width="110-20" height="17" action="auto_match_key" coloroff="infos_background" coloron="infos_background" brcoloroff="infos_background" brcoloron="infos_background" textsize="10" textcolor="textoff3" textcoloron="needle" text="A. MATCH KEY"/>
<button class="button_main" x="+114+114+16-20-20" y="+0" width="90-20" height="17" action="auto_sync" coloroff="infos_background" coloron="infos_background" brcoloroff="infos_background" brcoloron="infos_background" textsize="10" textcolor="textoff3" textcoloron="needle" text="A. SYNC"/>
<button class="button_main" x="+114+94+114+24-20-20-20" y="+0" width="120-20" height="17" action="auto_pitch_lock" coloroff="infos_background" coloron="infos_background" brcoloroff="infos_background" brcoloron="infos_background" textsize="10" textcolor="textoff3" textcoloron="needle" text="A. PITCH LOCK"/>
```

Original line 22:

```xml
<button class="button_main" x="+0" y="+10" width="50" height="22" action="sync" coloroff="button_background" text="SYNC" textcolor="white" iconsize="20" sysicon="" border="0"/>
<button class="button_main" x="+50+4" y="+10" width="50" height="22" action="play_button" coloroff="button_background" textcolor="white" iconsize="20" sysicon="arrowright" border="0"/>
```

Original line 26:

```xml
<visual class="gfx_shape" width="128" height="80" coloroff="transparent"/>
KEY TEXT
```

Original line 35:

```xml
KEY MISMATCH WARNING
<visual type="square" x="+10" y="+40" width="10" height="10" color="red" visibility="not is_sync ? blink : false"/>
```

Original line 43:

```xml
<textzone class="text"
x="+26" y="+40"
width="128-26-26" height="20"
fontsize="12" align="center" weight=""
color="#999999"
textaction="get_key_modifier_text"/>
<button class="button_main" action="key_match_button" width="128-26-26" height="16" x="+26"
y="+5" coloroff="button_background" bordersize="0" textsize="12" textcolor="textdarker"
textcoloron="black" textaction="get_text 'SYNC'" visibility="not is_sync ? blink : false" />
loaded ? key 0
```

Original line 55:

```xml
<button class="button_main" x="+10" y="+50" width="72-20" height="20" action="master_tempo" coloroff="button_background" textcolor="textoff4" text="MT"/>
<textzone class="text" x="+72-10" y="+50" width="56" height="20" fontsize="13" color="textdarker" align="center" weight="" text="KEY"/>
```

Original line 63:

```xml
<button class="button_main" x="+56+10" y="+50" width="72-20" height="20" action="master_tempo" coloroff="button_background" textcolor="textoff4" text="MT"/>
<textzone class="text" x="+10" y="+50" width="56" height="20" fontsize="13" color="textdarker" align="center" weight="" text="KEY"/>
```

Original line 67:

```xml
<visual class="gfx_shape" width="196" height="40" coloroff="transparent"/>
<button class="button_main" x="+0" y="+8" width="196-73" height="24" action="beat_tap" dblclick="reanalyze" rightclick="edit_bpm" coloroff="transparent" coloron="transparent" bordersize="0" textcolor="textdarker" textsize="20" textaction="not loaded ? get_text 'TAP'" tooltip="Beat Tap \nRight-click: Edit BPM \nDouble-click: Reanalyze"/>
<textzone class="text" x="+0" y="+10" width="196-73" height="20" fontsize="18" color="deckcolor" align="center" weight="" textaction="var_equal '@$jog_bpm_digits' 0 ? get_text '%bpm' : var_equal '@$jog_bpm_digits' 1 ? get_text '%bpmex'" visibility="not var_equal '@$jog_type' 0 ? var_equal '@$deck_stack' 1 ? var_equal '@deck_mode' 0 : false"/>
<textzone class="text" x="+0" y="+10" width="196-73" height="20" fontsize="18" color="needle" align="center" weight="" textaction="var_equal '@$jog_bpm_digits' 0 ? get_text '%Pbpm' : var_equal '@$jog_bpm_digits' 1 ? get_text '%Pbpmex'" novisibility="not var_equal '@$jog_type' 0 ? var_equal '@$deck_stack' 1 ? var_equal '@deck_mode' 0 : false"/>
<button class="button_main" x="+196-105" y="+11" width="60" height="20" action="masterdeck" coloroff="button_background" coloron="orange" brcoloron="orange" textcoloron="black" textcolor="textoff4" textsize="10" text="MASTER"/>
<textzone class="text" x="+154" y="+8" action="pitch_reset" width="80" height="24" fontsize="20" color="textoff2" align="center" weight="" textaction="get_text '%Ppitch%'" visibility="not var_equal '@$deck_stack' 1"/>
```

Original line 80:

```xml
<button class="button_main" x="+56" y="+50" width="80" height="20" action="masterdeck" coloroff="button_background" textcolor="textoff4" text="MASTER" visibility="var_equal '@$jog_type' 0"/>
```

Original line 86:

```xml
<button class="button_main" x="+56" y="+50" width="80" height="20" action="masterdeck" coloroff="button_background" textcolor="textoff4" text="MASTER"/>
```

## src/components/effects.xml

Original line 72:

```xml
<panel class="knob" x="+104+28+8+15" y="+10" knobsize="22" knobradius="10" faderradius="5" action="effect_slider [SOURCE] 1" frommiddle="false" fillcolor="knobfilloff" novisibility="effect_active [SOURCE]"/>
<panel class="knob" x="+104+28+8+15" y="+10" knobsize="22" knobradius="10" faderradius="5" action="effect_slider [SOURCE] 1" frommiddle="false" fillcolor="knobfillon" visibility="effect_active [SOURCE]"/>
<panel class="knob" x="+104+28+8+28+25" y="+10" knobsize="22" knobradius="10" faderradius="5" action="effect_slider [SOURCE] 2" frommiddle="false" fillcolor="knobfilloff" novisibility="effect_active [SOURCE]"/>
<panel class="knob" x="+104+28+8+28+25" y="+10" knobsize="22" knobradius="10" faderradius="5" action="effect_slider [SOURCE] 2" frommiddle="false" fillcolor="knobfillon" visibility="effect_active [SOURCE]"/>
```

Original line 79:

```xml
<square x="+0" y="+0" width="[WIDTH]+28" height="36" color="black" />
```

Original line 82:

```xml
<panel class="knob" x="+104+28+8+15" y="+10" knobsize="22" knobradius="10" faderradius="5" action="effect_slider [SOURCE] 1" frommiddle="true" fillcolor="knobfilloff" novisibility="effect_active [SOURCE]"/>
<panel class="knob" x="+104+28+8+15" y="+10" knobsize="22" knobradius="10" faderradius="5" action="effect_slider [SOURCE] 1" frommiddle="false" fillcolor="knobfillon" visibility="effect_active [SOURCE]"/>
<panel class="knob" x="+104+28+8+28+25" y="+10" knobsize="22" knobradius="10" faderradius="5" action="effect_slider [SOURCE] 2" frommiddle="false" fillcolor="knobfilloff" novisibility="effect_active [SOURCE]"/>
<panel class="knob" x="+104+28+8+28+25" y="+10" knobsize="22" knobradius="10" faderradius="5" action="effect_slider [SOURCE] 2" frommiddle="false" fillcolor="knobfillon" visibility="effect_active [SOURCE]"/>
```

## src/components/jogwheel.xml

Original line 4:

```xml
<visual>
<size width="24" height="24"/>
<pos x="-2" y="-2"/>
<off shape="circle" color="#111111" border="#000000" border_size="1"/>
</visual>
```

Original line 143:

```xml
BPM % DIFF
<textzone>
<pos x="+0" y="-12"/>
<size width="+[JOGSIZE]" height="25"/>
<text fontsize="14" weight="" color="white" align="center" format="`get_text '%Ppitch%'`" important="true"/>
</textzone>
BPM % DIFF
```

Original line 156:

```xml
<button class="button_main" x="+18+6" y="+72" width="50" height="20" coloroff="transparent" coloron="#222222" bordersize="1" brcoloroff="dark_5" radius="5" textsize="16" border="red" textcolor="textoff2" textaction="get_key_modifier_text" action="key_match_button" visibility="loaded ? not key 0"/>
```

Original line 164:

```xml
<button class="button_main" action="key_match_button" width="50" height="16" x="+18+6" y="+72" coloroff="button_background" bordersize="0" textsize="12" textcolor="textdarker" text="KEY" visibility="loaded ? key 0"/>
center
left
<button class="button_main" x="+18+6" y="+72" width="50" height="20" coloroff="transparent" coloron="#222222" bordersize="1" brcoloroff="dark_5" radius="5" textsize="16" border="red" textcolor="textoff2" textaction="get_key_modifier_text" action="key_match_button" visibility="loaded ? not key 0"/>
right
<button class="button_main" x="+18+6+50" y="+72" width="50" height="16" coloroff="transparent" coloron="transparent" bordersize="1" textsize="14" textcolor="textoff2" textaction="get_text '±%Ppitchrange'" visibility="loaded"/>
```

Original line 197:

```xml
time elapsed
<textzone class="text" x="+18" y="+92" width="[JOGSIZE]-36" height="26" fontsize="18" color="texton2" align="center" weight="" textaction="get_time 'elapsed'" visibility="loaded ? var_equal '@$jog_display_mode' 2"/>
<textzone class="text" x="+18" y="+92" width="[JOGSIZE]-36" height="26" fontsize="18" color="texton2" align="center" weight="" textaction="get_time 'remain'" visibility="loaded ? var_equal '@$jog_display_mode' 3"/>
```

Original line 261:

```xml
LABEL: BPM
<textzone>
<pos x="+0" y="+7"/>
<size width="[JOGSIZE]" height="25"/>
<text fontsize="8" weight="" color="white" align="center" text="BPM" important="true"/>
</textzone>
<line x="+6" y="+58" color="white" shadow="transparent" width="146"/>
```

Original line 269:

```xml
BPM-
<button class="button_main" x="+27" y="+42" width="26" height="16" action="pitch -1 bpm" textcoloron="white" coloron="transparent" coloroff="transparent" brcoloron="transparent" brcoloroff="transparent" iconsize="15" sysicon="minus"/>
BPM+
<button class="button_main" x="+102" y="+42" width="26" height="16" action="pitch +1 bpm" textcoloron="white" coloron="transparent" coloroff="transparent" brcoloron="transparent" brcoloroff="transparent" iconsize="15" sysicon="plus"/>
PRO: JOGWHEEL: KEY BEAT PHRASE INDICATORS
```

Original line 294:

```xml
KEY MISMATCH WARNING
<visual type="square" x="+10" y="+40" width="10" height="10" color="red" visibility="not is_sync ? blink : false"/>
```

Original line 302:

```xml
<visual >
<tooltip/>
<pos x="+0" y="+0"/>
<size width="[JOGSIZE]" height="[JOGSIZE]"/>
<off shape="circle" color="deckcolor" border="jogprogressoff"/>
</visual>
<visual x="-1" y="-1" tooltip="">
<size width="[JOGSIZE]" height="[JOGSIZE]"/>
<off border_size="2" border="transparent" color="orange" shape="circle"/>
<on border_size="7" border="jogprogressoff" color="orange" shape="circle"/>
</visual>
<visual name="outerborder" x="+0" y="+0" source="true">
<size width="[JOGSIZE]" height="[JOGSIZE]"/>
<off border_size="2" border="transparent" color="mixerbackground" shape="circle"/>
<on  border_size="7"
border="orange"
color="mixerbackground"
shape="circle"/>
</visual>
```

Original line 326:

```xml
<visual name="outerborder" x="+0" y="+0" source="true">
<size width="[JOGSIZE]" height="[JOGSIZE]"/>
<off border_size="2" border="transparent" color="mixerbackground" shape="circle"/>
<on  border_size="7"
border="orange"
color="mixerbackground"
shape="circle"/>
</visual>
```

Original line 349:

```xml
overlay: orange border only when THIS deck is the master/sync master
<visual name="outerborder_master" x="+0" y="+0"
visibility="param_equal 'get_deck' 'get_activedeck'">
<size width="[JOGSIZE]" height="[JOGSIZE]"/>
draw only a border (transparent fill)
<off border_size="7" border="orange" color="transparent" shape="circle"/>
</visual>
```

Original line 366:

```xml
<visual visibility="loaded ? constant 0.8 : constant 0.0">
<tooltip/>
<pos x="+20" y="+54"/>
<size width="[JOGSIZE]-40" height="[JOGSIZE]-56-56"/>
<off shape="square" color="jogprogressoff" border="jogprogressoff" radius="6"/>
<textzone class="text" x="+18" y="+50" width="[JOGSIZE]-36" height="46" fontsize="26" color="needle" align="center" weight="bold" textaction="var_equal '@$bpm_hide_options' 1 ? get_text '==.==' : var_equal '@$jog_bpm_digits' 0 ? get_text '%Pbpm' : var_equal '@$jog_bpm_digits' 1 ? get_text '%Pbpmex'"/>
</visual>
```

Original line 375:

```xml
<scratch>
<pos width="[JOGSIZE]" height="[JOGSIZE]"/>
<mousecircle width="[JOGSIZE]" height="[JOGSIZE]"/>
</scratch>
```

## src/components/loop-panels.xml

Original line 361:

```xml
<visual width="280" height="215">
<off shape="square" color="#090909"/>
</visual>
```

## src/components/pitch.xml

Original line 34:

```xml
<line color="faderlines" x="+0" y="+0" width="38" height="1"/>
<line color="faderlines" x="+2" y="+13" width="34" height="1"/>
<line color="faderlines" x="+2" y="+13*2" width="34" height="1"/>
<line color="faderlines" x="+2" y="+13*3" width="34" height="1"/>
<line color="faderlines" x="+0" y="+13*4" width="38" height="1"/>
<line color="faderlines" x="+2" y="+13*5" width="34" height="1"/>
<line color="faderlines" x="+2" y="+13*6" width="34" height="1"/>
<line color="faderlines" x="+2" y="+13*7" width="34" height="1"/>
<line color="faderlines" x="+0" y="+13*8" width="38" height="1"/>
```

Original line 50:

```xml
<slider action="pitch" rightclick="pitch_zero" dblclick="pitch_reset" orientation="vertical" direction="down" frommiddle="true">
<pos x="+0" y="-7+6"/>
<size width="38" height="[HEIGHT]"/>
<fader color="faderbackgroundline" width="38" height="2"/>
</slider>
<button x="-7" y="+[HEIGHT]" width="52" height="16" action="beatlock" query="beatlock">
<off color="button_background3" border="button_background3" border_size="1" radius="5"/>
<on color="button_background3" border="white" border_size="1" radius="5"/>
<over color="button_background3" border="button_background3" border_size="1" radius="5"/>
<down color="button_background3" border="white" border_size="1" radius="5"/>
<text dy="-1" text="BEATLOCK" fontsize="8" coloroff="dark_8" coloron="needle" align="center"/>
</button>
```

Original line 129:

```xml
<line color="faderlines" x="+0" y="+0" width="38" height="1"/>
```

Original line 139:

```xml
<line color="faderlines" x="+0" y="+12*10" width="38" height="1"/>
```

Original line 142:

```xml
BLACK STRIP
<visual width="10" height="123">
<pos x="+0" y="+0"/>
<off shape="square" color="black" radius="3"/>
</visual>
LEVEL
```

Original line 206:

```xml
<button class="button_main" x="-5" y="+0" width="38" height="38" action="auto_crossfade 0%" rightclick="crossfader 0%" tooltip="Auto-Crossfader Left\nRight-click: Crossfader 0%" coloroff="transparent" coloron="transparent" brcoloroff="transparent" brcoloron="transparent" textsize="10" textcolor="textoff3" textcoloron="needle" iconsize="30" sysicon="arrowleft" query="crossfader 0%" visibility="var_equal '@$4decks' 0"/>
<button class="button_main" x="+240" y="+0" width="38" height="38" action="auto_crossfade 100%" rightclick="crossfader 100%" tooltip="Auto-Crossfader Right\nRight-click: Crossfader 100%"coloroff="transparent" coloron="transparent" brcoloroff="transparent" brcoloron="transparent" textsize="10" textcolor="textoff3" textcoloron="needle" iconsize="30" sysicon="arrowright" query="crossfader 100%" visibility="var_equal '@$4decks' 0"/>
<group name="channel_assign" x="-10" visibility="var_not_equal '@$4decks' 0">
<button class="button_main" x="+0" y="+0" width="18" height="18" action="deck 1 leftcross" text="1" coloron="waveform_active1" bordersize="0"/>
<button class="button_main" x="+20" y="+0" width="18" height="18" action="deck 2 leftcross" text="2" coloron="waveform_active2" bordersize="0"/>
<button class="button_main" x="+0" y="+20" width="18" height="18" action="deck 3 leftcross" text="3" coloron="waveform_active3" bordersize="0"/>
<button class="button_main" x="+20" y="+20" width="18" height="18" action="deck 4 leftcross" text="4" coloron="waveform_active4" bordersize="0"/>
</group>
<group name="channel_assign" x="+244" visibility="var_not_equal '@$4decks' 0">
<button class="button_main" x="+0" y="+0" width="18" height="18" action="deck 1 rightcross" text="1" coloron="waveform_active1" bordersize="0"/>
<button class="button_main" x="+20" y="+0" width="18" height="18" action="deck 2 rightcross" text="2" coloron="waveform_active2" bordersize="0"/>
<button class="button_main" x="+0" y="+20" width="18" height="18" action="deck 3 rightcross" text="3" coloron="waveform_active3" bordersize="0"/>
<button class="button_main" x="+20" y="+20" width="18" height="18" action="deck 4 rightcross" text="4" coloron="waveform_active4" bordersize="0"/>
</group>
<line color="faderlines" x="960-18-18-18-18-18" y="+0" width="1" height="38" />
<line color="faderlines" x="960-18-18-18-18" y="+2" width="1" height="34" />
<line color="faderlines" x="960-18-18-18" y="+2" width="1" height="34" />
<line color="faderlines" x="960-18-18" y="+2" width="1" height="34" />
<line color="faderlines" x="960-18" y="+2" width="1" height="34" />
<line color="faderlines" x="960" y="+0" width="1" height="38" />
<line color="faderlines" x="960+17" y="+2" width="1" height="34" />
<line color="faderlines" x="960+18+17" y="+2" width="1" height="34" />
<line color="faderlines" x="960+18+18+17" y="+2" width="1" height="34" />
<line color="faderlines" x="960+18+18+18+17" y="+2" width="1" height="34" />
<line color="faderlines" x="960+18+18+18+17+18" y="+0" width="1" height="38" />
<slider action="crossfader" rightclick="crossfader 50%" dblclick="crossfader 50%" orientation="horizontal" frommiddle="true">
<pos x="+30+9" y="+0"/>
<size width="194" height="38"/>
<off width="-4" height="-24" color="xf_progressbackground" border="xf_background" border_size="4" shape="square"/>
<on width="-4" height="-24" color="mastercoloron" border="xf_background" border_size="4" shape="square"/>
<fader color="faderbackground2" width="14" height="38"/>
</slider>
<slider action="crossfader" rightclick="crossfader 50%" dblclick="crossfader 50%" orientation="horizontal" frommiddle="true">
<pos x="+30+9+6" y="+0"/>
<size width="194-12" height="38"/>
<fader color="faderbackgroundline" width="2" height="38"/>
</slider>
```

Original line 304:

```xml
<visual class="gfx_shape" x="+0" y="+0" width="58" height="170" coloroff="#000000" bordercolor="#333333" border_size="2"/>
```

Original line 311:

```xml
PITCH RANGE
<button class="button_main" x="+0" y="+0" action="pitch_range '8,16,32,50' +1" rightclick="pitch_range '8,16,32,50' -1" tooltip="Pitch range +8,16,32,50.\nRigth-click: Pitch range -8,16,32,50." width="58" height="24" coloroff="button_background3" brcoloroff="button_background3" textsize="14" textcolor="textoff2" textaction="get_text '+-%pitchrange'"/>
SLIDER
```

Original line 318:

```xml
+ and -
<button class="button_main" x="+0" y="+6+30+4+30+6+62+12" width="29" height="18" action="pitch_bend -2% 500ms" rightclick="pitch_range '8,16,32,50' -1"  tooltip="Pitch Bend.\nRigth-click: Pitch range -8,16,32,50." textsize="14" text="-" visibility="var_not_equal '@$jog_type' 0"/>
<button class="button_main" x="+29" y="+6+30+4+30+6+62+12" width="29" height="18" action="pitch_bend +2% 500ms" rightclick="pitch_range '8,16,32,50' +1" tooltip="Pitch Bend.\nRigth-click: Pitch range +8,16,32,50." textsize="14" text="+" visibility="var_not_equal '@$jog_type' 0"/>
<button x="+0" y="+0" width="26" height="26" action="master_tempo on ? master_tempo off : master_tempo on" coloroff="cue_color [SOURCE]" textcolor="white">
<off color="cue_color [SOURCE]"/>
<over color="cue_color [SOURCE] ? constant 0.4"/>
<icon dx="+2" sysicon="arrowright" color="white" colordown="white" colorselected="white" width="25" height="25" />
<text size="8" dx="22" dy="2">PITCH LOCK</text>
</button>
Master Tempo (Pitch Lock) toggle button
<button class="button_main"
x="+5" y="+150" width="50" height="15"
visible="yes" available="yes"
action="master_tempo on ? master_tempo off : master_tempo on"
query="master_tempo"
text="PITCHLOCK"
textdx="22" textdy="2"
textsize="8" align="center"
textcolor="#CCCCCC" textcoloron="#FFFFFF"
coloroff="#444444" coloron="#444444"
brcoloroff="#000000" brcoloron="#FFFFFF"
>
lock vs. unlock icon
<icon width="16" height="16"
sysicon="lock" sysiconon="lock_open"
colordown="white" colorselected="white"
color="#CCCCCC" coloron="#00FF00"/>
<icon dx="+2" sysicon="lock" color="white" colordown="white" colorselected="white" width="25" height="25" />
</button>
PITCH SLIDER: PITCH LOCK BUTTON
<button class="button_main" x="+0" y="+150" width="60" height="16" action="master_tempo on ? master_tempo off : master_tempo on" query="master_tempo" textsize="8" text="PITCH LOCK" coloroff="button_background3" coloron="button_background3" bordersize="0" textcolor="textoff3" textcoloron="needle" query="slip_mode ? blink 800ms : off"/>
```

## src/components/sliders.xml

Original line 14:

```xml
VU METER
<visual source="get_level '[STEM]'" type="linear" orientation="horizontal" direction="up" granularity="[GRANULARITY]">
<pos x="+0" y="+[HEIGHT]+2"/>
<size width="[WIDTH]" height="7"/>
<off shape="square" border="#2A2A2A" color="black" radius="2"/>
<down shape="square" border="[COLOR]" color="[COLOR]" radius="2"/>
</visual>
GAIN SLIDER
<slider action="param_multiply 50% &amp; stem '[STEM]'" dblclick="stem '[STEM]' 50%" orientation="horizontal" direction="up" frommiddle="false">
<pos x="+0" y="+[HEIGHT]+2"/>
<size width="[WIDTH]" height="7"/>
<fader color="#AAAAAA" width="2" height="5"/>
</slider>
<visual source="get_level '[STEM]'" type="linear" orientation="vertical" direction="up" granularity="23">
<pos x="+0" y="+55"/>
<size width="40" height="4"/>
<off shape="square" color="#333333" radius="0"/>
<on shape="square" color="[COLOR]" radius="0"/>
</visual>
```

Original line 36:

```xml
<line color="faderlines" x="+0" y="+0" width="38" height="1"/>
```

Original line 46:

```xml
<line color="faderlines" x="+0" y="+12*10" width="38" height="1"/>
```

Original line 52:

```xml
BLACK STRIP
<visual width="10" height="123">
<pos x="+0" y="+0"/>
<off shape="square" color="black" radius="3"/>
</visual>
LEVEL
```

## src/components/track-info.xml

Original line 20:

```xml
left
<line visibility="stem_pad 'instrumental'" color="color_instrumental" x="+4" y="+0" width="526" height="2"/>
<line visibility="stem_pad 'acapella'" color="color_acapella" x="+4" y="+0" width="526" height="2"/>
```

Original line 63:

```xml
LINE 1: TITLE
<textzone tooltip="">
<size width="320" height="20"/>
<text fontsize="16" weight="bold" color="white" colorover="black" align="left" scroll="yes" action="deck loaded ? get_title_before_remix &amp; param_uppercase" localize="true" important="true"/>
</textzone>
```

Original line 85:

```xml
<textzone>
<pos y="+16"/>
<size width="260" height="70-6-6-26"/>
<text fontsize="12" color="#888888" align="left" scroll="yes" action="get_loaded_song 'artist' &amp; param_uppercase" localize="true" important="true"/>
</textzone>
SONG FILE INFO
```

Original line 160:

```xml
<group visibility="get_deck 1 ? true : get_deck 3 ? true : false">
```

Original line 163:

```xml
black bg spine
<visual x="+0" y="+1" width="34" height="320">
<off shape="square" color="black" radius="6"/>
</visual>
<menu class="menu_maindecks" query="select" x="+5" y="+295" width="28" height="20"/>
```

Original line 188:

```xml
highlight
<visual width="62" height="62" x="+0" y="+0">
<off shape="square" color="transparent" border_size="1" border="#44FFFFFF" radius="0"/>
</visual>
```

Original line 195:

```xml
<button class="button_main" x="+0" y="+4" width="90" height="34" action="beat_tap" dblclick="reanalyze" rightclick="edit_bpm" coloroff="transparent" coloron="transparent" bordersize="0" textcolor="textdarker" textsize="18" textaction="not loaded ? get_text 'TAP'" tooltip="Beat Tap \nRigth-click: Edit BPM \nDouble-click: Reanalyze"/>
```

Original line 199:

```xml
<button class="button_main" x="+878-10-90+77+2" y="+38-2" width="90" height="18" action="masterdeck" coloroff="button_background" textcolor="textoff4" text="MASTER"/>
<button class="button_main" x="+878-10-90-10-80-10-48+50-28+77+2" y="+15" width="20" height="22" action="key_move -1" coloroff="button_background" textcolor="textoff4" iconsize="16" sysicon="arrowleft"/>
<button class="button_main" x="+878-10-90-10-80-10-48+50+60+77+2" y="+15" width="20" height="22" action="key_move +1" coloroff="button_background" textcolor="textoff4" iconsize="16" sysicon="arrowright"/>
```

Original line 205:

```xml
<button class="button_main" x="+878-10-90-10-80-10-48+50+77+2" y="+38-2" width="54" height="18" action="master_tempo" coloroff="button_background" textcolor="textoff4" text="MT"/>
time
```

Original line 212:

```xml
RIGHT DECK
<group visibility="get_deck 2 ? true : get_deck 4 ? true : false">
not cover
<group x="+77+2" y="-2" visibility="var_equal '@$show_cover_title' 0">
<panel class="textzone_title_artist_combo" x="+2+354" y="+4" width="478" align="right" scroll="no" titlefontsize="18" artistfontsize="14" visibility="var_equal '@hntnhtxtscroll' 0"/>
<panel class="textzone_title_artist_combo" x="+2+354" y="+4" width="478" align="right" scroll="yes" titlefontsize="18" artistfontsize="14" visibility="var_equal '@hntnhtxtscroll' 1"/>
</group>
with cover
<group x="-5+77+2+5" y="-2" visibility="var_equal '@$show_cover_title' 1">
<panel class="textzone_title_artist_combo" x="+2+354" y="+4" width="478-50-8" align="right" scroll="no" titlefontsize="18" artistfontsize="14" artistcolor="#888888" visibility="var_equal '@hntnhtxtscroll' 0"/>
<panel class="textzone_title_artist_combo" x="+2+354" y="+4" width="478-50-8" align="right" scroll="yes" titlefontsize="20" artistfontsize="17" artistcolor="#888888" visibility="var_equal '@hntnhtxtscroll' 1"/>
</group>
PERFORMANCE: EXTENDED: RIGHT DECK: MODES
<button class="button_main" x="+10" y="+4" width="90" height="34" action="beat_tap" dblclick="reanalyze" rightclick="edit_bpm" coloroff="transparent" coloron="transparent" bordersize="0" textcolor="textdarker" textsize="18" textaction="not loaded ? get_text 'TAP'" tooltip="Beat Tap \nRigth-click: Edit BPM \nDouble-click: Reanalyze"/>
<textzone class="text" x="+10" y="+4" width="90" height="34" fontsize="22" color="needle" align="center" weight="bold" textaction="var_equal '@$jog_bpm_digits' 0 ? get_text '%Pbpm' : var_equal '@$jog_bpm_digits' 1 ? get_text '%Pbpmex'" visibility="var_equal '@$jog_type' 0"/>
<textzone class="text" x="+10" y="+4" width="90" height="34" fontsize="22" color="deckcolor" align="center" weight="bold" textaction="var_equal '@$jog_bpm_digits' 0 ? get_text '%bpm' : var_equal '@$jog_bpm_digits' 1 ? get_text '%bpmex'" visibility="not var_equal '@$jog_type' 0"/>
<button class="button_main" x="+10" y="+38-2" width="90" height="18" action="masterdeck" coloroff="button_background" textcolor="textoff4" text="MASTER"/>
<button class="button_main" x="+10+90+10+80+10-55-22" y="+10" width="20" height="22" action="key_move -1" coloroff="button_background" textcolor="textoff4" iconsize="16" sysicon="arrowleft"/>
<button class="button_main" x="+10+90+10+80+10-55+54" y="+10" width="20" height="22" action="key_move +1" coloroff="button_background" textcolor="textoff4" iconsize="16" sysicon="arrowright"/>
<textzone class="text" x="+10+90+10+80+10-55" y="+4" width="54" height="34" action="key_match_menu" fontsize="22" color="`get_key_color`" align="center" weight="bold" textaction="get_key"/>
<button class="button_main" x="+10+90+10+80+10-55" y="+38-2" width="54" height="18" action="master_tempo" coloroff="button_background" textcolor="textoff4" text="LOCK"/>
<textzone class="text" x="+10+90+10+80+10+48+10-20" y="+4" action="cycle '@$hauntinstimesdisplay' 3" tooltip="" width="80" height="24" fontsize="12" color="textdarker" align="center" weight="" textaction="var_equal '@$hauntinstimesdisplay' 0 ? get_text 'ELAPSED' : var_equal '@$hauntinstimesdisplay' 1 ? get_text 'REMAIN' : var_equal '@$hauntinstimesdisplay' 2 ? get_text 'TOTAL'"/>
<textzone class="text" x="+10+90+10+80+10+48+10-20" y="+4+24-2" action="cycle '@$hauntinstimesdisplay' 3" tooltip="" width="80" height="34" fontsize="20" color="needle" align="center" weight="" textaction="var_equal '@$hauntinstimesdisplay' 0 ? get_time 'ELAPSED' : var_equal '@$hauntinstimesdisplay' 1 ? get_time 'REMAIN' : var_equal '@$hauntinstimesdisplay' 2 ? get_time 'TOTAL'"/>
<textzone class="text" x="+10+90+10+80-55" y="+30" width="128-26-26" height="20" fontsize="12" align="center" weight="" color="#999999" textaction="get_key_modifier_text"/>
<panel class="cover_art_hntg" size="62-6-6" x="+878-2-4-28-56-6+77+2+6" y="+6" visibility="var_equal '@$show_cover_title' 1"/>
<button class="button_main" x="+878-2-4-28+77+2" y="+6" width="28" height="62-6-6" action="select" rightclick="cycle '@infospannelmode' 5" tooltip="Select Deck" coloroff="button_background" textheight="30" textsize="16" textaction="get_deck"/>
<menu class="menu_maindecks" query="select" x="+878-2-4-28+77+2" y="+64-8-22" width="28" height="20"/>
</group>
```

Original line 290:

```xml
<button class="button_main" x="+878-2-4-28-78" y="+6" width="28" height="68-6-6" action="select" rightclick="cycle '@infospannelmode' 5" tooltip="Select Deck" coloroff="button_background" textheight="30" textsize="16" textaction="get_deck"/>
```

Original line 385:

```xml
<dropzone visibility="var_equal '@$layout_4deck' 1" x="-2" y="-2">
<size width="770" height="236"/>
<over color="transparent" border_size="2" border="color_dropzone" shape="square" radius="10"/>
</dropzone>
```

Original line 390:

```xml
CLASS: STEM BUTTONS
<define class="_STEM_BUTTON" placeholders="*stem,*label,*color,width=65,height=23,fontsize=13,granularity=23">
TOGGLE
<button x="+0" action="stem_pad '[STEM]'" border_size="1">
<size width="[WIDTH]" height="[HEIGHT]"/>
<off color="#222222" border="#444444" radius="3"/>
<down color="#222222" border="[COLOR]" radius="3"/>
<selected color="transparent" border="[COLOR]" radius="3"/>
<text fontsize="[FONTSIZE]" color="#555555" colorover="[COLOR]" colorselected="[COLOR]" colordown="[COLOR]" align="center" text="[LABEL]"/>
</button>
VU METER
<visual source="get_level '[STEM]'" type="linear" orientation="horizontal" direction="up" granularity="[GRANULARITY]">
<pos x="+0" y="+[HEIGHT]+2"/>
<size width="[WIDTH]" height="7"/>
<off shape="square" border="#2A2A2A" color="black" radius="2"/>
<down shape="square" border="[COLOR]" color="[COLOR]" radius="2"/>
</visual>
GAIN SLIDER
<slider action="param_multiply 50% &amp; stem '[STEM]'" dblclick="stem '[STEM]' 50%" orientation="horizontal" direction="up" frommiddle="false">
<pos x="+0" y="+[HEIGHT]+2"/>
<size width="[WIDTH]" height="7"/>
<fader color="#AAAAAA" width="2" height="5"/>
</slider>
STEM FX
<button x="+0" y="+[HEIGHT]+12" action="stem_pad '[STEM]'" border_size="1">
<size width="[WIDTH]/3" height="[HEIGHT]*0.8"/>
<off color="#222222" border="#444444" radius="3"/>
<down color="#222222" border="[COLOR]" radius="3"/>
<selected color="transparent" border="[COLOR]" radius="3"/>
<text fontsize="[FONTSIZE]" color="#555555" colorselected="[COLOR]" colordown="[COLOR]" align="center" text="FX"/>
</button>
</define>
```

Original line 425:

```xml
TAGS
<group x="+235" y="+64">
<panel class="hashtag_stack" deck="1" x="+0" panelname="tags1" visibility="not deck 3 leftdeck"/>
<panel class="hashtag_stack" deck="3" x="+0" panelname="tags3" visibility="deck 3 leftdeck"/>
<panel class="hashtag_stack" deck="2" x="+1920-280" panelname="tags2" visibility="not deck 4 leftdeck"/>
<panel class="hashtag_stack" deck="4" x="+1920-280" panelname="tags4" visibility="deck 4 leftdeck"/>
</group>
MID PANEL: STEM AREA
```

Original line 501:

```xml
<visual class="gfx_shape" source="effect_active colorfx" width="80" height="18" coloroff="#222222" bordercoloroff="transparent" bordersize="1"/>
```

Original line 542:

```xml
STATUS: FX1/2/3
<button x="+0" y="+40" width="28" height="18" action="effect_active 1" border_size="1">
<off color="#222222"/>
<selected color="magenta"/>
<text fontsize="12" color="#111111" colorselected="black" align="center" text="FX1"/>
</button>
<button x="+30" y="+40" width="28" height="18" action="effect_active 2" border_size="1">
<off color="#222222"/>
<selected color="magenta"/>
<text fontsize="12" color="#111111" colorselected="black" align="center" text="FX2"/>
</button>
<button x="+60" y="+40" width="30" height="18" action="effect_active 3" border_size="1">
<off color="#222222"/>
<selected color="magenta"/>
<text fontsize="12" color="#111111" colorselected="black" align="center" text="FX3"/>
</button>
```

Original line 559:

```xml
<panel class="key_display_left" x="+2+4+220+4+120" y="+14"/>
<panel class="bpm_display_left" x="+2+4+200+4+128+4" y="+2"/>
```

Original line 563:

```xml
<define class="_STEM_BUTTON" placeholders="*stem,*label,*color,width=65,height=23,fontsize=13,granularity=23">
TOGGLE
<button x="+0" action="stem_pad '[STEM]'" border_size="1">
<size width="[WIDTH]" height="[HEIGHT]"/>
<off color="#222222" border="#444444" radius="3"/>
<down color="#222222" border="[COLOR]" radius="3"/>
<selected color="transparent" border="[COLOR]" radius="3"/>
<text fontsize="[FONTSIZE]" color="#555555" colorover="[COLOR]" colorselected="[COLOR]" colordown="[COLOR]" align="center" text="[LABEL]"/>
</button>
VU METER
<visual source="get_level '[STEM]'" type="linear" orientation="horizontal" direction="up" granularity="[GRANULARITY]">
<pos x="+0" y="+[HEIGHT]+2"/>
<size width="[WIDTH]" height="7"/>
<off shape="square" border="#2A2A2A" color="black" radius="2"/>
<down shape="square" border="[COLOR]" color="[COLOR]" radius="2"/>
</visual>
GAIN SLIDER
<slider action="param_multiply 50% &amp; stem '[STEM]'" dblclick="stem '[STEM]' 50%" orientation="horizontal" direction="up" frommiddle="false">
<pos x="+0" y="+[HEIGHT]+2"/>
<size width="[WIDTH]" height="7"/>
<fader color="#AAAAAA" width="2" height="5"/>
</slider>
STEM FX
<button x="+0" y="+[HEIGHT]+12" action="stem_pad '[STEM]'" border_size="1">
<size width="[WIDTH]/3" height="[HEIGHT]*0.8"/>
<off color="#222222" border="#444444" radius="3"/>
<down color="#222222" border="[COLOR]" radius="3"/>
<selected color="transparent" border="[COLOR]" radius="3"/>
<text fontsize="[FONTSIZE]" color="#555555" colorselected="[COLOR]" colordown="[COLOR]" align="center" text="FX"/>
</button>
</define>
```

## src/components/transport.xml

Original line 11:

```xml
<panel class="syncoptions_display" x="+2+6" y="+39" />
```

Original line 38:

```xml
<button class="button_main" x="+0" textsize="11" y="+6+30" width="60" height="30" action="match_key" text="KEY" textcolor="red" textcoloron="red" coloroff="red" coloron="red" visibility="loaded ? not masterdeck ? sync_hint"/>
```

Original line 41:

```xml
<button class="button_main" x="+0" y="+6+30+4+62" width="60" height="30" action="cue_button" textaction="cue_button" textcolor="textoff2" textcoloron="black"/>
```

Original line 154:

```xml
PHRASE BUTTON
<button class="button_main" x="+0" action="sync &amp; phrase_sync 32" bordersize="1" query="`is_sync '$phrase_len'`" visibility="not masterdeck">
<pos x="+82*2" condition="param_equal [DECKSIDE] 'left'"/>
<pos x="+82*1" condition="param_equal [DECKSIDE] 'right'"/>
<size width="80" height="25"/>
<off color="#440000" border="#FF3333" radius="3"/>
<down color="#222222" border="deckcolor" radius="3"/>
<selected color="transparent" border="deckcolor" radius="3"/>
<text fontsize="12" color="#FF3333" colorselected="deckcolor" colordown="deckcolor" align="center" text="PHRASE"/>
</button>
```

## src/components/video.xml

Original line 35:

```xml
<panel class="stem_control" stem="hihat" label="HI-HAT" color="colorhihat" x="+240" y="+10"/>
```

Original line 47:

```xml
<textzone action="filter_selectcolorfx">
<pos x="+0" y="+34"/>
<size width="51"/>
<text fontsize="10" weight="" color="knobtextoff" align="center" action="filter_label 'colorfx' &amp; param_cast 'text'" text="" important="true" localize="true"/>
</textzone>
```

Original line 55:

```xml
Stem Toggle Button
<button class="button_main"
x="+0" y="+42" width="45" height="12"
action="stem_pad '[STEM]'"
coloroff="#111111" brcoloroff="#111111"
coloron="[COLOR]" brcoloron="[COLOR]"
textcoloroff="[COLOR]" textcoloron="black"
text="[LABEL]" textsize="10" />
Knob (muted state visible)
<panel class="knob" x="+10" y="+0" textwidth="40" textsize="12" textbelow="+37" textleft="-2" knobsize="34" knobradius="7" faderradius="6" action="stem '[STEM]'" rgclick="stem_pad '[STEM]'" dblclick="stem '[STEM]' 50%" frommiddle="false" fillcolor="#333333" fillcoloroff="#000000" text="" visibility="mute_stem '[STEM]' on"/>
Knob (unmuted state visible)
<panel class="knob" x="+10" y="+0" textwidth="40" textsize="12" textbelow="+37" textleft="-2" knobsize="34" knobradius="8" faderradius="6" action="stem '[STEM]'" rgclick="stem_pad '[STEM]'" dblclick="stem '[STEM]' 50%" frommiddle="false" fillcolor="[COLOR]" fillcoloroff="#000000" text="" visibility="mute_stem '[STEM]' off"/>
SIMPLE VECTOR VU METER
<visual source="get_level '[STEM]'" type="linear" orientation="horizontal" direction="up" granularity="23">
<pos x="+0" y="+55"/>
<size width="40" height="4"/>
<off shape="square" color="#333333" radius="0"/>
<on  shape="square" color="[COLOR]" radius="0"/>
</visual>
BUTTON
```

## src/components/containers/deck/deck-containers.xml

Original line 27:

```xml
<line color="#333333" x="+0" y="+400-2" width="765" height="1"/>
```

Original line 44:

```xml
bg: spine
<visual x="+768" y="+0" width="34" height="[HEIGHT]">
<off shape="square" color="black"/>
</visual>
PRO: RIGHT: PANEL BG
```

Original line 54:

```xml
<panel class="infos2" x="+800-567" visibility="has_video_mix 'active' &amp;&amp; skin_panel 'videomixer'"/>
```

Original line 67:

```xml
<panel class="video_preview" x="+2+60+11+1" y="+6" visibility="has_video_mix 'active' &amp;&amp; skin_panel 'videomixer'"/>
```

Original line 121:

```xml
<define class="DECK_CONTAINER_PERFORMANCE_SPINE" placeholders="*deck,*panelname,*deckside">
<deck deck="[DECK]">
<panel class="deck_spine" height="320" condition="param_equal [DECKSIDE] 'left'"/>
<panel class="deck_spine" height="320" condition="param_equal [DECKSIDE] 'right'"/>
</deck>
</define>
Shared performance body used on the left side and mirrored into the two-deck right-side shell
```

## src/components/containers/mixer/mixer-containers.xml

Original line 20:

```xml
<panel class="knob" x="+18" y="+14+81+68+68+64" knobsize="41" knobradius="10" faderradius="9" action="filter" dblclick="filter 50%" frommiddle="true" fillcolor="knobfillon" textaction="filter_label &amp; param_cast 'text' 9" actiontext="effect_select colorfx"/>
```

Original line 53:

```xml
<visual class="gfx_shape" width="77" height="432-56-1" coloroff="panel_background"/>
3knobs
PRO: MIXER PANEL: EQ KNOBS
```

Original line 57:

```xml
<visual x="+10" y="+6" width="55" height="432-56-16">
<off shape="square" color="#1C1C1C" radius="6" bordersize="1" border="#444444"/>
</visual>
```

Original line 133:

```xml
<textzone>
<pos x="+0" y="+0"/>
<size width="77" height="30"/>
<text fontsize="15" weight="" color="deckcolor" align="center" action="get_level 'db'" important="true"/>
</textzone>
```

Original line 140:

```xml
CUE BUTTON
<button class="button_main" x="+2+4+4" y="+175" width="57" height="24" action="pfl" coloroff="button_background4" brcoloroff="button_background4" textcoloron="black" text="CUE"/>
```

Original line 537:

```xml
panel bg
<visual class="gfx_shape" shape="square" width="312" height="432-56-1" bordercoloroff="red" bordersize="1"/>
header
```

Original line 591:

```xml
<visual x="+0" y="+0" width="310-20" height="34*8+2">
<off shape="square" color="transparent" border_size="3" border="#222222" radius="6"/>
</visual>
border
```

Original line 638:

```xml
<text fontsize="11" color="#FFFFFF" align="left" action="param_equal `sampler_pad_page` &quot;1 to 8&quot; ? get_text '`get_sample_info [INDEX] bpm`bpm' : param_equal `sampler_pad_page` &quot;9 to 16&quot; ? get_text '`get_constant 8 &amp; param_add [INDEX] &amp; get_sample_info bpm`bpm' : param_equal `sampler_pad_page` &quot;17 to 24&quot; ? get_text '`get_constant 16 &amp; param_add [INDEX] &amp; get_sample_info bpm`bpm' : param_equal `sampler_pad_page` &quot;25 to 32&quot; ? get_text '`get_constant 24 &amp; param_add [INDEX] &amp; get_sample_info bpm`bpm' : param_equal `sampler_pad_page` &quot;33 to 40&quot; ? get_text '`get_constant 32 &amp; param_add [INDEX] &amp; get_sample_info bpm`bpm' : param_equal `sampler_pad_page` &quot;41 to 48&quot; ? get_text '`get_constant 40 &amp; param_add [INDEX] &amp; get_sample_info bpm`bpm' : param_equal `sampler_pad_page` &quot;49 to 56&quot; ? get_text '`get_constant 48 &amp; param_add [INDEX] &amp; get_sample_info bpm`bpm' : param_equal `sampler_pad_page` &quot;57 to 64&quot; ? get_text '`get_constant 56 &amp; param_add [INDEX] &amp; get_sample_info bpm`bpm' : get_text ''"/>
```

Original line 681:

```xml
<group name="sampler_mode" x="+10">
label
<textzone class="text" x="+0" y="+0" width="45" height="20" fontsize="8" color="textoff" align="left" weight="" text="MODE"/>
<button x="+0" y="+16" class="button_main" bordersize="1" width="60" height="26" action="sampler_mode" textsize="10" textcolor="white">
<size height="15"/>
<off color="#111111" border="#555555"/>
<down color="#111111" border="#555555"/>
<selected color="#111111" border="#555555"/>
<text align="center" action="sampler_mode &amp; param_uppercase"/>
</button>
</group>
SAMPLER ROUTING TOGGLE HEADPHONES/MASTER
```

Original line 704:

```xml
<button x="-73" class="button_main" bordersize="1" textsize="11" width="60" height="26" action="deck 1 masterdeck ? deck 1 sampler_pad_page +1 : deck 2 masterdeck ? deck 2 sampler_pad_page +1 : deck 3 masterdeck ? deck 3 sampler_pad_page +1 : deck 4 masterdeck ? deck 4 sampler_pad_page +1 : sampler_pad_page +1" textcolor="white">
<size width="60" height="24"/>
<off color="#111111"/>
<down color="#111111"/>
<selected color="#111111"/>
<text align="center" weight="" action="deck 1 masterdeck ? deck 1 sampler_pad 1 : deck 2 masterdeck ? deck 2 sampler_pad 1 : deck 3 masterdeck ? deck 3 sampler_pad 1 : deck 4 masterdeck ? deck 4 sampler_pad 1 : sampler_pad 1"/>
</button>
```

Original line 740:

```xml
BORDER BACKGROUND
<visual x="+0" y="+0" width="144" height="43-8-8">
<off shape="square" color="transparent" border_size="1" border="#444444" radius="4"/>
</visual>
```

Original line 880:

```xml
<visual class="gfx_shape" width="312" height="432-56-1" coloroff="wave_background" bordercoloroff="panel_background" bordersize="2" visibility="var_equal '@$hide_crossfader' 0"/>
<visual class="gfx_shape" width="312" height="432-56-1+57" coloroff="wave_background" bordercoloroff="panel_background" bordersize="2" visibility="var_equal '@$hide_crossfader' 1"/>
LEFT
```

Original line 884:

```xml
<panel class="vertical_scratchwave" deck="1" visibility="not deck 3 leftdeck" x="+40" y="+0"/>
```

Original line 891:

```xml
NEEDLE
<group x="+25" y="+90">
<visual width="260" height="28">
<off shape="square" color="#66000000" border_size="0" border="deckcolor" radius="6"/>
</visual>
<visual y="+13" width="260" height="2">
<off shape="square" color="white" border_size="0" border="deckcolor" radius="1"/>
</visual>
</group>
left aligned
<group visibility="setting 'waveformCenter' 'left'">
shadow
<visual x="+1920/2-6" y="+2" width="10" height="[WAVEFORMHEIGHT]-6">
<off shape="square" color="#55000000" border_size="0" border="deckcolor" radius="6"/>
</visual>
tip
<visual x="+1920/2-2" y="+0" width="2" height="[WAVEFORMHEIGHT]" visibility="select">
<off shape="square" color="white" border_size="0" border="deckcolor" radius="6"/>
</visual>
</group>
center aligned
```

Original line 1086:

```xml
Play/Pause Button
<button x="+0" y="+17"
width="[WIDTH]" height="15"
action="play_pause"
border_size="0">
<off color="#111111"/>
<over color="[OVERCOLOR]"/>
<selected color="deckcolor"/>
<icon dx="-2" sysicon="play"
width="37" height="33"
color="[TEXTCOLOR]" colordown="white"
colorselected="black"/>
</button>
```

Original line 1113:

```xml
PLAY state (no decks playing)
<button width="66" height="34" action="deck left play &amp; deck right play &amp; deck all sync &amp; phrase_sync" sysicon="play_button" iconsize="39">
<off color="#000000" border="#333333" border_size="1" shape="square" radius="4" iconcolor="white"/>
<over color="#111111" border="#666666" border_size="1" shape="square" radius="4" iconcolor="#999999"/>
<down color="#111111" border="#888888" border_size="1" shape="square" radius="4" iconcolor="#999999"/>
<selected color="white" border="white" radius="4" iconcolor="white"/>
</button>
STOP state (any deck playing)
<button textsize="11" width="66" height="34" visibility="deck 1 play or deck 2 play or deck 3 play or deck 4 play" action="deck all pause &amp; sampler stop all" sysicon="play_button" iconsize="39">
<off color="#000000" border="#333333" border_size="1" shape="square" radius="4" iconcolor="#999999"/>
<over color="#111111" border="#666666" border_size="1" shape="square" radius="4" iconcolor="#999999"/>
<down color="#111111" border="#888888" border_size="1" shape="square" radius="4" iconcolor="#666666"/>
<selected color="white" border="white" radius="4" iconcolor="white"/>
</button>
```

Original line 1138:

```xml
<button class="button_main" x="+30" y="+20" width="40" height="40" border="deck 1 deckcolor" border_size="3" action="invert_deck left" coloroff="deckcolor" text="" textcolor="white" iconsize="40" sysicon="play" border="0" shape="circle"/>
<button class="button_main" x="+5" y="+55" width="30" height="30" action="invert_deck left" coloroff="#222222" text="" textcolor="white" iconsize="30" sysicon="goto_last_folder" border="0" shape="circle"/>
<button class="button_main" x="+276" y="+55" width="30" height="30" action="invert_deck right" coloroff="#222222" text="" textcolor="white" iconsize="30" sysicon="goto_last_folder" border="0" shape="circle"/>
HAS LINKED TRACKS
<button class="button_main"
x="+106" y="+68" width="100" height="15"
action="browser_sideview 'linked'"
query="has_linked_tracks"
text="LINK"
textcolor="textoff3"
textcoloron="green"
textsize="10"
/>
LINK TRACKS BUTTON
<button class="button_main"
x="+65" y="+64" width="50" height="15"
action="mark_linked_tracks"
text="LINK"
textcolor="#888888"
textcoloron="black"
coloron="green"
textsize="10" />
<button class="button_main" x="+62*3" y="+70" width="63" height="17" action="crossfader_curve 'custom' ? setting 'crossfaderDisable' : crossfader_curve 'custom'" query="crossfader_curve 'custom' ? not setting 'crossfaderDisable' ? true : false" coloroff="xf_background" coloron="xf_background" brcoloroff="xf_background" brcoloron="xf_background" textsize="10" textcolor="textoff3" textcoloron="needle" textaction="get_text 'CUSTOM'"/>
<button class="button_main" x="+62*4" y="+70" width="63" height="17" action="crossfader_curve 'cut' ? setting 'crossfaderDisable' : crossfader_curve 'cut'" query="crossfader_curve 'cut' ? not setting 'crossfaderDisable' ? true : false" coloroff="xf_background" coloron="xf_background" brcoloroff="xf_background" brcoloron="xf_background" textsize="10" textcolor="textoff3" textcoloron="needle" textaction="get_text 'CUT'"/>
```

## src/components/containers/pads/pad-containers.xml

Original line 76:

```xml
Pads (Default)
<panel name="@padssl_[PANELNAME]" group="pads16++_[PANELNAME]" visible="yes" available="yes" displayname="Pads (Default)">
<visual class="gfx_shape" x="+10" y="+6" width="454+45" height="28" coloroff="xf_background"/>
<group name="pad_param1" visibility="pad_has_param 1">
<button class="button_main" x="+10" y="+6" width="26" height="28" action="pad_param -1" iconsize="20" sysicon="arrowleft" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
<button class="button_main" x="+10+26" y="+6" width="82" height="28" action="pad_param +1" query="off" textaction="pad_param" coloroff="xf_background" coloron="xf_background" bordersize="0" textsize="10" textcolor="textdarker"/>
<button class="button_main" x="+10+26+82" y="+6" width="26" height="28" action="pad_param +1" iconsize="20" sysicon="arrowright" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
</group>
<group name="pad_param1" x="+45" visibility="pad_param_visible 2">
<button class="button_main" x="+454+10-26-82-26" y="+6" width="26" height="28" action="pad_param2 -1" iconsize="20" sysicon="arrowleft" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
<button class="button_main" x="+454+10-26-82" y="+6" width="82" height="28" action="cccccccccery="off" textaction="pad_param2" coloroff="xf_background" coloron="xf_background" bordersize="0" textsize="10" textcolor="textdarker"/>
<button class="button_main" x="+454+10-26" y="+6" width="26" height="28" action="pad_param2 +1" iconsize="20" sysicon="arrowright" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
</group>
<button class="button_main" x="+10+150" y="+6" width="454-300+45" height="28" action="pad_page_select" query="on/off" rightclick="pad_bank2" scroll="pad_page" tooltip="Select a different pad page.\nRigth-click: Switch Pad bank 1 - Pad bank 2" textsize="13" textaction="pad_page & param_uppercase" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textoff2"/>
</panel>
```

Original line 103:

```xml
Pads (5 btn)
<panel name="@padsbtns2_[PANELNAME]" group="pads16++_[PANELNAME]" visible="no" available="yes" displayname="Pads (5 btns)">
<button class="button_main" x="+10" y="+6" width="95" height="28" action="shift ? pad_pages 26 : pad_pages 1 ? pad_pages 5 : pad_pages 1" rightclick="pad_pages 26 ? pad_page_select 26 : pad_pages 5 ? pad_page_select 5 : pad_page_select 1" query="pad_pages 26 ? blink 400ms : pad_pages 5 ? blink : pad_pages 1" tooltip="Select this pad page, one more click shows pad bank 2.\nRigth-click: select a different pad page." textcoloron="needle" textsize="13" textaction="pad_pages 26 ? pad_pages 26 & param_uppercase : pad_pages 5 ? pad_pages 5 & param_uppercase : pad_pages 1 & param_uppercase" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
<button class="button_main" x="+10+101" y="+6" width="95" height="28" action="shift ? pad_pages 27 : pad_pages 2 ? pad_pages 6 : pad_pages 2" rightclick="pad_pages 27 ? pad_page_select 27 : pad_pages 6 ? pad_page_select 6 : pad_page_select 2" query="pad_pages 27 ? blink 400ms : pad_pages 6 ? blink : pad_pages 2" tooltip="Select this pad page, one more click shows pad bank 2.\nRigth-click: select a different pad page." textcoloron="needle" textsize="13" textaction="pad_pages 27 ? pad_pages 27 & param_uppercase : pad_pages 6 ? pad_pages 6 & param_uppercase : pad_pages 2 & param_uppercase" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
<button class="button_main" x="+10+101+101" y="+6" width="95" height="28" action="shift ? pad_pages 28 : pad_pages 3 ? pad_pages 7 : pad_pages 3" rightclick="pad_pages 28 ? pad_page_select 28 : pad_pages 7 ? pad_page_select 7 : pad_page_select 3" query="pad_pages 28 ? blink 400ms : pad_pages 7 ? blink : pad_pages 3" tooltip="Select this pad page, one more click shows pad bank 2.\nRigth-click: select a different pad page." textcoloron="needle" textsize="13" textaction="pad_pages 28 ? pad_pages 28 & param_uppercase : pad_pages 7 ? pad_pages 7 & param_uppercase : pad_pages 3 & param_uppercase" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
<button class="button_main" x="+10+101+101+101" y="+6" width="95" height="28" action="shift ? pad_pages 29 : pad_pages 4 ? pad_pages 19 : pad_pages 19 ? pad_pages 8 : pad_pages 4" rightclick="pad_pages 29 ? pad_page_select 29 : pad_pages 4 ? pad_page_select 4 : pad_pages 19 ? pad_page_select 19 : pad_page_select 8" query="pad_pages 29 ? blink 400ms : pad_pages 8 ? blink : pad_pages 4 ? on : pad_pages 19" tooltip="Select this pad page, one more click shows pad bank 2.\nRigth-click: select a different pad page." textcoloron="needle" textsize="13" textaction="pad_pages 29 ? pad_pages 29 & param_uppercase : pad_pages 19 ? pad_pages 19 & param_uppercase : pad_pages 8 ? pad_pages 8 & param_uppercase : pad_pages 4 & param_uppercase" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
<button class="button_main" x="+10+101+101+101+101" y="+6" width="95" height="28" action="shift ? pad_pages 30 : pad_pages 12 ? pad_pages 16 : pad_pages 12" rightclick="pad_pages 30 ? pad_page_select 30 : pad_pages 16 ? pad_page_select 16 : pad_page_select 12" query="pad_pages 30 ? blink 400ms : pad_pages 16 ? blink : pad_pages 12" tooltip="Select this pad page, one more click shows pad bank 2.\nRigth-click: select a different pad page." textcoloron="needle" textsize="13" textaction="pad_pages 30 ? pad_pages 30 & param_uppercase : pad_pages 16 ? pad_pages 16 & param_uppercase : pad_pages 12 & param_uppercase" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
</panel>
Hot Cues
```

Original line 146:

```xml
Pads (Default)
<panel name="@padssl_[PANELNAME]" group="pads16++_[PANELNAME]" visible="yes" available="yes" displayname="Pads (Default)">
<visual class="gfx_shape" x="+10" y="+6" width="454+45-80-52" height="28" coloroff="xf_background"/>
<group name="pad_param1" visibility="pad_has_param 1">
<button class="button_main" x="+10" y="+6" width="26" height="25" action="pad_param -1" iconsize="20" sysicon="arrowleft" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
<button class="button_main" x="+10+26" y="+6" width="82-12" height="25" action="pad_param +1" query="off" textaction="pad_param" coloroff="xf_background" coloron="xf_background" bordersize="0" textsize="10" textcolor="textdarker"/>
<button class="button_main" x="+10+26+82-12" y="+6" width="26" height="25" action="pad_param +1" iconsize="20" sysicon="arrowright" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
</group>
<group name="pad_param1" x="+45-78-54+12" visibility="pad_param_visible 2">
<button class="button_main" x="+454+10-26-82-26" y="+6" width="26" height="28" action="pad_param2 -1" iconsize="20" sysicon="arrowleft" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
<button class="button_main" x="+454+10-26-82" y="+6" width="82-12" height="28" action="pad_param2 +1" query="off" textaction="pad_param2" coloroff="xf_background" coloron="xf_background" bordersize="0" textsize="10" textcolor="textdarker"/>
<button class="button_main" x="+454+10-26-12" y="+6" width="26" height="28" action="pad_param2 +1" iconsize="20" sysicon="arrowright" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textdarker"/>
</group>
<button class="button_main" x="+10+150-12" y="+6" width="454-300+45-78-54+24" height="28" action="pad_page_select" query="on/off" rightclick="pad_bank2" scroll="pad_page" tooltip="Select a different pad page.\nRigth-click: Switch Pad bank 1 - Pad bank 2" textsize="13" textaction="pad_page & param_uppercase" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textoff2"/>
</panel>
Pads (8 Pads)
```

Original line 192:

```xml
<panel class="hcue_button_vert" x="+10" y="+30*7" source="8"/>
```

Original line 200:

```xml
<panel class="hcue_button_vert" x="+10+185" y="+30*7" source="15"/>
```

Original line 212:

```xml
<panel visibility="not skin_panel '@hotcuesx16_[PANELNAME]' ? not pad_bank2 : false">
<panel class="padbutton_vert" x="+10" y="+6+34" width="88" height="50" source="1"/>
<panel class="padbutton_vert" x="+10+93" y="+6+34" width="88" height="50" source="2"/>
<panel class="padbutton_vert" x="+10+93+93" y="+6+34" width="88" height="50" source="3"/>
<panel class="padbutton_vert" x="+10+93+93+93" y="+6+34" width="88" height="50" source="4"/>
<panel class="padbutton_vert" x="+10" y="+6+34+50+5" width="88" height="50" source="5"/>
<panel class="padbutton_vert" x="+10+93" y="+6+34+50+5" width="88" height="50" source="6"/>
<panel class="padbutton_vert" x="+10+93+93" y="+6+34+50+5" width="88" height="50" source="7"/>
<panel class="padbutton_vert" x="+10+93+93+93" y="+6+34+50+5" width="88" height="50" source="8"/>
</panel>
```

Original line 293:

```xml
PAD PAGE SELECT
<button class="button_main" x="+6" y="+6" width="100" height="28" action="pad_page_select" query="on/off" rightclick="pad_bank2" scroll="pad_page" tooltip="Select a different pad page.\nRigth-click: Switch Pad bank 1 - Pad bank 2" textsize="13" textaction="pad_page & param_uppercase" align="left" coloroff="xf_background" coloron="xf_background" bordersize="0" textcolor="textoff2"/>
PAD PAGE MENU
<button class="menu_button" action="pad_menu" query="on/off" x="+6+270" y="+6+5" width="18" height="18" visibility="pad_has_menu"/>
PAD PAGE TABS
```

Original line 299:

```xml
background
<visual class="gfx_shape" x="+0" y="+6" width="299" height="24" coloroff="xf_background"/>
buttons
```

Original line 307:

```xml
PAD PAGE PARAM 1
<group name="pad_param1" x="+105" visibility="pad_has_param 1">
<button class="button_main" query="on/off" x="+0" y="+6" width="26" height="28" action="pad_param -1" iconsize="20" sysicon="arrowleft" coloroff="transparent" coloron="transparent" bordersize="0" textcolor="textdarker"/>
<button class="button_main" query="on/off" x="+26" y="+6" width="36" height="28" action="pad_param +1" query="off" textaction="pad_param" coloroff="transparent" coloron="transparent" bordersize="0" textsize="10" textcolor="textdarker" textscroll="true"/>
<button class="button_main" query="on/off" x="+0+26+36" y="+6" width="26" height="28" action="pad_param +1" iconsize="20" sysicon="arrowright" coloroff="transparent" coloron="transparent" bordersize="0" textcolor="textdarker"/>
</group>
PAD PAGE PARAM 2
<group name="pad_param1" x="+104+78" visibility="pad_param_visible 2">
<button class="button_main" query="on/off" x="+0" y="+6" width="26" height="28" action="pad_param2 -1" iconsize="20" sysicon="arrowleft" coloroff="transparent" coloron="transparent" bordersize="0" textcolor="textdarker"/>
<button class="button_main" query="on/off" x="+26" y="+6" width="36" height="28" action="pad_param2 +1" query="off" textaction="pad_param2" coloroff="transparent" coloron="transparent" bordersize="0" textsize="10" textcolor="textdarker" textscroll="true"/>
<button class="button_main" query="on/off" x="+0+26+36" y="+6" width="26" height="28" action="pad_param2 +1" iconsize="20" sysicon="arrowright" coloroff="transparent" coloron="transparent" bordersize="0" textcolor="textdarker"/>
</group>
```

Original line 320:

```xml
12 PADS
<panel>
<panel class="padbutton-extra-small" x="+0" y="+8+24" source="1"/>
<panel class="padbutton-extra-small" x="+75" y="+8+24" source="2"/>
<panel class="padbutton-extra-small" x="+75*2" y="+8+24" source="3"/>
<panel class="padbutton-extra-small" x="+75*3" y="+8+24" source="4"/>
<panel class="padbutton-extra-small" x="+0" y="+8+24+42" source="5"/>
<panel class="padbutton-extra-small" x="+75" y="+8+24+42" source="6"/>
<panel class="padbutton-extra-small" x="+75*2" y="+8+24+42" source="7"/>
<panel class="padbutton-extra-small" x="+75*3" y="+8+24+42" source="8"/>
<panel class="padbutton-extra-small" x="+0" y="+8+24+84" source="9"/>
<panel class="padbutton-extra-small" x="+75" y="+8+24+84" source="10"/>
<panel class="padbutton-extra-small" x="+75*2" y="+8+24+84" source="11"/>
<panel class="padbutton-extra-small" x="+75*3" y="+8+24+84" source="12" />
</panel>
STACK: 16 PADS
```

## src/components/containers/pads/page-selector.xml

Original line 40:

```xml
BACKGROUND
<visual width="752" height="40*4+50+35" query="shift">
<off shape="square" color="dark_1" border="dark_0" border_size="1" radius="5"/>
<on shape="square" color="red" border="dark_0" border_size="1" radius="5"/>
</visual>
```

Original line 46:

```xml
<visual x="-1" y="+45" width="730+2" height="40*4+8">
<off shape="square" color="dark_6" border="0" radius="6"/>
</visual>
16 PADS
```

Original line 100:

```xml
8-button style
<panel group="pads16_[PANELNAME]" visible="yes" available="yes" displayname="16 Pads">
BACK ROW
<group x="+20" y="+8">
<button class="pad_page_upper_bank_tab" page="5" x="+4"/>
<button class="pad_page_upper_bank_tab" page="6" x="+4+110*1"/>
<button class="pad_page_upper_bank_tab" page="7" x="+4+110*2"/>
<button class="pad_page_upper_bank_tab" page="8" x="+4+110*3"/>
</group>
FRONT ROW
<group x="+20" y="+23">
<button class="PAD_PAGE_LOWER_TAB" page="1" altpage="5" x="+0" y="+1"/>
<button class="PAD_PAGE_LOWER_TAB" page="2" altpage="6" x="+2+110" y="+1"/>
<button class="PAD_PAGE_LOWER_TAB" page="3" altpage="7" x="+2+110*2" y="+1"/>
<button class="PAD_PAGE_LOWER_TAB" page="4" altpage="8" x="+2+110*3" y="+1"/>
</group>
</panel>
PAD BUTTONS
```

Original line 232:

```xml
<define class="MINI_CUE_BUTTON" placeholders="*index,*width=20,*height=20">
<size width="[WIDTH]" height="[HEIGHT]"/>
<off color="transparent" border="dark_7" border_size="1" radius="5"/>
<text fontsize="12" color="light_3" colorover="light_0" align="center" text="[INDEX]"/>
</define>
<button class="MINI_CUE_BUTTON" index="1" x="+0" y="+0" action="hot_cue 1" query="has_cue 1">
<selected color="transparent" border="`cue_color 1`" border_size="1" radius="5"/>
<downselected color="transparent" border="`cue_color 1`" border_size="1" radius="5"/>
<textselected fontsize="12" color="`cue_color 1`" align="center" text="1"/>
</button>
<button class="MINI_CUE_BUTTON" index="2" x="+21" y="+0" action="hot_cue 2" query="has_cue 2">
<selected color="transparent" border="`cue_color 2`" border_size="1" radius="5"/>
<downselected color="transparent" border="`cue_color 2`" border_size="1" radius="5"/>
<textselected fontsize="12" color="`cue_color 2`" align="center" text="2"/>
</button>
```

Original line 271:

```xml
PAD AREA BORDER
<visual x="+0" y="+21" width="508" height="166">
<off shape="square" color="transparent" border="#222222" border_size="4" radius="8"/>
</visual>
<visual x="+0" y="+21" width="508" height="166">
<off shape="square" color="transparent" border="dark_5" border_size="1" radius="6"/>
</visual>
```

## src/components/containers/racks/rack-containers.xml

Original line 26:

```xml
background (second case: if 16 pads enabled show 2px more at the bottom)
<visual class="gfx_shape" width="504" height="80" coloroff="panel_background" visibility="not skin_panel '@pads16_[PANELNAME]'"/>
<visual class="gfx_shape" width="504" height="80+2" coloroff="panel_background" visibility="skin_panel '@pads16_[PANELNAME]'"/>
left deck fx panel tab button
<panel class="tab_button" action="skin_panelgroup 'efx_[PANELNAME]' +1" action3="skin_panelgroup_available 'efx_[PANELNAME]'" query="on/off" width="30" height="80" orientation="vertical" posrec="+27" heightrec="30" textaction="skin_panel '@pads16_[PANELNAME]' ? get_text 'PADS' : get_text 'FX'" visibility="leftdeck ? not skin_panel '@pads16_[PANELNAME]'"/>
right deck fx panel tab button
<panel class="tab_button" action="skin_panelgroup 'efx_[PANELNAME]' +1" action3="skin_panelgroup_available 'efx_[PANELNAME]'" query="on/off" x="+504-30" width="30" height="80" orientation="vertical-cw" posrec="+27" heightrec="30" textaction="skin_panel '@pads16_[PANELNAME]' ? get_text 'PADS' : get_text 'FX'" visibility="rightdeck ? not skin_panel '@pads16_[PANELNAME]'"/>
left deck 16-pad panel tab button
<panel class="tab_button" action="skin_panelgroup 'efx_[PANELNAME]' +1" action3="skin_panelgroup_available 'efx_[PANELNAME]'" query="on/off" width="30" height="80+2+132" orientation="vertical" posrec="+27" heightrec="160" textaction="skin_panel '@pads16_[PANELNAME]' ? get_text 'PADS' : get_text 'FX'" visibility="leftdeck ? skin_panel '@pads16_[PANELNAME]'"/>
right deck 16-pad panel tab button
<panel class="tab_button" action="skin_panelgroup 'efx_[PANELNAME]' +1" action3="skin_panelgroup_available 'efx_[PANELNAME]'" query="on/off" x="+504-30" width="30" height="80+2+132" orientation="vertical-cw" posrec="+27" heightrec="160" textaction="skin_panel '@pads16_[PANELNAME]' ? get_text 'PADS' : get_text 'FX'" visibility="rightdeck ? skin_panel '@pads16_[PANELNAME]'"/>
left deck fx panel menu button
<menu class="menu_button_fx" tooltip="FX OPTIONS" query="on/off" x="+6" y="+6" width="18" height="18" visibility="leftdeck ? not skin_panel '@pads16_[PANELNAME]'"/>
left deck 16-pad panel menu button
<button class="menu_button" action="pad_menu" query="on/off" x="+6" y="+6" width="18" height="18" visibility="leftdeck ? skin_panel '@pads16_[PANELNAME]' ? pad_has_menu"/>
right deck fx panel menu button
<menu class="menu_button_fx" tooltip="FX OPTIONS" query="on/off" x="+504-30+6" y="+6" width="18" height="18" visibility="rightdeck ? not skin_panel '@pads16_[PANELNAME]'"/>
right deck 16-pad panel menu button
<button class="menu_button" action="pad_menu" query="on/off" x="+504-30+6" y="+6" width="18" height="18" visibility="rightdeck ? pad_has_menu ? skin_panel '@pads16_[PANELNAME]'"/>
```

Original line 316:

```xml
<define class="pads_rack" placeholders="deck,*panelname">
<deck deck="[DECK]">
background
<visual class="gfx_shape" width="504" height="132" coloroff="panel_background"/>
<panel class="tab_button" action="skin_panelgroup 'pads16_[PANELNAME]' +1" action2="pad_menu" action3="skin_panelgroup_available 'pads16_[PANELNAME]'" query="on/off" width="30" height="132" orientation="vertical" text="PADS" visibility="leftdeck ? not skin_panel '@pads16_[PANELNAME]'"/>
<button class="menu_button" action="pad_menu" query="on/off" x="+6" y="+6" width="18" height="18" visibility="leftdeck ? pad_has_menu"/>
<panel class="tab_button" action="skin_panelgroup 'pads16_[PANELNAME]' +1" action2="pad_menu" action3="skin_panelgroup_available 'pads16_[PANELNAME]'" query="on/off" x="+504-30" width="30" height="132" orientation="vertical-cw" text="PADS" menuvisible="pad_has_menu" visibility="rightdeck ? not skin_panel '@pads16_[PANELNAME]'"/>
<button class="menu_button" action="pad_menu" query="on/off" x="+504-30+6" y="+6" width="18" height="18" visibility="rightdeck ? pad_has_menu"/>
<panel class="pads" x="+32-2" panelname="[PANELNAME]" visibility="leftdeck"/>
<panel class="pads" panelname="[PANELNAME]" visibility="rightdeck"/>
</deck>
</define>
Wrapper for the vertical performance pad surface
```

## src/components/containers/topbar/menu-items.xml

Original line 153:

```xml
<item text="Auto Zoom (with controllers)" localize="true" action="toggle '@$browser_zoom_mode'" check="var_equal '@$browser_zoom_mode' 1"/>
```

## src/components/containers/topbar/topbar-containers.xml

Original line 50:

```xml
<visual class="gfx_shape" width="1920" height="50" coloroff="red"/>
DECK MODE BUTTONS
```

Original line 53:

```xml
<button tooltip="UTILITY BAR MODE\nToggle between utility bar and hashtag bar at the bottom of the screen." class="button_main" action="toggle '@$bottombar_mode'" width="26" height="27" textsize="12" textcolor="needle" textaction="var_equal '@$bottombar_mode' 1 ? get_text '#' : get_text 'U'" coloroff="panel_background" coloron="#222222" query="true" bordersize="0"/>
<button tooltip="BORDER MODE\nShow or hide the active deck border." class="button_main" x="+30" action="toggle '@$dd_bordermode'" width="26" height="27" textsize="12" textcoloron="needle" text="B" coloroff="panel_background" coloron="#222222" bordersize="0"/>
```

Original line 56:

```xml
<button tooltip="" class="button_main" x="+122" action="setting 'showLyrics'" width="60" height="27" textsize="12" textcoloron="needle" text="LYRICS" coloroff="#101010" coloron="#222222" bordersize="0"/>
<button tooltip="SAMPLE PADS\nToggle sample pads." class="button_main" x="+125" action="sideview_triggerpad 'sideview' &amp; sideview_triggerpad &amp; show_splitpanel 'sideview'" width="70" height="27" textsize="12" textcoloron="needle" text="SAMPLES" coloroff="#101010" coloron="#222222" bordersize="0" query=""/>
```

Original line 167:

```xml
<button class="button_main" x="+1150" y="+8" width="60" height="12" action="setting 'hotcueMode' 'play'" query="setting 'hotcueMode' 'play'" textsize="11" text="CUE PLAY" coloroff="button_background3" coloron="button_background3" bordersize="0" textcolor="textoff3" textcoloron="needle"/>
<button class="button_main" x="+1150" y="+8+12+2" width="60" height="12" action="setting 'hotcueMode' 'stutter'" textsize="11" text="STUTTER" coloroff="button_background3" coloron="button_background3" bordersize="0" textcolor="textoff3" textcoloron="needle" query="slip_mode ? blink 800ms : off"/>
```

Original line 190:

```xml
layout buttons (separate)
<group x="+8" y="+11">
<button class="button_main" action="set '@$performance_layout' 1 &amp; load_skin" width="40" height="22" color="transparent" coloroff="transparent" bordersize="0" align="center" radius="10">
<text overcolor="#999999" weight="normal" size="14" oncolor="white" text="VERT"/>
</button>
<button class="button_main" x="+53" action="set '@$performance_layout' 2 &amp; load_skin" width="40" height="22" color="transparent" coloroff="transparent" bordersize="0" align="center" radius="6">
<text overcolor="#999999" weight="normal" size="14" oncolor="white" text="HORIZ"/>
</button>
<button class="button_main" x="+53+50" action="set '@$performance_layout' 0 &amp; load_skin" width="40" height="22" color="transparent" coloroff="transparent" bordersize="0" align="center" radius="6">
<text overcolor="#999999" weight="normal" size="14" oncolor="white" text="EXT"/>
</button>
<line x="+45" y="-2" width="1" height="26" highlight="#666666" shadow="000000"/>
<line x="+100" y="-2" width="1" height="26" highlight="#666666" shadow="000000"/>
</group>
```

Original line 231:

```xml
<button class="button_main" x="115+80+300+75+75" y="8" width="32" height="27" tooltip="Quantize all" action="deck 1 quantize_all &amp; deck 2 quantize_all &amp; deck 3 quantize_all &amp; deck 4 quantize_all" textsize="10" text="QT" coloron="br_focus" bordersize="0"/>
```

Original line 235:

```xml
<button class="button_main" x="115+80+300+90+643" y="8" width="75" height="27" action="sandbox" textsize="10" textcoloron="texton" text="SANDBOX" coloron="orange" bordersize="0" query="sandbox ? blink 300ms"/>
```

Original line 239:

```xml
<group name="beatbar">
<panel condition="var_equal '@$4decks' 0">
<panel class="beat_keeper_ex" deck="1" x="+884" y="+8"/>
<panel class="beat_keeper_ex" deck="2" x="+884" y="+8+12+4"/>
</panel>
<panel condition="var_not_equal '@$4decks' 0">
<panel class="beat_keeper_ex" deck="1" x="+890-86" y="+8"/>
<panel class="beat_keeper_ex" deck="2" x="+890+75" y="+8"/>
<panel class="beat_keeper_ex" deck="3" x="+890-86" y="+8+12+4"/>
<panel class="beat_keeper_ex" deck="4" x="+890+75" y="+8+12+4"/>
<panel class="phrase_circle" x="+890-128-40" y="+6" deck="3" visibility="var_equal '@$phrasecircle' 1"/>
<panel class="phrase_circle" x="+890-128" y="+6" deck="1" visibility="var_equal '@$phrasecircle' 1"/>
<panel class="phrase_circle" x="+890+234" y="+6" deck="2" visibility="var_equal '@$phrasecircle' 1"/>
<panel class="phrase_circle" x="+890+234+40" y="+6" deck="4" visibility="var_equal '@$phrasecircle' 1"/>
</panel>
</group>
```

Original line 293:

```xml
<group visibility="var_equal '@$show_zoom_racks' 1 ? constant 0 : constant 0.75">
<visual class="gfx_shape" x="+490" width="220" height="43" coloroff="panel_background" visibility="var '@$browser_zoom_mode' 1 ? browser_zoom ? true : browser_isactive ? true : false : browser_zoom ? true : false"/>
</group>
<group visibility="var_equal '@$show_zoom_racks' 1 ? constant 0.75">
<visual class="gfx_shape" x="+490" width="58" height="43" coloroff="panel_background" visibility="var '@$browser_zoom_mode' 1 ? browser_zoom ? true : browser_isactive ? true : false : browser_zoom ? true : false"/>
</group>
SANDBOX
<button class="button_main" x="115+80+300+90+643" y="8" width="75" height="27" action="sandbox" textsize="10" textcoloron="texton" text="SANDBOX" coloron="orange" bordersize="0" query="sandbox ? blink 300ms"/>
DISABLED SANDBOX
<group visibility="0.75">
<visual class="gfx_shape" x="115+80+300+90+643" y="8" width="75" height="27" coloroff="panel_background" visibility="not can_sandbox"/>
</group>
<group name="beatbar">
<panel condition="var_equal '@$4decks' 0">
<panel class="beat_keeper_ex" deck="1" x="+884" y="+8"/>
<panel class="beat_keeper_ex" deck="2" x="+884" y="+8+12+4"/>
</panel>
<panel condition="var_not_equal '@$4decks' 0">
<panel class="beat_keeper_ex" deck="1" x="+890-86" y="+8"/>
<panel class="beat_keeper_ex" deck="2" x="+890+75" y="+8"/>
<panel class="beat_keeper_ex" deck="3" x="+890-86" y="+8+12+4"/>
<panel class="beat_keeper_ex" deck="4" x="+890+75" y="+8+12+4"/>
<panel class="phrase_circle" x="+890-128-40" y="+6" deck="3" visibility="var_equal '@$phrasecircle' 1"/>
<panel class="phrase_circle" x="+890-128" y="+6" deck="1" visibility="var_equal '@$phrasecircle' 1"/>
<panel class="phrase_circle" x="+890+234" y="+6" deck="2" visibility="var_equal '@$phrasecircle' 1"/>
<panel class="phrase_circle" x="+890+234+40" y="+6" deck="4" visibility="var_equal '@$phrasecircle' 1"/>
</panel>
</group>
```

Original line 324:

```xml
FX: IS_USING ''
<group x="+0">
<visual type="transparent" source="is_using 'padfx' ? blink 500ms">
<pos x="+0" y="+8" width="12" height="12"/>
<off color="tab_menu" border="tab_menu" shape="circle"/>
<on color="green" border="green" shape="circle"/>
</visual>
<button class="button_main" x="+4" width="40" height="27" textsize="12" text="FX" radius="6" coloroff="transparent" coloron="transparent" bordersize="0" textcolor="#888888" textcoloron="#888888" brcoloroff="transparent" brcoloron="transparent" action="deck all effect_active 'Echo' off &amp; effect_active 'Reverb' off &amp; effect_active 'Delay' off &amp; effect_active 'Cut' off &amp; effect_active 'Echo Out' off &amp; effect_active 'Loop Roll' off &amp;    effect_active 'Backspin' off &amp;    effect_active 'Brake' off &amp;    effect_active 'Spiral' off &amp;    effect_active 'Phaser' off &amp;    effect_active 'Beatgrid' off &amp;    effect_active 'Gate' off" query="effects_used ? blink 500ms"/>
</group>
PADFX: EFFECTS_USED
<group x="+0">
<visual type="transparent" source="effects_used 'padfx' ? blink 500ms : false">
<pos x="+0" y="+8" width="12" height="12"/>
<off color="tab_menu" border="tab_menu" shape="circle"/>
<on color="green" border="green" shape="circle"/>
</visual>
<button class="button_main" x="+18" width="40" height="27" textsize="12" text="FX" align="left" radius="6" coloroff="transparent" coloron="transparent" bordersize="0" textcolor="#888888" textcoloron="#888888" brcoloroff="transparent" brcoloron="transparent" action="deck all effect_disable_all" query="effects_used ? blink 500ms"/>
</group>
COLORFX
<group x="+60">
<visual type="transparent" source="deck all effect_active colorfx ? blink 500ms : false">
<pos x="+0" y="+8" width="12" height="12"/>
<off color="tab_menu" border="tab_menu" shape="circle"/>
<on color="green" border="green" shape="circle"/>
</visual>
<button class="button_main" x="+18" width="40" height="27" textsize="12" text="CFX" align="left" radius="6" coloroff="transparent" coloron="transparent" bordersize="0" textcolor="#888888" textcoloron="#888888" brcoloroff="transparent" brcoloron="transparent" action="deck all effect_active colorfx off" query="deck 1 effect_active colorfx ? blink 500ms : deck 2 effect_active colorfx ? true : deck 3 effect_active colorfx ? true : deck 4 effect_active colorfx"/>
</group>
COLORFX INDICATOR
```

Original line 581:

```xml
<line x="+0" y="+42" width="1920" height="1" highlight="#666666" shadow="000000"/>
```

## src/components/containers/waveform/horizontal-waveform.xml

Original line 45:

```xml
<size width="[HEIGHT]" height="[HEIGHT]"/>
```

Original line 88:

```xml
<size width="[HEIGHT]" height="[HEIGHT]"/>
```

Original line 130:

```xml
PRO: HORIZONTAL WAVEFORM: BORDER
<visual source="select" x="+34" y="+0" visibility="var_equal '@$dd_bordermode' 1">
<size width="1920-34-34" height="[HEIGHT]"/>
<size width="[HEIGHT]" height="[HEIGHT]"/>
<down color="transparent" border_size="1" border="deckcolor" shape="square" radius="10"/>
</visual>
```

## src/components/containers/waveform/main-waveform.xml

Original line 858:

```xml
ZOOM SLIDER
<slider action="zoom & zoom_scratch" dblclick="zoom 28% & zoom_scratch 28%" orientation="vertical" frommiddle="false" visibility="0.8">
<pos x="+10" y="+10"/>
<size width="20" height="[WAVEFORMHEIGHT]-10-10"/>
<off color="xf_background" border="textdarker" shape="square"/>
<on color="xf_background" border="textdarker" shape="square"/>
<fader color="needle" width="18" height="7"/>
</slider>
WAVEFORM SIZE UP DOWN
bg
```

## src/components/containers/waveform/scratch-waveforms.xml

Original line 62:

```xml
<overlay>
<pos x="+0" y="[OVERLAY_Y]"/>
<size width="90" height="4"/>
<background color="needle" shape="square"/>
</overlay>
```

## src/layouts/browser/mini.xml and src/layouts/performance/extended.xml

Original line 93:

```xml
<panel class="deck_container_mini" x="+2" panelname="deck3" deck="3" visibility="deck 3 leftdeck"/>
```

Original line 149:

```xml
<panel class="DECK_CONTAINER_PERFORMANCE_BODY" x="+2" panelname="deck1" deck="1" visibility="not deck 3 leftdeck"/>
<panel class="DECK_CONTAINER_PERFORMANCE_BODY" x="+2" panelname="deck3" deck="3" visibility="deck 3 leftdeck"/>
```

Original line 156:

```xml
<panel class="DECK_CONTAINER_PERFORMANCE_BODY" x="+1920-2-878-77-2" panelname="deck2" deck="2" visibility="not deck 4 rightdeck"/>
<panel class="DECK_CONTAINER_PERFORMANCE_BODY" x="+1920-2-878-77-2" panelname="deck4" deck="4" visibility="deck 4 rightdeck"/>
```

## src/components/containers/bottombar/panel.xml

Original line 31:

```xml
bg
<visual x="+0" y="+0" width="335" height="38" visibility="0.2">
<off shape="square" color="color_tag_mix" border_size="1" border="color_tag_mix" radius="0"/>
</visual>
<visual class="gfx_shape" x="+0" y="+0" width="335" height="2" coloroff="color_tag_mix" visibility="0.5"/>
<visual class="gfx_shape" x="+0" y="+34" width="335" height="2" coloroff="color_tag_mix" visibility="0.5"/>
label
<visual x="+0" y="+0" width="335" height="38" visibility="0.2">
```

Original line 51:

```xml
bg
<visual x="+0" y="+0" width="+26+66+15+2+50+2+58" height="38" visibility="0.2">
<off shape="square" color="color_tag_timing" border_size="1" border="color_tag_timing" radius="0"/>
</visual>
<visual class="gfx_shape" x="+0" y="+0" width="+26+66+15+2+50+2+58" height="2" coloroff="color_tag_timing" visibility="0.5"/>
label
```

Original line 68:

```xml
<visual x="+0" y="+0" width="+26+66+15+2+50+2+58" height="38" visibility="0.2">
<off shape="square" color="color_tag_mood" border_size="1" border="color_tag_mood" radius="0"/>
</visual>
<visual class="gfx_shape" x="+0" y="+0" width="+26+66+15+2+50+2+58" height="2" coloroff="color_tag_mood" visibility="0.5"/>
label
```

Original line 118:

```xml
<button class="button_main" x="+494-32+122" y="-2" width="105" height="24" action="automix" textsize="10" textcolor="br_textoff" text="AUTOMIX" coloroff="br_background" coloron="br_automix2" bordersize="0" query="automix ? blink 1200ms"/>
<button class="button_main" x="+494-32+122+105+2" y="-2" width="55" height="24" action="automix_skip" textsize="10" textcolor="br_textoff" text="NEXT" coloroff="br_background" coloron="br_focus" bordersize="0"/>
<button class="button_main" x="+494-32+122+105+2+55+2" y="-2" width="65" height="24" action="switch_sidelist_playlist" textsize="10" textcolor="br_textoff" text="SIDELIST" coloroff="br_background" coloron="br_focus" bordersize="0"/>
<visual class="gfx_shape" x="+494-32+122" y="-2+24-2" width="105" height="2" coloroff="br_automix2"/>
<visual class="gfx_shape" x="+494-32+122+105+2" y="-2+24-2" width="55" height="2" coloroff="br_focus"/>
<visual class="gfx_shape" x="+494-32+122+105+2+55+2" y="-2+24-2" width="65" height="2" coloroff="br_focus"/>
```

Original line 126:

```xml
<button class="button_main" x="+1" y="+1" width="81" height="40" action="show_splitpanel 'sideview' toggle &amp; sideview 'remixes'" textsize="10" textcolor="br_textoff" text="SIDEPANEL" brcoloroff="#222222" coloroff="#111111" coloron="#660099" colorover="#222222" bordersize="1" radius="3"/>
karaoke
```

## src/components/containers/topbar/panel.xml

Original line 72:

```xml
<button tooltip="BORDER MODE\nShow or hide the active deck border." class="button_main" x="+30" action="toggle '@$dd_bordermode'" width="26" height="27" textsize="12" textcoloron="needle" text="B" coloroff="panel_background" coloron="#222222" bordersize="0"/>
<button tooltip="BROWSER ZOOM\nToggle browser zoom mode." class="button_main" x="+0" action="browser_zoom" width="70" height="42" textsize="12" textcoloron="needle" text="LIBRARY" coloroff="#101010" coloron="#222222" bordersize="0"/>
<button tooltip="" class="button_main" x="+122" action="setting 'showLyrics'" width="60" height="27" textsize="12" textcoloron="needle" text="LYRICS" coloroff="#101010" coloron="#222222" bordersize="0"/>
<button tooltip="SAMPLE PADS\nToggle sample pads." class="button_main" x="+125" action="sideview_triggerpad 'sideview' &amp; sideview_triggerpad &amp; show_splitpanel 'sideview'" width="70" height="27" textsize="12" textcoloron="needle" text="SAMPLES" coloroff="#101010" coloron="#222222" bordersize="0" query=""/>
```

Original line 147:

```xml
SETTINGS BUTTON
<button action="settings" x="+180">
<size width="42" height="27"/>
<off color="#000000"/>
<over color="#222222"/>
<icon sysicon="settings" width="25" height="25" coloroff="#CCCCCC" colorover="#FFFFFF"/>
</button>
```
