from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_veeqo.schemas import CustomObject


class DeliveryMethodObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("cost", StringType),
        Property("name", StringType),
        Property("user_id", IntegerType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("deleted_at", DateTimeType),
        Property("deleted_by_id", IntegerType),
    )
