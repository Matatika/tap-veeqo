from singer_sdk import typing as th

from tap_veeqo.schemas import CustomObject, NullType
from tap_veeqo.schemas.inventory import InventoryObject
from tap_veeqo.schemas.store import StoreObject
from tap_veeqo.schemas.warehouse import WarehouseObject


class _ProductObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("title", th.StringType),
        th.Property("weight", th.NumberType),
        th.Property("origin_country", th.StringType),
        th.Property("hs_tariff_number", th.StringType),
        th.Property("tax_rate", th.NumberType),
        th.Property("estimated_delivery", NullType),
        th.Property("deleted_at", th.DateTimeType),
        th.Property("deleted_by_id", th.IntegerType),
        th.Property("description", th.StringType),
        th.Property("main_image_src", th.URIType),
    )


class _StockEntryObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("sellable_id", th.IntegerType),
        th.Property("warehouse_id", th.IntegerType),
        th.Property("infinite", th.BooleanType),
        th.Property("allocated_stock_level", th.IntegerType),
        th.Property("stock_running_low", th.BooleanType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("incoming_stock_level", th.IntegerType),
        th.Property("transit_outgoing_stock_level", th.IntegerType),
        th.Property("warehouse", WarehouseObject),
        th.Property("physical_stock_level", th.IntegerType),
        th.Property("available_stock_level", th.IntegerType),
        th.Property("sellable_on_hand_value", th.NumberType),
        th.Property("transit_incoming_stock_level", th.IntegerType),
        th.Property("location", NullType),
    )


class _VariantPropertySpecificObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("product_specific_id", th.IntegerType),
        th.Property("product_property_id", th.IntegerType),
        th.Property("product_property_name", th.StringType),
        th.Property("value", th.StringType),
    )


class _MeasurementAttributesObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("width", th.NumberType),
        th.Property("height", th.NumberType),
        th.Property("depth", th.NumberType),
        th.Property("dimensions_unit", th.StringType),  # cm
    )


class ChannelSellableObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("remote_title", th.StringType),
        th.Property("remote_sku", th.StringType),
        th.Property("remote_price", th.NumberType),
        th.Property("remote_grams", th.StringType),
        th.Property("remote_profit", th.NumberType),
        th.Property("remote_margin", th.NumberType),
        th.Property("currency_code", th.StringType),
        th.Property("channel_product_id", th.IntegerType),
        th.Property("channel_product_remote_title", th.StringType),
        th.Property("channel_product_status", th.StringType),  # pulled
        th.Property("sellable_id", th.IntegerType),
        th.Property("image_url", th.URIType),
        th.Property("url", th.URIType),
        th.Property("failures", th.ArrayType(th.ObjectType())),
        th.Property("channel", StoreObject),
    )


class SellableObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("awaiting_stock_orders_count", th.IntegerType),
        th.Property("backorder_quantity", th.IntegerType),
        th.Property("total_quantity_sold", th.IntegerType),
        th.Property("requires_review", th.BooleanType),
        th.Property("allocated_stock_level_at_all_warehouses", th.IntegerType),
        th.Property("id", th.IntegerType),
        th.Property("type", th.StringType),  # ProductVariant
        th.Property("title", th.StringType),
        th.Property("sku_code", th.StringType),
        th.Property("upc_code", th.StringType),
        th.Property("model_number", th.StringType),
        th.Property("price", th.NumberType),
        th.Property("cost_price", th.NumberType),
        th.Property("min_reorder_level", th.IntegerType),
        th.Property("quantity_to_reorder", th.IntegerType),
        th.Property("created_by_id", th.IntegerType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("weight_grams", th.NumberType),
        th.Property("weight_unit", th.StringType),  # g, kg
        th.Property("product_title", th.StringType),
        th.Property("full_title", th.StringType),
        th.Property("sellable_title", th.StringType),
        th.Property("profit", th.NumberType),
        th.Property("margin", th.NumberType),
        th.Property("tax_rate", th.NumberType),
        th.Property("estimated_delivery", NullType),
        th.Property("origin_country", th.StringType),
        th.Property("hs_tariff_number", th.StringType),
        th.Property("customs_description", th.StringType),
        th.Property("image_url", th.URIType),
        th.Property("product", _ProductObject),
        th.Property("reorders", th.ArrayType(th.ObjectType())),
        th.Property("stock_entries", th.ArrayType(_StockEntryObject)),
        th.Property(
            "variant_option_specifics", th.ArrayType(_VariantPropertySpecificObject)
        ),
        th.Property(
            "variant_property_specifics",
            th.ArrayType(_VariantPropertySpecificObject),
        ),
        th.Property("images", th.ArrayType(th.URIType)),
        th.Property("measurement_attributes", _MeasurementAttributesObject),
        th.Property("main_thumbnail_url", th.URIType),
        th.Property("available_stock_level_at_all_warehouses", th.IntegerType),
        th.Property("stock_level_at_all_warehouses", th.IntegerType),
        th.Property("inventory", InventoryObject),
        th.Property("weight", th.NumberType),
        th.Property("active_channels", th.ArrayType(StoreObject)),
        th.Property("channel_sellables", th.ArrayType(ChannelSellableObject)),
        th.Property("on_hand_value", th.NumberType),
    )
