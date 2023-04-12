from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_veeqo.schemas import CustomObject


class TagObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("name", StringType),
        Property("colour", StringType),
        Property("company_id", IntegerType),
        Property("taggings_count", IntegerType),
        Property("deleted_at", DateTimeType),
        Property("deleted_by_id", IntegerType),
    )
