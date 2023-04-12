from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_veeqo.schemas import CustomObject, NullType


class WarehouseObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("name", StringType),
        Property("user_id", NullType),
        Property("address_line_1", StringType),
        Property("address_line_2", StringType),
        Property("city", StringType),
        Property("region", StringType),
        Property("country", StringType),
        Property("post_code", StringType),
        Property("inventory_type_code", StringType),
        Property("default_min_reorder", IntegerType),
        Property("click_and_collect_enabled", BooleanType),
        Property("click_and_collect_days", StringType),
        Property("created_by_id", IntegerType),
        Property("updated_by_id", IntegerType),
        Property("deleted_at", DateTimeType),
        Property("deleted_by_id", IntegerType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("phone", StringType),
        Property("requested_carrier_account", BooleanType),
        Property("display_position", IntegerType),
        Property("lat", StringType),
        Property("lng", StringType),
        Property("trading_name", StringType),
        Property("company_id", IntegerType),
        Property("eori_id", StringType),
        Property("ioss_id", StringType),
    )
