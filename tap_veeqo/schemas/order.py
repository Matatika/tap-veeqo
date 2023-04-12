from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
    URIReferenceType,
    URIType,
)

from tap_veeqo.schemas import CustomObject, NullType
from tap_veeqo.schemas.address import BillingAddressObject, DeliveryAddressObject
from tap_veeqo.schemas.customer import CustomerObject
from tap_veeqo.schemas.employee import EmployeeObject
from tap_veeqo.schemas.sellable import SellableObject
from tap_veeqo.schemas.store import StoreObject
from tap_veeqo.schemas.tag import TagObject
from tap_veeqo.schemas.user import UserObject
from tap_veeqo.schemas.warehouse import WarehouseObject


class _EmployeeNoteObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("text", StringType),
        Property("order_id", IntegerType),
        Property("created_at", DateTimeType),
        Property("mentions", ArrayType(EmployeeObject)),
        Property("created_by", EmployeeObject),
    )


class _PaymentObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("payment_type", StringType),
        Property("reference_number", StringType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("order_id", IntegerType),
        Property("card_number", StringType),
        Property("created_by_id", IntegerType),
    )


class _DeliveryMethodObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("cost", NumberType),
        Property("name", StringType),
    )


class _CustomerNoteObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("text", StringType),
        Property("order_id", IntegerType),
    )


class _LineItemObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("price_per_unit", NumberType),
        Property("quantity", IntegerType),
        Property("picked_quantity", IntegerType),
        Property("tax_rate", NumberType),
        Property("taxless_discount_per_unit", NumberType),
        Property("additional_options", StringType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("remote_id", StringType),
        Property("sellable", SellableObject),
    )


class _TrackingNumberObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("tracking_number", StringType),
        Property("cancelled", BooleanType),
        Property("used", BooleanType),
        Property("carrier_service_id", IntegerType),
        Property("billed", BooleanType),
        Property("shipment_id", IntegerType),
        Property("tracking_number_range_id", IntegerType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("user_trackable", BooleanType),
    )


class _OptionValueObject(CustomObject):
    properties = PropertiesList(
        Property("value", StringType),
        Property("label", StringType),
        Property("price", NullType),
        Property("currency", NullType),
    )


class _OptionObject(CustomObject):
    properties = PropertiesList(
        Property(
            "key", StringType
        ),  # parcel_type, delivery_type, account_type, signature
        Property("label", StringType),
        Property("type", StringType),  # select
        Property("multiple", BooleanType),
        Property("values", ArrayType(_OptionValueObject)),
        Property("validation", NullType),
        Property("unit", NullType),
    )


class _ShippingServiceOptionsObject(CustomObject):
    properties = PropertiesList(
        Property("base", ArrayType(_OptionObject)),
    )


class _CarrierObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("created_at", DateTimeType),
        Property("updated_at", DateTimeType),
        Property("provider_type", StringType),
        Property("slug", StringType),
        Property("name", StringType),
        Property("is_configured?", BooleanType),
        Property("is_integrated?", BooleanType),
        Property("is_demo_mode?", BooleanType),
        Property("show_when_shipping?", BooleanType),
        Property("inbound_supported", BooleanType),
        Property("shipping_service_options", _ShippingServiceOptionsObject),
    )


class _ShipmentObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("updated_at", DateTimeType),
        Property("created_at", DateTimeType),
        Property("allocation_id", IntegerType),
        Property("carrier_id", IntegerType),
        Property("shipped_by_id", IntegerType),
        Property("parcel_format", NullType),
        Property("postal_class", NullType),
        Property("weight", NumberType),
        Property("collection_manifest_id", IntegerType),
        Property("carrier_service_id", IntegerType),
        Property(
            "service_type", StringType
        ),  # 1, 10, 30, 48, 220, 225, 240, 250, 260, 270
        Property("service_name", StringType),
        Property("short_service_name", NullType),
        Property("service_carrier_name", NullType),
        Property("packaging_type", NullType),
        Property("drop_off_type", NullType),
        Property("insured_value", NumberType),
        Property("notify_customer", BooleanType),
        Property("update_remote_order", BooleanType),
        Property("delivery_confirmation_number", NullType),
        Property("tracking_url", URIType),
        Property("label_url", URIReferenceType),
        Property("commercial_invoice_url", NullType),
        Property("aftership_url", URIType),
        Property("tracking_number", _TrackingNumberObject),
        Property("order_id", IntegerType),
        Property("carrier", _CarrierObject),
        Property("carrier_service", NullType),
        Property("carrier_country", NullType),
        Property("carrier_fees", ArrayType(ObjectType())),
        Property("carrier_fee", NullType),
        Property("shipped_by", EmployeeObject),
    )


class _AllocationObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("updated_at", DateTimeType),
        Property("created_at", DateTimeType),
        Property("total_weight", NumberType),
        Property("weight_unit", StringType),  # g, kg
        Property("allocated_by_id", IntegerType),
        Property("order_id", IntegerType),
        Property("packed_completely", NullType),
        Property("due_date", DateTimeType),
        Property("dispatch_date", DateTimeType),
        Property("line_items", ArrayType(_LineItemObject)),
        Property("recommended_shipping_options", NullType),
        Property("preferred_shipment_options", NullType),
        Property("matched_parcel_properties_criteria", NullType),
        Property("shipment", _ShipmentObject),
        Property("warehouse", WarehouseObject),
    )


class _ReturnLineItemObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("title", StringType),
        Property("sku_code", StringType),
        Property("quantity", IntegerType),
        Property("sellable_id", IntegerType),
        Property("received_quantity", IntegerType),
        Property("refund_amount", NumberType),
        Property("refund_amount_per_unit", NumberType),
        Property("refund_quantity", IntegerType),
    )


class _ReturnObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("number", StringType),
        Property("status", StringType),  # returning, returned
        Property("reason", NullType),
        Property("created_at", DateTimeType),
        Property(
            "type", StringType
        ),  # AllocatedItemsReturn, ShippedItemsReturn, UnallocatedItemsReturn
        Property("line_items", ArrayType(_ReturnLineItemObject)),
        Property("user", UserObject),
        Property("warehouse_name", StringType),
    )


class OrderObject(CustomObject):
    properties = PropertiesList(
        Property("id", IntegerType),
        Property("cancel_reason", StringType),
        Property("send_refund_email", BooleanType),
        Property("cancelled_at", DateTimeType),
        Property("created_at", DateTimeType),
        Property("delivery_cost", NumberType),
        Property("due_date", DateTimeType),
        Property("dispatch_date", DateTimeType),
        Property("international", BooleanType),
        Property("notes", StringType),
        Property("number", StringType),
        Property("receipt_printed", BooleanType),
        Property("send_notification_email", BooleanType),
        Property("can_pay_by_card", BooleanType),
        Property("shipped_at", DateTimeType),
        Property(
            "status", StringType
        ),  # awaiting_fulfillment, awaiting_payment, awaiting_stock, cancelled, on_hold, refunded, shipped
        Property("subtotal_price", NumberType),
        Property("total_discounts", NumberType),
        Property("total_price", NumberType),
        Property("total_tax", NumberType),
        Property("total_fees", NumberType),
        Property("buyer_user_id", IntegerType),
        Property("updated_at", DateTimeType),
        Property("till_id", IntegerType),
        Property("fulfilled_by_amazon", BooleanType),
        Property("is_amazon_prime", BooleanType),
        Property("is_amazon_premium_order", BooleanType),
        Property("additional_order_level_taxless_discount", NumberType),
        Property("additional_order_level_taxless_discount_percentage", NumberType),
        Property("shipping_discount", NumberType),
        Property("restock_shipped_items", BooleanType),
        Property("adjustment_amount", NumberType),
        Property("currency_code", StringType),
        Property("contact_id", IntegerType),
        Property("business_customer_billing_address_id", IntegerType),
        Property("business_customer_shipping_address_id", IntegerType),
        Property("payment_due_date", DateTimeType),
        Property("payment_terms", IntegerType),  # 14
        Property("price_list_id", IntegerType),
        Property("picked_status", StringType),  # picked, unpicked
        Property("invoice_file_url", URIType),
        Property("invoice_date", DateTimeType),
        Property("employee_notes", ArrayType(_EmployeeNoteObject)),
        Property("tags", ArrayType(TagObject)),
        Property("payment", _PaymentObject),
        Property("invoice_sent_ago", IntegerType),
        Property("invoice_viewed_at", NullType),
        Property("refund_amount", NumberType),
        Property("total_price", NumberType),
        Property("cancelled_by", EmployeeObject),
        Property("created_by", EmployeeObject),
        Property("updated_by", EmployeeObject),
        Property("delivery_method", _DeliveryMethodObject),
        Property("deliver_to", DeliveryAddressObject),
        Property("billing_address", BillingAddressObject),
        Property("channel", StoreObject),
        Property("customer", CustomerObject),
        Property("customer_note", _CustomerNoteObject),
        Property("allocations", ArrayType(_AllocationObject)),
        Property("returns", ArrayType(_ReturnObject)),
        Property("allocated_completely", BooleanType),
        Property("picked_completely", BooleanType),
        Property("fulfillment_channel_order", NullType),
        Property("mergeable_id", StringType),
        Property("with_duties", BooleanType),
        Property("can_be_shipped", BooleanType),
        Property("line_items", ArrayType(_LineItemObject)),
    )
