from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    EmailType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
    URIType,
)

from tap_veeqo.schemas import CustomObject, NullType
from tap_veeqo.schemas.warehouse import WarehouseObject


class _Api2CartChannelSpecficObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("url", URIType),
        Property("api2cart_store_key", StringType),
        Property("bridge_verified", BooleanType),
        Property("bridge_url", URIType),
        Property("channel_id", IntegerType),
        Property("multi_store", BooleanType),
        Property("additional_api2cart_sites", ArrayType(ObjectType())),
    )


class _ChannelWarehouseObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("active", BooleanType),
        Property("rank", IntegerType),
        Property("warehouse", WarehouseObject),
    )


class StoreObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("type_code", StringType),
        Property("created_by_id", IntegerType),
        Property("name", StringType),
        Property("short_name", StringType),
        Property("currency_code", StringType),
        Property("state", StringType),  # active
        Property("url", URIType),
        Property("shopify_url", URIType),
        Property("shopify_multi_location", NullType),
        Property("shopify_pull_orders_fraud_info", NullType),
        Property("shopify_pull_order_edits", NullType),
        Property("shopify_import_hs_code_and_country_of_origin", NullType),
        Property("ebay_url", URIType),
        Property("ebay_site_code_id", IntegerType),
        Property("country", StringType),
        Property("region", StringType),
        Property("city", StringType),
        Property("address_line_1", StringType),
        Property("address_line_2", StringType),
        Property("post_code", StringType),
        Property("pulled_products_at", DateTimeType),
        Property("pulled_orders_at", DateTimeType),
        Property("pulled_stock_level_at", DateTimeType),
        Property("seller_id", IntegerType),
        Property("marketplace_id", IntegerType),
        Property("mws_auth_token", StringType),
        Property("deleted_at", DateTimeType),
        Property("deleted_by_id", IntegerType),
        Property("api2cart_store_key", StringType),
        Property("bridge_url", URIType),
        Property("bridge_verified", BooleanType),
        Property("pull_pending_orders", BooleanType),
        Property("default_send_shipment_email", BooleanType),
        Property("automatic_product_linking_disabled", BooleanType),
        Property("update_remote_order", BooleanType),
        Property("successfully_fetched_stock_levels_at", DateTimeType),
        Property("create_product_if_unmatched", BooleanType),
        Property("skip_title_matching", BooleanType),
        Property("email", EmailType),
        Property("skip_fba_orders_and_products", BooleanType),
        Property("pull_stock_level_required", BooleanType),
        Property("pull_product_properties", BooleanType),
        Property("pull_historical_orders", BooleanType),
        Property("adjust_orders_tax_rate", NullType),
        Property("send_notification_emails_to_customers", BooleanType),
        Property("end_ebay_listing_on_out_of_stock", BooleanType),
        Property("update_product_attributes", BooleanType),
        Property("max_qty_to_advert", IntegerType),
        Property("min_threshold_qty", IntegerType),
        Property("percent_of_qty", IntegerType),
        Property("always_set_qty", IntegerType),
        Property("veeqo_dictates_stock_level", BooleanType),
        Property("with_fba", BooleanType),
        Property("first_sync_finish_notice_marked_as_read", BooleanType),
        Property("pull_unpaid_shopify_orders", BooleanType),
        Property("create_product_on_ended_listings", BooleanType),
        Property("link_to_products_linked_to_current_channel", BooleanType),
        Property("link_with_similar_listings_by_sku", BooleanType),
        Property("weight_unit", StringType),  # g, kg
        Property("import_cost_price", BooleanType),
        Property("veeqo_dictates_price", BooleanType),
        Property("keep_inventory_tracking_value", BooleanType),
        Property("marketplace_country", NullType),
        Property("time_zone", StringType),
        Property("time_zone_offset", NullType),
        Property("amazon_fulfillment_enabled", BooleanType),
        Property("import_product_tags", BooleanType),
        Property("import_product_brands", BooleanType),
        Property("token", StringType),
        Property("import_additional_payment_details", BooleanType),
        Property("import_order_tags", BooleanType),
        Property("authorized_at_remote_store", BooleanType),
        Property("pull_product_images", BooleanType),
        Property("routing_order_type", IntegerType),
        Property("channel_setup_id", IntegerType),
        Property("is_master", BooleanType),
        Property("warehouse", WarehouseObject),
        Property("warehouses", ArrayType(WarehouseObject)),
        Property("stock_level_update_requests", ArrayType(ObjectType())),
        Property("amazon_fulfillment_setting", NullType),
        Property("amazon_channel_specific", NullType),
        Property("api2cart_channel_specific", _Api2CartChannelSpecficObject),
        Property("additional_api2cart_site", NullType),
        Property("channel_warehouses", ArrayType(_ChannelWarehouseObject)),
        Property("channel_ranked_warehouses", ArrayType(_ChannelWarehouseObject)),
        Property("channel_near_warehouses", ArrayType(_ChannelWarehouseObject)),
        Property("time_since_product_sync", StringType),
        Property("time_since_order_sync", StringType),
        Property("time_since_tried_fetch_stock_level", StringType),
        Property("time_since_successfully_fetch_stock_level", StringType),
        Property("default_warehouse", WarehouseObject),
        Property("remote", BooleanType),
        Property("channel_oauth_refresh_token_expires_at", NullType),
        Property("disabled_push_of_stock_level", BooleanType),
        Property("remote_warehouses_exist", BooleanType),
    )
