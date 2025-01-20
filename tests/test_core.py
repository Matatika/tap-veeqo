"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_veeqo.tap import TapVeeqo

SAMPLE_CONFIG = {}


# Run standard built-in tap tests from the SDK:
TestTapTrello = get_tap_test_class(
    tap_class=TapVeeqo,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(
        ignore_no_records_for_streams=[
            "product_option_specifics",
            "product_properties",
            "product_property_specifics",
            "variant_property_specifics",
        ]
    ),
)
