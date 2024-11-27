"""Schema definitions for variant property specific objects."""

from singer_sdk import typing as th

VariantPropertySpecificObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("product_specific_id", th.IntegerType),
    th.Property("product_property_id", th.IntegerType),
    th.Property("product_property_name", th.StringType),
    th.Property("value", th.StringType),
)
