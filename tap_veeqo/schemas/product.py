from singer_sdk import typing as th

from tap_veeqo.schemas import CustomObject, NullType
from tap_veeqo.schemas.inventory import InventoryObject
from tap_veeqo.schemas.product_brand import ProductBrandObject
from tap_veeqo.schemas.sellable import ChannelSellableObject, SellableObject
from tap_veeqo.schemas.store import StoreObject
from tap_veeqo.schemas.tag import TagObject


class _ChannelProductObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("remote_title", th.StringType),
        th.Property("remote_description", th.StringType),
        th.Property("remote_id", th.StringType),
        th.Property("channel_type_code", th.StringType),
        th.Property("channel_short_name", th.StringType),
        th.Property("inactive_after", th.DateTimeType),
        th.Property("channel", StoreObject),
        th.Property("status", th.StringType),  # pulled
        th.Property("channel_sellables", th.ArrayType(ChannelSellableObject)),
    )


class ProductObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("title", th.StringType),
        th.Property("created_by_id", th.IntegerType),
        th.Property("created_at", th.DateTimeType),
        th.Property("weight", th.NumberType),
        th.Property("origin_country", th.StringType),
        th.Property("deleted_by_id", th.IntegerType),
        th.Property("deleted_at", th.DateTimeType),
        th.Property("hs_tariff_number", th.StringType),
        th.Property("notes", th.StringType),
        th.Property("product_tax_rate_id", th.IntegerType),
        th.Property("tax_rate", th.NumberType),
        th.Property("updated_by_id", th.IntegerType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("web_meta_description", th.StringType),
        th.Property("web_meta_keywords", th.StringType),
        th.Property("web_meta_title", th.StringType),
        th.Property("web_page_title", th.StringType),
        th.Property("web_page_url", th.StringType),
        th.Property("estimated_delivery", NullType),
        th.Property("total_quantity_sold", th.IntegerType),
        th.Property("requires_review", th.BooleanType),
        th.Property("main_image", th.URIType),
        th.Property("brand", ProductBrandObject),
        th.Property("sellables", th.ArrayType(SellableObject)),
        th.Property("channel_products", th.ArrayType(_ChannelProductObject)),
        th.Property("active_channels", th.ArrayType(StoreObject)),
        th.Property("tags", th.ArrayType(TagObject)),
        th.Property("image", th.URIType),
        th.Property("thumbnail_url", th.URIType),
        th.Property("description", th.StringType),
        th.Property("on_hand_value", th.NumberType),
        th.Property("main_image_src", th.URIType),
        th.Property("total_allocated_stock_level", th.IntegerType),
        th.Property("total_available_stock_level", th.IntegerType),
        th.Property("total_stock_level", th.IntegerType),
        th.Property("inventory", InventoryObject),
    )
