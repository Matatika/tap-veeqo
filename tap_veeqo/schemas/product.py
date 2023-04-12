from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    PropertiesList,
    Property,
    StringType,
    URIType,
)

from tap_veeqo.schemas import CustomObject, NullType
from tap_veeqo.schemas.inventory import InventoryObject
from tap_veeqo.schemas.product_brand import ProductBrandObject
from tap_veeqo.schemas.sellable import ChannelSellableObject, SellableObject
from tap_veeqo.schemas.store import StoreObject
from tap_veeqo.schemas.tag import TagObject


class _ChannelProductObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("remote_title", StringType),
        Property("remote_description", StringType),
        Property("remote_id", StringType),
        Property("channel_type_code", StringType),
        Property("channel_short_name", StringType),
        Property("inactive_after", DateTimeType),
        Property("channel", StoreObject),
        Property("status", StringType),  # pulled
        Property("channel_sellables", ArrayType(ChannelSellableObject)),
    )


class ProductObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("title", StringType),
        Property("created_by_id", IntegerType),
        Property("created_at", DateTimeType),
        Property("weight", NumberType),
        Property("origin_country", StringType),
        Property("deleted_by_id", IntegerType),
        Property("deleted_at", DateTimeType),
        Property("hs_tariff_number", StringType),
        Property("notes", StringType),
        Property("product_tax_rate_id", IntegerType),
        Property("tax_rate", NumberType),
        Property("updated_by_id", IntegerType),
        Property("updated_at", DateTimeType),
        Property("web_meta_description", StringType),
        Property("web_meta_keywords", StringType),
        Property("web_meta_title", StringType),
        Property("web_page_title", StringType),
        Property("web_page_url", StringType),
        Property("estimated_delivery", NullType),
        Property("total_quantity_sold", IntegerType),
        Property("requires_review", BooleanType),
        Property("main_image", URIType),
        Property("brand", ProductBrandObject),
        Property("sellables", ArrayType(SellableObject)),
        Property("channel_products", ArrayType(_ChannelProductObject)),
        Property("active_channels", ArrayType(StoreObject)),
        Property("tags", ArrayType(TagObject)),
        Property("image", URIType),
        Property("thumbnail_url", URIType),
        Property("description", StringType),
        Property("on_hand_value", NumberType),
        Property("main_image_src", URIType),
        Property("total_allocated_stock_level", IntegerType),
        Property("total_available_stock_level", IntegerType),
        Property("total_stock_level", IntegerType),
        Property("inventory", InventoryObject),
    )
