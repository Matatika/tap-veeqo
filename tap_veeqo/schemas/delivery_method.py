"""Schema definitions for delivery method objects."""

from singer_sdk import typing as th

from tap_veeqo.schemas import CustomObject


class DeliveryMethodObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("cost", th.StringType),
        th.Property("name", th.StringType),
        th.Property("user_id", th.IntegerType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("deleted_at", th.DateTimeType),
        th.Property("deleted_by_id", th.IntegerType),
    )
