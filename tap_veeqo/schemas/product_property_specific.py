"""Schema definitions for product property specific objects."""

from singer_sdk import typing as th

ProductPropertySpecificObject = th.PropertiesList(
    th.Property("product_id", th.IntegerType),  # from context
    th.Property("id", th.IntegerType),
    th.Property("product_property_id", th.IntegerType),
    th.Property("product_property_name", th.StringType),
    th.Property("value", th.StringType),
)
