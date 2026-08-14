"""Schema definitions for customer objects."""

from singer_sdk import typing as th

from tap_veeqo.schemas import NullType
from tap_veeqo.schemas.address import BillingAddressObject, DeliveryAddressObject

_ContactObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("email", th.EmailType),
    th.Property("phone", th.StringType),
    th.Property("title", th.StringType),
    th.Property("is_default", th.BooleanType),
    th.Property("customer_id", th.IntegerType),
)


_AddressObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("company", th.StringType),
    th.Property("address1", th.StringType),
    th.Property("address2", th.StringType),
    th.Property("city", th.StringType),
    th.Property("country", th.StringType),
    th.Property("state", th.StringType),
    th.Property("zip", th.StringType),
    th.Property("type", th.StringType),  # BillingAddress, ShippingAddress
    th.Property("short_name", th.StringType),
    th.Property("email", th.EmailType),
    th.Property("customer_id", th.IntegerType),
    th.Property("phone", th.StringType),
    th.Property("editable", th.BooleanType),
    th.Property("is_default", th.BooleanType),
)


_PriceListObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("default", NullType),
    th.Property("currency_code", th.StringType),
)


_ContactDataObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("title", th.StringType),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("email", th.EmailType),
    th.Property("phone", th.StringType),
    th.Property("customer_id", th.IntegerType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("is_default", th.BooleanType),
)


_DeliveryMethodObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("cost", th.NumberType),
    th.Property("name", th.StringType),
)


CustomerObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("email", th.EmailType),
    th.Property("phone", th.StringType),
    th.Property("mobile", th.StringType),
    th.Property("notes", th.StringType),
    th.Property("account", th.StringType),
    th.Property("created_by_id", th.IntegerType),
    th.Property("customer_type", th.StringType),  # business, retail
    th.Property("company_name", th.StringType),
    th.Property("payment_terms", th.IntegerType),  # 14
    th.Property("currency", NullType),
    th.Property("payment_method", NullType),
    th.Property("discount", th.NumberType),
    th.Property("minimum_order_value", th.NumberType),
    th.Property("delivery_method_id", th.IntegerType),
    th.Property("full_name", th.StringType),
    th.Property("price_list_id", th.IntegerType),
    th.Property("remote_id", th.StringType),
    th.Property("contacts", th.ArrayType(_ContactObject)),
    th.Property("addresses", th.ArrayType(_AddressObject)),
    th.Property("price_list", _PriceListObject),
    th.Property("billing_address", BillingAddressObject),
    th.Property("shipping_addresses", th.ArrayType(DeliveryAddressObject)),
    th.Property("contact_data", _ContactDataObject),
    th.Property("last_used_shipping_address", DeliveryAddressObject),
    th.Property("delivery_method", _DeliveryMethodObject),
)
