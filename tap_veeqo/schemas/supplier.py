"""Schema definitions for supplier objects."""

from singer_sdk import typing as th

SupplierObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("address_line_1", th.StringType),
    th.Property("address_line_2", th.StringType),
    th.Property("city", th.StringType),
    th.Property("region", th.StringType),
    th.Property("country", th.StringType),
    th.Property("post_code", th.StringType),
    th.Property("sales_contact_name", th.StringType),
    th.Property(
        "sales_contact_email",
        th.StringType,
    ),  # valid email, empty string or null
    th.Property("sales_phone_number", th.StringType),
    th.Property("accounting_contact_name", th.StringType),
    th.Property(
        "accounting_contact_email",
        th.StringType,
    ),  # valid email, empty string, or null
    th.Property("accounting_phone_number", th.StringType),
    th.Property("currency_code", th.StringType),
    th.Property("created_by_id", th.IntegerType),
    th.Property("updated_by_id", th.IntegerType),
    th.Property("deleted_at", th.DateTimeType),
    th.Property("deleted_by_id", th.IntegerType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("bank_name", th.StringType),
    th.Property("bank_account_number", th.StringType),
    th.Property("bank_sort_code", th.StringType),
    th.Property("credit_limit", th.StringType),
    th.Property("active_purchase_order_count", th.IntegerType),
    th.Property("completed_purchase_order_count", th.IntegerType),
    th.Property("purchase_order_template", th.StringType),
    th.Property("reminder_email_template", th.StringType),
    th.Property("company_id", th.IntegerType),
)
