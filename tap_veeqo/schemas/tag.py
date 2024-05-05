"""Schema definitions for tag objects."""

from singer_sdk import typing as th

TagObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("colour", th.StringType),
    th.Property("company_id", th.IntegerType),
    th.Property("taggings_count", th.IntegerType),
    th.Property("deleted_at", th.DateTimeType),
    th.Property("deleted_by_id", th.IntegerType),
)
