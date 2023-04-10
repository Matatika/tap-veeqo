"""Veeqo tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_veeqo import streams


class TapVeeqo(Tap):
    """Veeqo tap class."""

    name = "tap-veeqo"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,
            description="API key",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.VeeqoStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.GroupsStream(self),
            streams.UsersStream(self),
        ]


if __name__ == "__main__":
    TapVeeqo.cli()
