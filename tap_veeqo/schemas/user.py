from singer_sdk.typing import (
    EmailType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_veeqo.schemas import CustomObject


class UserObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("name", StringType),
        Property("email", EmailType),
    )
