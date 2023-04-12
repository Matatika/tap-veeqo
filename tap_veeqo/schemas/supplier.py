from singer_sdk.typing import (
    DateTimeType,
    EmailType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_veeqo.schemas import CustomObject


class SupplierObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("name", StringType),
        Property("address_line_1", StringType),
        Property("address_line_2", StringType),
        Property("city", StringType),
        Property("region", StringType),
        Property("country", StringType),
        Property("post_code", StringType),
        Property("sales_contact_name", StringType),
        Property("sales_contact_email", EmailType),
        Property("sales_phone_number", StringType),
        Property("accounting_contact_name", StringType),
        Property("accounting_contact_email", EmailType),
        Property("accounting_phone_number", StringType),
        Property("currency_code", StringType),
        Property("created_by_id", IntegerType),
        Property("updated_by_id", IntegerType),
        Property("deleted_at", DateTimeType),
        Property("deleted_by_id", IntegerType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("bank_name", StringType),
        Property("bank_account_number", StringType),
        Property("bank_sort_code", StringType),
        Property("credit_limit", StringType),
        Property("active_purchase_order_count", IntegerType),
        Property("completed_purchase_order_count", IntegerType),
        Property("purchase_order_template", StringType),
        Property("reminder_email_template", StringType),
        Property("company_id", IntegerType),
    )
