# VirtualDJ Skin Reference Notes

These notes capture behavior verified in this skin project where the official VirtualDJ documentation is terse or easy to misread.

## Define Placeholders And `*`

Official docs describe `*placeholder` as enabling simple math, but runtime testing showed a broader practical rule:

- Use `*name` for any placeholder that must be substituted inside VDJ Script expressions, `condition` attributes, or text strings.
- Unstarred placeholders may work for simple XML attribute replacement, but they can remain literal in script/text contexts.
- Boolean-style placeholders should be declared with a star when used in conditions.

Observed with the canary in `src/prototypes/mirror-condition-canary.xml`:

```xml
<define class="STRING_CONDITION_CANARY" placeholders="side=false">
  <textzone text="[SIDE]"/>
  <group condition="param_equal '[SIDE]' 'true'"/>
</define>
```

`[SIDE]` stayed literal and did not drive conditions.

This version worked:

```xml
<define class="STRING_CONDITION_CANARY" placeholders="*side=false">
  <textzone text="[SIDE]"/>
  <group condition="param_equal '[SIDE]' 'true'"/>
</define>
```

So for production code, prefer:

```xml
<define class="TRACK_MODIFIERS_PANEL" placeholders="*mirror=false">
  <group condition="not [MIRROR]"/>
  <group condition="[MIRROR]"/>
</define>
```

Called as:

```xml
<panel class="track_modifiers_panel" mirror="false"/>
<panel class="track_modifiers_panel" mirror="true"/>
```

Numeric starred placeholders also work:

```xml
<define class="EXAMPLE" placeholders="*flip=0">
  <group condition="param_equal [FLIP] 0"/>
  <group condition="param_equal [FLIP] 1"/>
</define>
```

## String Comparisons

When comparing placeholder values as strings, quote the placeholder expansion and the target value:

```xml
condition="param_equal '[MIRROR]' 'true'"
```

For boolean-like placeholders declared with `*`, direct boolean conditions also worked:

```xml
condition="[MIRROR]"
condition="not [MIRROR]"
```

Use direct boolean conditions only when the placeholder value is exactly `true` or `false`.

## Conditional Group Positioning

For `<group>`, put `x` and `y` directly on the group node. Do not rely on conditional child `<pos>` elements for group placement.

Verified working:

```xml
<group x="+0" y="+5" condition="not [MIRROR]">
  ...
</group>
<group x="+265" y="+5" condition="[MIRROR]">
  ...
</group>
```

Observed as fragile/non-working:

```xml
<group>
  <pos x="+0" y="+5" condition="not [MIRROR]"/>
  <pos x="+265" y="+5" condition="[MIRROR]"/>
  ...
</group>
```

In the canary, the child-`<pos>` group rendered but did not move horizontally, while equivalent `condition` branches on groups with direct `x`/`y` behaved correctly.

## Official Docs

- VirtualDJ Skin Define: https://www.virtualdj.com/wiki/Skin%20Define.html
- VirtualDJ Skin Element Positioning: https://www.virtualdj.com/wiki/Skin%20Element%20Positioning.html
- VirtualDJ Skin Element Properties: https://www.virtualdj.com/wiki/Skin%20Element%20Properties.html
