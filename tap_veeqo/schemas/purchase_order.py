from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    PropertiesList,
    Property,
    StringType,
)

from tap_veeqo.schemas import CustomObject
from tap_veeqo.schemas.employee import EmployeeObject
from tap_veeqo.schemas.sellable import SellableObject
from tap_veeqo.schemas.supplier import SupplierObject
from tap_veeqo.schemas.warehouse import WarehouseObject


class _SupplierProductVariant(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("supplier", SupplierObject),
        Property("cost", NumberType),
        Property("reference_number", StringType),
        Property("default_supplier", BooleanType),
        Property("tax_rate", NumberType),
        Property("average_cost", NumberType),
        Property("title", StringType),
        Property("has_active_purchase_order", BooleanType),
        Property("created_by_id", IntegerType),
        Property("updated_by_id", IntegerType),
        Property("supplier_id", IntegerType),
        Property("product_variant_id", IntegerType),
        Property("lead_time", IntegerType),
        Property("product_variant", SellableObject),
    )


class _PurchaseOrderProductVariantObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("purchase_order_id", IntegerType),
        Property("product_variant_id", IntegerType),
        Property("supplier_id", IntegerType),
        Property("created_by_id", IntegerType),
        Property("updated_by_id", IntegerType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("quantity", IntegerType),
        Property("received", IntegerType),
        Property("received_at", DateTimeType),
        Property("cost", NumberType),
        Property("tax_rate", NumberType),
        Property("total_amount_including_tax", NumberType),
        Property("total_amount_excluding_tax", NumberType),
        Property("shipped", BooleanType),
        Property("supplier_product_variant", _SupplierProductVariant),
    )


class PurchaseOrderObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("number", StringType),
        Property("reference_number", StringType),
        Property("user_id", IntegerType),
        Property("supplier_id", IntegerType),
        Property("destination_warehouse_id", IntegerType),
        Property("state", StringType),  # active, completed, draft
        Property("created_by_id", IntegerType),
        Property("updated_by_id", IntegerType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("expected_date", DateTimeType),
        Property("estimated_delivery_days", IntegerType),
        Property("currency_code", StringType),
        Property("currency_rate", NumberType),
        Property("shipping_address_line_1", StringType),
        Property("shipping_address_line_2", StringType),
        Property("shipping_address_town", StringType),
        Property("shipping_address_state", StringType),
        Property("shipping_address_postcode", StringType),
        Property("shipping_address_country", StringType),
        Property("billing_address_line_1", StringType),
        Property("billing_address_line_2", StringType),
        Property("billing_address_town", StringType),
        Property("billing_address_state", StringType),
        Property("billing_address_postcode", StringType),
        Property("billing_address_country", StringType),
        Property("product_variants_count", IntegerType),
        Property("received_product_variants_count", IntegerType),
        Property("note", StringType),
        Property("units_ordered", IntegerType),
        Property("units_received", IntegerType),
        Property("subtotal", NumberType),
        Property("total_tax", NumberType),
        Property("shipping_and_handling", NumberType),
        Property("total_including_tax", NumberType),
        Property("total_excluding_tax", NumberType),
        Property("supplier_report_format", StringType),  # pdf
        Property("sent_at", DateTimeType),
        Property("received_at", DateTimeType),
        Property("supplier", SupplierObject),
        Property("destination_warehouse", WarehouseObject),
        Property("created_by", EmployeeObject),
        Property(
            "purchase_order_product_variants",
            ArrayType(_PurchaseOrderProductVariantObject),
        ),
    )
