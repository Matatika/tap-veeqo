from singer_sdk import typing as th

from tap_veeqo.schemas import CustomObject


class ProductBrandObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("display_position", th.IntegerType),
        th.Property("products_count", th.IntegerType),
    )
