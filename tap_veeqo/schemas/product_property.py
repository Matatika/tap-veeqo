"""Schema definitions for product property objects."""

from singer_sdk import typing as th

ProductPropertyObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
)
