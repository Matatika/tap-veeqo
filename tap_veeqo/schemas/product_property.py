"""Schema definitions for product property objects.

Copyright (c) 2026 Meltano.
"""

from singer_sdk import typing as th

ProductPropertyObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
)
