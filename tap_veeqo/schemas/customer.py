from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    EmailType,
    IntegerType,
    NumberType,
    PropertiesList,
    Property,
    StringType,
)

from tap_veeqo.schemas import CustomObject, NullType
from tap_veeqo.schemas.address import BillingAddressObject, DeliveryAddressObject


class _ContactObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("first_name", StringType),
        Property("last_name", StringType),
        Property("email", EmailType),
        Property("phone", StringType),
        Property("title", StringType),
        Property("is_default", BooleanType),
        Property("customer_id", IntegerType),
    )


class _AddressObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("first_name", StringType),
        Property("last_name", StringType),
        Property("company", StringType),
        Property("address1", StringType),
        Property("address2", StringType),
        Property("city", StringType),
        Property("country", StringType),
        Property("state", StringType),
        Property("zip", StringType),
        Property("type", StringType),  # BillingAddress, ShippingAddress
        Property("short_name", StringType),
        Property("email", EmailType),
        Property("customer_id", IntegerType),
        Property("phone", StringType),
        Property("editable", BooleanType),
        Property("is_default", NullType),
    )


class _PriceListObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("name", StringType),
        Property("default", NullType),
        Property("currency_code", StringType),
    )


class _ContactDataObject(CustomObject):
    properties = PropertiesList(
        Property("email", EmailType),
        Property("phone", StringType),
    )


class _DeliveryMethodObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("cost", NumberType),
        Property("name", StringType),
    )


class CustomerObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("email", EmailType),
        Property("phone", StringType),
        Property("mobile", StringType),
        Property("notes", StringType),
        Property("account", StringType),
        Property("created_by_id", IntegerType),
        Property("customer_type", StringType),  # business, retail
        Property("company_name", StringType),
        Property("payment_terms", IntegerType),  # 14
        Property("currency", NullType),
        Property("payment_method", NullType),
        Property("discount", NumberType),
        Property("minimum_order_value", NumberType),
        Property("delivery_method_id", IntegerType),
        Property("full_name", StringType),
        Property("price_list_id", IntegerType),
        Property("remote_id", StringType),
        Property("contacts", ArrayType(_ContactObject)),
        Property("addresses", ArrayType(_AddressObject)),
        Property("price_list", _PriceListObject),
        Property("billing_address", BillingAddressObject),
        Property("shipping_addresses", ArrayType(DeliveryAddressObject)),
        Property("contact_data", _ContactDataObject),
        Property("last_used_shipping_address", DeliveryAddressObject),
        Property("delivery_method", _DeliveryMethodObject),
    )
