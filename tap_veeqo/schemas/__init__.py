"""Schema definitions for tap-veeqo."""

from singer_sdk import typing as th
from typing_extensions import override


class NullType(th.JSONTypeHelper):
    """`null` type."""

    @th.DefaultInstanceProperty
    @override
    def type_dict(self):
        return {
            "type": ["null"],
        }
