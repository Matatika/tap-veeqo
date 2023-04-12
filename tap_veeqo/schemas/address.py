from singer_sdk.typing import (
    BooleanType,
    EmailType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_veeqo.schemas import CustomObject, NullType


class BillingAddressObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("short_name", StringType),
        Property("first_name", StringType),
        Property("last_name", StringType),
        Property("address1", StringType),
        Property("address2", StringType),
        Property("city", StringType),
        Property("company", StringType),
        Property("country", StringType),
        Property("state", StringType),
        Property("zip", StringType),
        Property("phone", StringType),
        Property("email", EmailType),
        Property("is_default", NullType),
    )


class DeliveryAddressObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("short_name", StringType),
        Property("first_name", StringType),
        Property("last_name", StringType),
        Property("email", EmailType),
        Property("company", StringType),
        Property("address1", StringType),
        Property("address2", StringType),
        Property("city", StringType),
        Property("country", StringType),
        Property("state", StringType),
        Property("zip", StringType),
        Property("phone", StringType),
        Property("tax_id", NullType),
        Property("is_default", NullType),
        Property("validated", NullType),
        Property("residential", NullType),
        Property("validation_message", NullType),
        Property("verified", BooleanType),
        Property("location_found", BooleanType),
    )
