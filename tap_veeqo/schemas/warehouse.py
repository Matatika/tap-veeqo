"""Schema definitions for warehouse objects."""

from singer_sdk import typing as th

from tap_veeqo.schemas import NullType

WarehouseObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("user_id", NullType),
    th.Property("address_line_1", th.StringType),
    th.Property("address_line_2", th.StringType),
    th.Property("city", th.StringType),
    th.Property("region", th.StringType),
    th.Property("country", th.StringType),
    th.Property("post_code", th.StringType),
    th.Property("inventory_type_code", th.StringType),
    th.Property("default_min_reorder", th.IntegerType),
    th.Property("click_and_collect_enabled", th.BooleanType),
    th.Property("click_and_collect_days", th.StringType),
    th.Property("created_by_id", th.IntegerType),
    th.Property("updated_by_id", th.IntegerType),
    th.Property("deleted_at", th.DateTimeType),
    th.Property("deleted_by_id", th.IntegerType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("phone", th.StringType),
    th.Property("requested_carrier_account", th.BooleanType),
    th.Property("display_position", th.IntegerType),
    th.Property("lat", th.StringType),
    th.Property("lng", th.StringType),
    th.Property("trading_name", th.StringType),
    th.Property("company_id", th.IntegerType),
    th.Property("eori_id", th.StringType),
    th.Property("ioss_id", th.StringType),
    th.Property("letterbox_address_id", th.UUIDType),
    th.Property("letterbox_address_status", th.StringType),  # READY
    th.Property("tax_id", th.StringType),
    th.Property("cut_off_times_enabled", th.BooleanType),
    th.Property("cut_off_times", NullType),
    th.Property("uk_ims_id", th.StringType),
    th.Property("sortinghat_warehouse_id", th.UUIDType),
    th.Property("cached_time_zone", th.StringType),
)
