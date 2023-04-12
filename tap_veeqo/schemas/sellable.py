from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
    URIType,
)

from tap_veeqo.schemas import CustomObject, NullType
from tap_veeqo.schemas.inventory import InventoryObject
from tap_veeqo.schemas.store import StoreObject
from tap_veeqo.schemas.warehouse import WarehouseObject


class _ProductObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("title", StringType),
        Property("weight", NumberType),
        Property("origin_country", StringType),
        Property("hs_tariff_number", StringType),
        Property("tax_rate", NumberType),
        Property("estimated_delivery", NullType),
        Property("deleted_at", DateTimeType),
        Property("deleted_by_id", IntegerType),
        Property("description", StringType),
        Property("main_image_src", URIType),
    )


class _StockEntryObject(CustomObject):
    properties = PropertiesList(
        Property("sellable_id", IntegerType),
        Property("warehouse_id", IntegerType),
        Property("infinite", BooleanType),
        Property("allocated_stock_level", IntegerType),
        Property("stock_running_low", BooleanType),
        Property("updated_at", DateTimeType),
        Property("incoming_stock_level", IntegerType),
        Property("transit_outgoing_stock_level", IntegerType),
        Property("warehouse", WarehouseObject),
        Property("physical_stock_level", IntegerType),
        Property("available_stock_level", IntegerType),
        Property("sellable_on_hand_value", NumberType),
        Property("transit_incoming_stock_level", IntegerType),
        Property("location", NullType),
    )


class _VariantPropertySpecificObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("product_specific_id", IntegerType),
        Property("product_property_id", IntegerType),
        Property("product_property_name", StringType),
        Property("value", StringType),
    )


class _MeasurementAttributesObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("width", NumberType),
        Property("height", NumberType),
        Property("depth", NumberType),
        Property("dimensions_unit", StringType),  # cm
    )


class ChannelSellableObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("remote_title", StringType),
        Property("remote_sku", StringType),
        Property("remote_price", NumberType),
        Property("remote_grams", StringType),
        Property("remote_profit", NumberType),
        Property("remote_margin", NumberType),
        Property("currency_code", StringType),
        Property("channel_product_id", IntegerType),
        Property("channel_product_remote_title", StringType),
        Property("channel_product_status", StringType),  # pulled
        Property("sellable_id", IntegerType),
        Property("image_url", URIType),
        Property("url", URIType),
        Property("failures", ArrayType(ObjectType())),
        Property("channel", StoreObject),
    )


class SellableObject(CustomObject):
    properties = PropertiesList(
        Property("awaiting_stock_orders_count", IntegerType),
        Property("backorder_quantity", IntegerType),
        Property("total_quantity_sold", IntegerType),
        Property("requires_review", BooleanType),
        Property("allocated_stock_level_at_all_warehouses", IntegerType),
        Property("id", IntegerType),
        Property("type", StringType),  # ProductVariant
        Property("title", StringType),
        Property("sku_code", StringType),
        Property("upc_code", StringType),
        Property("model_number", StringType),
        Property("price", NumberType),
        Property("cost_price", NumberType),
        Property("min_reorder_level", IntegerType),
        Property("quantity_to_reorder", IntegerType),
        Property("created_by_id", IntegerType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("weight_grams", NumberType),
        Property("weight_unit", StringType),  # g, kg
        Property("product_title", StringType),
        Property("full_title", StringType),
        Property("sellable_title", StringType),
        Property("profit", NumberType),
        Property("margin", NumberType),
        Property("tax_rate", NumberType),
        Property("estimated_delivery", NullType),
        Property("origin_country", StringType),
        Property("hs_tariff_number", StringType),
        Property("customs_description", StringType),
        Property("image_url", URIType),
        Property("product", _ProductObject),
        Property("reorders", ArrayType(ObjectType())),
        Property("stock_entries", ArrayType(_StockEntryObject)),
        Property("variant_option_specifics", ArrayType(_VariantPropertySpecificObject)),
        Property(
            "variant_property_specifics",
            ArrayType(_VariantPropertySpecificObject),
        ),
        Property("images", ArrayType(URIType)),
        Property("measurement_attributes", _MeasurementAttributesObject),
        Property("main_thumbnail_url", URIType),
        Property("available_stock_level_at_all_warehouses", IntegerType),
        Property("stock_level_at_all_warehouses", IntegerType),
        Property("inventory", InventoryObject),
        Property("weight", NumberType),
        Property("active_channels", ArrayType(StoreObject)),
        Property("channel_sellables", ArrayType(ChannelSellableObject)),
        Property("on_hand_value", NumberType),
    )
