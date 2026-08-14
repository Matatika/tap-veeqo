"""Schema definitions for product brand objects.

Copyright (c) 2026 Meltano.
"""

from singer_sdk import typing as th

ProductBrandObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("display_position", th.IntegerType),
    th.Property("products_count", th.IntegerType),
)
