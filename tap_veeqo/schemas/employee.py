from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    EmailType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_veeqo.schemas import CustomObject


class _PermissionsObject(CustomObject):
    properties = PropertiesList(
        Property("rules", BooleanType),
        Property("accounts", BooleanType),
        Property("invoices", BooleanType),
        Property("customers", BooleanType),
        Property("edit_users", BooleanType),
        Property("share_views", BooleanType),
        Property("edit_channels", BooleanType),
        Property("custom_reports", BooleanType),
        Property("delete_product", BooleanType),
        Property("manage_billing", BooleanType),
        Property("edit_cost_price", BooleanType),
        Property("edit_warehouses", BooleanType),
        Property("email_templates", BooleanType),
        Property("manage_listings", BooleanType),
        Property("manage_shipping", BooleanType),
        Property("manage_suppliers", BooleanType),
        Property("view_team_report", BooleanType),
        Property("view_sales_report", BooleanType),
        Property("edit_product_price", BooleanType),
        Property("share_custom_views", BooleanType),
        Property("edit_product_images", BooleanType),
        Property("view_product_report", BooleanType),
        Property("view_forecast_report", BooleanType),
        Property("view_shipping_report", BooleanType),
        Property("create_order_payments", BooleanType),
        Property("edit_delivery_methods", BooleanType),
        Property("manage_picking_queues", BooleanType),
        Property("picking_configuration", BooleanType),
        Property("view_dashboard_report", BooleanType),
        Property("manage_purchase_orders", BooleanType),
        Property("manage_stock_transfers", BooleanType),
        Property("remove_order_inventory", BooleanType),
        Property("view_stock_take_report", BooleanType),
        Property("manage_general_settings", BooleanType),
        Property("manage_role_permissions", BooleanType),
        Property("import_and_export_orders", BooleanType),
        Property("manual_stock_adjustments", BooleanType),
        Property("view_sales_digest_report", BooleanType),
        Property("manage_inventory_settings", BooleanType),
        Property("manage_printing_templates", BooleanType),
        Property("delete_company_custom_views", BooleanType),
        Property("manage_collection_manifests", BooleanType),
        Property("update_company_custom_views", BooleanType),
        Property("view_warehouse_inventory_report", BooleanType),
    )


class _RoleObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("company_id", IntegerType),
        Property(
            "name", StringType
        ),  # Admin, Customer Service Manager, Warehouse Manager, Purchaser, Accountant, Customer Service Agent, Picker/Packer
        Property("permissions", _PermissionsObject),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
    )


class _StockTakePreferenceObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("warehouse_id", IntegerType),
        Property("percentage", IntegerType),
    )


class EmployeeObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("company_id", IntegerType),
        Property("login", StringType),
        Property("email", EmailType),
        Property("default_warehouse_id", IntegerType),
        Property("default_channel_id", IntegerType),
        Property("two_factor_authentication_enabled", BooleanType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("timezone", StringType),
        Property("role", _RoleObject),
        Property("stock_take_preferences", ArrayType(_StockTakePreferenceObject)),
        Property("company_owner", BooleanType),
    )
