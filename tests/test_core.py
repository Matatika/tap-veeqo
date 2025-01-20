"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_tap_test_class

from tap_veeqo.tap import TapVeeqo

SAMPLE_CONFIG = {}


# Run standard built-in tap tests from the SDK:
TestTapTrello = get_tap_test_class(
    tap_class=TapVeeqo,
    config=SAMPLE_CONFIG,
)
