"""Schema definitions for user objects.

Copyright (c) 2026 Meltano.
"""

from singer_sdk import typing as th

UserObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("email", th.EmailType),
)
