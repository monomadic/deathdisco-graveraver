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
