"""Schema definitions for address objects."""

from singer_sdk import typing as th

from tap_veeqo.schemas import NullType

BillingAddressObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("short_name", th.StringType),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("address1", th.StringType),
    th.Property("address2", th.StringType),
    th.Property("city", th.StringType),
    th.Property("company", th.StringType),
    th.Property("country", th.StringType),
    th.Property("state", th.StringType),
    th.Property("zip", th.StringType),
    th.Property("phone", th.StringType),
    th.Property("email", th.EmailType),
    th.Property("is_default", th.BooleanType),
)


DeliveryAddressObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("short_name", th.StringType),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("email", th.EmailType),
    th.Property("company", th.StringType),
    th.Property("address1", th.StringType),
    th.Property("address2", th.StringType),
    th.Property("city", th.StringType),
    th.Property("country", th.StringType),
    th.Property("state", th.StringType),
    th.Property("zip", th.StringType),
    th.Property("phone", th.StringType),
    th.Property("tax_id", NullType),
    th.Property("is_default", th.BooleanType),
    th.Property("validated", NullType),
    th.Property("residential", NullType),
    th.Property("validation_message", NullType),
    th.Property("verified", th.BooleanType),
    th.Property("location_found", th.BooleanType),
)
