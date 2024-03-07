"""Schema definitions for tap-veeqo."""

from singer_sdk import typing as th
from typing_extensions import override


class CustomObject(th.JSONTypeHelper):
    """Custom object."""

    properties: th.PropertiesList

    @th.DefaultInstanceProperty
    @override
    def type_dict(cls):
        return cls.properties.to_dict()

    @th.DefaultInstanceProperty
    def schema(cls):  # noqa: D102
        return cls.type_dict


class NullType(th.JSONTypeHelper):
    @th.DefaultInstanceProperty
    @override
    def type_dict(self):
        return {
            "type": ["null"],
        }
