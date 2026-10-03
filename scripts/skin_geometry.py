"""Shared dimensions for generated waveform and browser position tables.

Keep expression terms explicit in the generated XML for runtime diagnostics.
Layout-specific base offsets belong in the generator, not in this data module.
"""

WAVE_SIZE_COUNT = 14
WAVE_STEP = 20
WAVE_HEIGHT_MIN = 121
WAVE_OFFSET_MIN = 7
RACK_GAP = 2
RACK_HEIGHTS = {"fx": 80, "mixer": 86, "video": 140}

# Most-specific first: a shorter condition also matches supersets of its racks.
# Retain the original condition order to keep generated XML diffs stable.
RACK_STATES = (
    ("fx", "mixer", "video"),
    ("mixer", "video"),
    ("fx", "video"),
    ("mixer", "fx"),
    ("video",),
    ("mixer",),
    ("fx",),
    (),
)


def wave_sizes():
    """Yield (state, offset, height), largest first as in the original tables."""
    for state in range(WAVE_SIZE_COUNT - 1, -1, -1):
        yield state, WAVE_OFFSET_MIN + state * WAVE_STEP, WAVE_HEIGHT_MIN + state * WAVE_STEP


def rack_combinations(*, stack=False):
    """Yield condition, added y terms, subtracted height terms for every state."""
    order = tuple(reversed(RACK_HEIGHTS)) if stack else tuple(RACK_HEIGHTS)
    for active in RACK_STATES:
        terms = [rack for rack in order if rack in active]
        checks = terms if stack else active
        condition = " ? ".join(f"var_equal '@$dd_show_{rack}_rack' 1" for rack in checks)
        added = "".join(f"+{RACK_HEIGHTS[rack]}+{RACK_GAP}" for rack in terms)
        removed = "".join(f"-{RACK_HEIGHTS[rack]}-{RACK_GAP}" for rack in terms)
        yield condition, added, removed


# --- Rack fit guard ---------------------------------------------------------
#
# The smallest browser the skin accepts. Pro mixer two-deck at wave size 13 with
# no racks leaves 126px; rack toggles refuse to go below this.
BROWSER_MIN_HEIGHT = 120

# Browser height available before the wave term (121 + 20*n) and rack terms
# (height + gap each) are subtracted, per rack-aware surface. The literals mirror
# the layout callers so a changed caller fails the geometry tests here.
PRO_MIXER_BROWSER = 1075 - 568                        # layouts/pro/waves.xml, DECKS_ABOVE
PRO_EXTENDED_BROWSER = (1080 - 60 - 2 - 2 - 2 - 1 - 50) - 344  # waves above (8px less than below)
PERFORMANCE_4DECK_BROWSER = 1080 - 43 - 2 - 333 - 2 - 2 - 333 - 2 - 50  # fixed, no wave term


def rack_fit_limit(available, wave_dependent, racks):
    """Wave states that keep BROWSER_MIN_HEIGHT with `racks` shown.

    Returns None when every wave size fits, 0 when none does, otherwise the
    first wave state that no longer fits (states below it fit).
    """
    room = available - BROWSER_MIN_HEIGHT - sum(RACK_HEIGHTS[r] + RACK_GAP for r in racks)
    if not wave_dependent:
        return None if room >= 0 else 0
    room -= WAVE_HEIGHT_MIN
    if room < 0:
        return 0
    limit = room // WAVE_STEP + 1
    return None if limit >= WAVE_SIZE_COUNT else limit


def _fit_leaf(available, wave_dependent, racks, yes, no):
    limit = rack_fit_limit(available, wave_dependent, racks)
    if limit is None:
        return yes
    if limit == 0:
        return no
    return f"var_smaller '@$dd_wave_size' {limit} ? {yes} : {no}"


def rack_fit_script(rack, *, single, yes="true", no="false"):
    """VDJScript that runs/returns `yes` when showing `rack` keeps BROWSER_MIN_HEIGHT.

    VDJScript conditions are single statements, so a guard cannot be computed
    and then tested; instead `yes`/`no` are placed at every leaf of the decision
    tree (an action with `no="nothing"`, or `true`/`false` for a visibility).
    `single` is rack mode 1 (other racks are cleared first); otherwise the tree
    reads the other racks' current state. Contexts that never overflow run `yes`.
    """
    def context(available, wave_dependent):
        if single:
            return _fit_leaf(available, wave_dependent, (rack,), yes, no)
        o1, o2 = [r for r in RACK_HEIGHTS if r != rack]
        leaf = lambda *others: _fit_leaf(available, wave_dependent, (rack, *others), yes, no)
        return (f"var_equal '@$dd_show_{o1}_rack' 1 ? "
                f"var_equal '@$dd_show_{o2}_rack' 1 ? {leaf(o1, o2)} : {leaf(o1)} : "
                f"var_equal '@$dd_show_{o2}_rack' 1 ? {leaf(o2)} : {leaf()}")

    pro_mixer = context(PRO_MIXER_BROWSER, True)
    pro_extended = context(PRO_EXTENDED_BROWSER, True)
    performance_4deck = context(PERFORMANCE_4DECK_BROWSER, False)
    # Pro mixer two-deck shows the rack band only with the main waves above the
    # decks; Pro extended shows it with waves above or below (the smaller height
    # is used for both). Performance four-deck has a fixed browser.
    pro = (f"var_equal '@$dd_layout_4deck' 0 ? var_equal '@$dd_hide_main_waveforms' 0 ? "
           f"var_equal '@$dd_hide_pro_mixer' 0 ? var_equal '@$dd_waveform_position' 0 ? {pro_mixer} : {yes} "
           f": {pro_extended} : {yes} : {yes}")
    performance = f"var_equal '@$dd_layout_4deck' 1 ? {performance_4deck} : {yes}"
    return (f"var_equal '@$dd_skin_mode' 0 ? {pro} : "
            f"var_equal '@$dd_skin_mode' 1 ? {performance} : {yes}")


# --- LED VU meters ----------------------------------------------------------
LED_PITCH = 6
LED_HEIGHT = 4
# class -> (led count, needle-colored top LEDs, alt-color red / orange counts)
VU_METERS = {
    "VU_METER_LEDS": dict(leds=26, needle=2, red=2, orange=4),
    "VU_METER_LEDS_MINI": dict(leds=10, needle=2, red=1, orange=2),
    "VU_METER_LEDS_STACK": dict(leds=21, needle=2, red=2, orange=3),
}


def vu_meter_height(leds):
    return (leds - 1) * LED_PITCH + LED_HEIGHT
