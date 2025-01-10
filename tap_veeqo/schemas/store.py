"""Schema definitions for store objects."""

from singer_sdk import typing as th

from tap_veeqo.schemas import NullType
from tap_veeqo.schemas.warehouse import WarehouseObject

_Api2CartChannelSpecficObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("url", th.URIType),
    th.Property("api2cart_store_key", th.StringType),
    th.Property("bridge_verified", th.BooleanType),
    th.Property("bridge_url", th.URIType),
    th.Property("channel_id", th.IntegerType),
    th.Property("multi_store", th.BooleanType),
    th.Property("additional_api2cart_sites", th.ArrayType(th.ObjectType())),
)


_ChannelWarehouseObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("active", th.BooleanType),
    th.Property("rank", th.IntegerType),
    th.Property("warehouse", WarehouseObject),
)


StoreObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("type_code", th.StringType),
    th.Property("created_by_id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("short_name", th.StringType),
    th.Property("currency_code", th.StringType),
    th.Property("state", th.StringType),  # active
    th.Property("url", th.URIType),
    th.Property("shopify_url", th.URIType),
    th.Property("shopify_multi_location", NullType),
    th.Property("shopify_pull_orders_fraud_info", NullType),
    th.Property("shopify_pull_order_edits", NullType),
    th.Property("shopify_import_hs_code_and_country_of_origin", NullType),
    th.Property("ebay_url", th.URIType),
    th.Property("ebay_site_code_id", th.IntegerType),
    th.Property("country", th.StringType),
    th.Property("region", th.StringType),
    th.Property("city", th.StringType),
    th.Property("address_line_1", th.StringType),
    th.Property("address_line_2", th.StringType),
    th.Property("post_code", th.StringType),
    th.Property("pulled_products_at", th.DateTimeType),
    th.Property("pulled_orders_at", th.DateTimeType),
    th.Property("pulled_stock_level_at", th.DateTimeType),
    th.Property("seller_id", th.IntegerType),
    th.Property("marketplace_id", th.IntegerType),
    th.Property("mws_auth_token", th.StringType),
    th.Property("deleted_at", th.DateTimeType),
    th.Property("deleted_by_id", th.IntegerType),
    th.Property("api2cart_store_key", th.StringType),
    th.Property("bridge_url", th.URIType),
    th.Property("bridge_verified", th.BooleanType),
    th.Property("pull_pending_orders", th.BooleanType),
    th.Property("default_send_shipment_email", th.BooleanType),
    th.Property("automatic_product_linking_disabled", th.BooleanType),
    th.Property("update_remote_order", th.BooleanType),
    th.Property("successfully_fetched_stock_levels_at", th.DateTimeType),
    th.Property("create_product_if_unmatched", th.BooleanType),
    th.Property("skip_title_matching", th.BooleanType),
    th.Property("email", th.EmailType),
    th.Property("skip_fba_orders_and_products", th.BooleanType),
    th.Property("pull_stock_level_required", th.BooleanType),
    th.Property("pull_product_properties", th.BooleanType),
    th.Property("pull_historical_orders", th.BooleanType),
    th.Property("adjust_orders_tax_rate", NullType),
    th.Property("send_notification_emails_to_customers", th.BooleanType),
    th.Property("end_ebay_listing_on_out_of_stock", th.BooleanType),
    th.Property("update_product_attributes", th.BooleanType),
    th.Property("max_qty_to_advert", th.IntegerType),
    th.Property("min_threshold_qty", th.IntegerType),
    th.Property("percent_of_qty", th.IntegerType),
    th.Property("always_set_qty", th.IntegerType),
    th.Property("veeqo_dictates_stock_level", th.BooleanType),
    th.Property("with_fba", th.BooleanType),
    th.Property("first_sync_finish_notice_marked_as_read", th.BooleanType),
    th.Property("pull_unpaid_shopify_orders", th.BooleanType),
    th.Property("create_product_on_ended_listings", th.BooleanType),
    th.Property("link_to_products_linked_to_current_channel", th.BooleanType),
    th.Property("link_with_similar_listings_by_sku", th.BooleanType),
    th.Property("weight_unit", th.StringType),  # g, kg
    th.Property("import_cost_price", th.BooleanType),
    th.Property("veeqo_dictates_price", th.BooleanType),
    th.Property("keep_inventory_tracking_value", th.BooleanType),
    th.Property("marketplace_country", NullType),
    th.Property("time_zone", th.StringType),
    th.Property("time_zone_offset", NullType),
    th.Property("amazon_fulfillment_enabled", th.BooleanType),
    th.Property("import_product_tags", th.BooleanType),
    th.Property("import_product_brands", th.BooleanType),
    th.Property("token", th.StringType),
    th.Property("import_additional_payment_details", th.BooleanType),
    th.Property("import_order_tags", th.BooleanType),
    th.Property("authorized_at_remote_store", th.BooleanType),
    th.Property("pull_product_images", th.BooleanType),
    th.Property("routing_order_type", th.IntegerType),
    th.Property("channel_setup_id", th.IntegerType),
    th.Property("is_master", th.BooleanType),
    th.Property("notify_on_outbound_shipment_date", th.BooleanType),
    th.Property("outbound_shipment_notification_time", th.TimeType),
    th.Property("warehouse", WarehouseObject),
    th.Property("warehouses", th.ArrayType(WarehouseObject)),
    th.Property("stock_level_update_requests", th.ArrayType(th.ObjectType())),
    th.Property("amazon_fulfillment_setting", NullType),
    th.Property("amazon_channel_specific", NullType),
    th.Property("api2cart_channel_specific", _Api2CartChannelSpecficObject),
    th.Property("additional_api2cart_site", NullType),
    th.Property("channel_warehouses", th.ArrayType(_ChannelWarehouseObject)),
    th.Property("channel_ranked_warehouses", th.ArrayType(_ChannelWarehouseObject)),
    th.Property("channel_near_warehouses", th.ArrayType(_ChannelWarehouseObject)),
    th.Property("time_since_product_sync", th.StringType),
    th.Property("time_since_order_sync", th.StringType),
    th.Property("time_since_tried_fetch_stock_level", th.StringType),
    th.Property("time_since_successfully_fetch_stock_level", th.StringType),
    th.Property("default_warehouse", WarehouseObject),
    th.Property("remote", th.BooleanType),
    th.Property("channel_oauth_refresh_token_expires_at", NullType),
    th.Property("disabled_push_of_stock_level", th.BooleanType),
    th.Property("remote_warehouses_exist", th.BooleanType),
)
