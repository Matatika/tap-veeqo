from singer_sdk.typing import IntegerType, PropertiesList, Property, StringType

from tap_veeqo.schemas import CustomObject


class ProductBrandObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("name", StringType),
        Property("display_position", IntegerType),
        Property("products_count", IntegerType),
    )
