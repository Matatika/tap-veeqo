"""Schema definitions for purchase order objects."""

from singer_sdk import typing as th

from tap_veeqo.schemas.employee import EmployeeObject
from tap_veeqo.schemas.sellable import SellableObject
from tap_veeqo.schemas.supplier import SupplierObject
from tap_veeqo.schemas.warehouse import WarehouseObject

_SupplierProductVariant = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("supplier", SupplierObject),
    th.Property("cost", th.NumberType),
    th.Property("reference_number", th.StringType),
    th.Property("default_supplier", th.BooleanType),
    th.Property("tax_rate", th.NumberType),
    th.Property("average_cost", th.NumberType),
    th.Property("title", th.StringType),
    th.Property("has_active_purchase_order", th.BooleanType),
    th.Property("created_by_id", th.IntegerType),
    th.Property("updated_by_id", th.IntegerType),
    th.Property("supplier_id", th.IntegerType),
    th.Property("product_variant_id", th.IntegerType),
    th.Property("lead_time", th.IntegerType),
    th.Property("product_variant", SellableObject),
)


_PurchaseOrderProductVariantObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("purchase_order_id", th.IntegerType),
    th.Property("product_variant_id", th.IntegerType),
    th.Property("supplier_id", th.IntegerType),
    th.Property("created_by_id", th.IntegerType),
    th.Property("updated_by_id", th.IntegerType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("quantity", th.IntegerType),
    th.Property("received", th.IntegerType),
    th.Property("received_at", th.DateTimeType),
    th.Property("cost", th.NumberType),
    th.Property("tax_rate", th.NumberType),
    th.Property("total_amount_including_tax", th.NumberType),
    th.Property("total_amount_excluding_tax", th.NumberType),
    th.Property("shipped", th.BooleanType),
    th.Property("supplier_product_variant", _SupplierProductVariant),
)


PurchaseOrderObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("number", th.StringType),
    th.Property("reference_number", th.StringType),
    th.Property("user_id", th.IntegerType),
    th.Property("supplier_id", th.IntegerType),
    th.Property("destination_warehouse_id", th.IntegerType),
    th.Property("state", th.StringType),  # active, completed, draft
    th.Property("created_by_id", th.IntegerType),
    th.Property("updated_by_id", th.IntegerType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("expected_date", th.DateTimeType),
    th.Property("estimated_delivery_days", th.IntegerType),
    th.Property("currency_code", th.StringType),
    th.Property("currency_rate", th.NumberType),
    th.Property("shipping_address_line_1", th.StringType),
    th.Property("shipping_address_line_2", th.StringType),
    th.Property("shipping_address_town", th.StringType),
    th.Property("shipping_address_state", th.StringType),
    th.Property("shipping_address_postcode", th.StringType),
    th.Property("shipping_address_country", th.StringType),
    th.Property("billing_address_line_1", th.StringType),
    th.Property("billing_address_line_2", th.StringType),
    th.Property("billing_address_town", th.StringType),
    th.Property("billing_address_state", th.StringType),
    th.Property("billing_address_postcode", th.StringType),
    th.Property("billing_address_country", th.StringType),
    th.Property("product_variants_count", th.IntegerType),
    th.Property("received_product_variants_count", th.IntegerType),
    th.Property("note", th.StringType),
    th.Property("units_ordered", th.IntegerType),
    th.Property("units_received", th.IntegerType),
    th.Property("subtotal", th.NumberType),
    th.Property("total_tax", th.NumberType),
    th.Property("shipping_and_handling", th.NumberType),
    th.Property("total_including_tax", th.NumberType),
    th.Property("total_excluding_tax", th.NumberType),
    th.Property("supplier_report_format", th.StringType),  # pdf
    th.Property("sent_at", th.DateTimeType),
    th.Property("received_at", th.DateTimeType),
    th.Property("supplier", SupplierObject),
    th.Property("destination_warehouse", WarehouseObject),
    th.Property("created_by", EmployeeObject),
    th.Property(
        "purchase_order_product_variants",
        th.ArrayType(_PurchaseOrderProductVariantObject),
    ),
)
