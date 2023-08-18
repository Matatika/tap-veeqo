from singer_sdk import typing as th

from tap_veeqo.schemas import CustomObject


class UserObject(CustomObject):
    properties = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("email", th.EmailType),
    )
