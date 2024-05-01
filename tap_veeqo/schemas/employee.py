"""Schema definitions for employee objects."""

from singer_sdk import typing as th

_PermissionsObject = th.PropertiesList(
    th.Property("rules", th.BooleanType),
    th.Property("accounts", th.BooleanType),
    th.Property("invoices", th.BooleanType),
    th.Property("customers", th.BooleanType),
    th.Property("edit_users", th.BooleanType),
    th.Property("share_views", th.BooleanType),
    th.Property("edit_channels", th.BooleanType),
    th.Property("custom_reports", th.BooleanType),
    th.Property("delete_product", th.BooleanType),
    th.Property("manage_billing", th.BooleanType),
    th.Property("edit_cost_price", th.BooleanType),
    th.Property("edit_warehouses", th.BooleanType),
    th.Property("email_templates", th.BooleanType),
    th.Property("manage_listings", th.BooleanType),
    th.Property("manage_shipping", th.BooleanType),
    th.Property("manage_suppliers", th.BooleanType),
    th.Property("view_team_report", th.BooleanType),
    th.Property("view_sales_report", th.BooleanType),
    th.Property("edit_product_price", th.BooleanType),
    th.Property("share_custom_views", th.BooleanType),
    th.Property("edit_product_images", th.BooleanType),
    th.Property("view_product_report", th.BooleanType),
    th.Property("view_forecast_report", th.BooleanType),
    th.Property("view_shipping_report", th.BooleanType),
    th.Property("create_order_payments", th.BooleanType),
    th.Property("edit_delivery_methods", th.BooleanType),
    th.Property("manage_picking_queues", th.BooleanType),
    th.Property("picking_configuration", th.BooleanType),
    th.Property("view_dashboard_report", th.BooleanType),
    th.Property("manage_purchase_orders", th.BooleanType),
    th.Property("manage_stock_transfers", th.BooleanType),
    th.Property("remove_order_inventory", th.BooleanType),
    th.Property("view_stock_take_report", th.BooleanType),
    th.Property("manage_general_settings", th.BooleanType),
    th.Property("manage_role_permissions", th.BooleanType),
    th.Property("import_and_export_orders", th.BooleanType),
    th.Property("manual_stock_adjustments", th.BooleanType),
    th.Property("view_sales_digest_report", th.BooleanType),
    th.Property("manage_inventory_settings", th.BooleanType),
    th.Property("manage_printing_templates", th.BooleanType),
    th.Property("delete_company_custom_views", th.BooleanType),
    th.Property("manage_collection_manifests", th.BooleanType),
    th.Property("update_company_custom_views", th.BooleanType),
    th.Property("view_warehouse_inventory_report", th.BooleanType),
)


_RoleObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("company_id", th.IntegerType),
    th.Property(
        "name",
        th.StringType,
        # Admin
        # Customer Service Manager
        # Warehouse Manager
        # Purchaser
        # Accountant
        # Customer Service Agent
        # Picker/Packer
    ),
    th.Property("permissions", _PermissionsObject),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
)


_StockTakePreferenceObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("warehouse_id", th.IntegerType),
    th.Property("percentage", th.IntegerType),
)


EmployeeObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("company_id", th.IntegerType),
    th.Property("login", th.StringType),
    th.Property("email", th.EmailType),
    th.Property("default_warehouse_id", th.IntegerType),
    th.Property("default_channel_id", th.IntegerType),
    th.Property("two_factor_authentication_enabled", th.BooleanType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("timezone", th.StringType),
    th.Property("role", _RoleObject),
    th.Property("stock_take_preferences", th.ArrayType(_StockTakePreferenceObject)),
    th.Property("company_owner", th.BooleanType),
)
