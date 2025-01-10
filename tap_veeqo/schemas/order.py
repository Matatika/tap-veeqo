"""Schema definitions for order objects."""

from singer_sdk import typing as th

from tap_veeqo.schemas import DimensionsUnitProperty, NullType, WeightUnitProperty
from tap_veeqo.schemas.address import BillingAddressObject, DeliveryAddressObject
from tap_veeqo.schemas.customer import CustomerObject
from tap_veeqo.schemas.employee import EmployeeObject
from tap_veeqo.schemas.sellable import SellableObject
from tap_veeqo.schemas.store import StoreObject
from tap_veeqo.schemas.tag import TagObject
from tap_veeqo.schemas.user import UserObject
from tap_veeqo.schemas.warehouse import WarehouseObject

_EmployeeNoteObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("text", th.StringType),
    th.Property("order_id", th.IntegerType),
    th.Property("created_at", th.DateTimeType),
    th.Property("mentions", th.ArrayType(EmployeeObject)),
    th.Property("created_by", EmployeeObject),
)


_PaymentObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("payment_type", th.StringType),
    th.Property("reference_number", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("order_id", th.IntegerType),
    th.Property("card_number", th.StringType),
    th.Property("created_by_id", th.IntegerType),
)


_DeliveryMethodObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("cost", th.NumberType),
    th.Property("name", th.StringType),
)


_CustomerNoteObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("text", th.StringType),
    th.Property("order_id", th.IntegerType),
)


_WarehouseSublocationObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("location", th.StringType),
)


_LineItemObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("price_per_unit", th.NumberType),
    th.Property("quantity", th.IntegerType),
    th.Property("picked_quantity", th.IntegerType),
    th.Property("tax_rate", th.NumberType),
    th.Property("taxless_discount_per_unit", th.NumberType),
    th.Property("additional_options", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("remote_id", th.StringType),
    th.Property("title", th.StringType),
    th.Property("sellable", SellableObject),
    th.Property("warehouse_sublocation", _WarehouseSublocationObject),
)


_OutboundLabelChargesObject = th.PropertiesList(
    th.Property("unit", NullType),
    th.Property("value", NullType),
)


_TrackingNumberObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("tracking_number", th.StringType),
    th.Property("cancelled", th.BooleanType),
    th.Property("used", th.BooleanType),
    th.Property("carrier_service_id", th.IntegerType),
    th.Property("billed", th.BooleanType),
    th.Property("shipment_id", th.IntegerType),
    th.Property("tracking_number_range_id", th.IntegerType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("user_trackable", th.BooleanType),
    th.Property("awaiting_collection_at", th.DateTimeType),
    th.Property("awaiting_drop_off_at", th.DateTimeType),
    th.Property("collected_at", th.DateTimeType),
    th.Property("delivered_at", th.DateTimeType),
    th.Property("delivered_to_secure_location_at", th.DateTimeType),
    th.Property("in_clearance_at", th.DateTimeType),
    th.Property("in_transit_at", th.DateTimeType),
    th.Property("out_for_delivery_at", th.DateTimeType),
    th.Property("attempted_delivery_at", th.DateTimeType),
    th.Property("collect_from_depot_at", th.DateTimeType),
    th.Property("notified_recipient_at", th.DateTimeType),
    th.Property("delayed_at", th.DateTimeType),
    th.Property("cancelled_at", th.DateTimeType),
    th.Property("contact_support_at", th.DateTimeType),
    th.Property("recipient_refused_at", th.DateTimeType),
    th.Property("returned_to_sender_at", th.DateTimeType),
    th.Property("status", th.StringType),  # created
)


_OptionValueObject = th.PropertiesList(
    th.Property("value", th.StringType),
    th.Property("label", th.StringType),
    th.Property("price", NullType),
    th.Property("currency", NullType),
)


_OptionObject = th.PropertiesList(
    th.Property(
        "key", th.StringType
    ),  # parcel_type, delivery_type, account_type, signature
    th.Property("label", th.StringType),
    th.Property("type", th.StringType),  # select
    th.Property("multiple", th.BooleanType),
    th.Property("values", th.ArrayType(_OptionValueObject)),
    th.Property("validation", NullType),
    th.Property("unit", NullType),
    th.Property("default", NullType),
)


_ShippingServiceOptionsObject = th.PropertiesList(
    th.Property("base", th.ArrayType(_OptionObject)),
)


_CarrierObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("provider_type", th.StringType),
    th.Property("slug", th.StringType),
    th.Property("name", th.StringType),
    th.Property("is_configured?", th.BooleanType),
    th.Property("is_integrated?", th.BooleanType),
    th.Property("is_demo_mode?", th.BooleanType),
    th.Property("show_when_shipping?", th.BooleanType),
    th.Property("inbound_supported", th.BooleanType),
    th.Property("requires_reconnect", th.BooleanType),
    th.Property("requires_test_labels", th.BooleanType),
    th.Property("is_pending", th.BooleanType),
    th.Property("shipping_service_options", _ShippingServiceOptionsObject),
    th.Property("using_dhl_parcel_rest_api", th.BooleanType),
)


_ShipmentObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("created_at", th.DateTimeType),
    th.Property("allocation_id", th.IntegerType),
    th.Property("carrier_id", th.IntegerType),
    th.Property("charges", th.ObjectType()),
    th.Property("shipped_by_id", th.IntegerType),
    th.Property("parcel_format", NullType),
    th.Property("postal_class", NullType),
    th.Property("weight", th.NumberType),
    th.Property("collection_manifest_id", th.IntegerType),
    th.Property("carrier_service_id", th.IntegerType),
    th.Property(
        "service_type", th.StringType
    ),  # 1, 10, 30, 48, 220, 225, 240, 250, 260, 270
    th.Property("service_name", th.StringType),
    th.Property("short_service_name", NullType),
    th.Property("service_carrier_name", NullType),
    th.Property("sub_carrier_id", th.IntegerType),
    th.Property("packaging_type", NullType),
    th.Property("drop_off_type", NullType),
    th.Property("insured_value", th.NumberType),
    th.Property("notify_customer", th.BooleanType),
    th.Property("update_remote_order", th.BooleanType),
    th.Property("delivery_confirmation_number", NullType),
    th.Property("tracking_url", th.URIType),
    th.Property("outbound_shipment_date", th.DateType),
    th.Property("outbound_label_charges", _OutboundLabelChargesObject),
    th.Property("label_url", th.URIReferenceType),
    th.Property("commercial_invoice_url", NullType),
    th.Property("aftership_url", th.URIType),
    th.Property("tracking_number", _TrackingNumberObject),
    th.Property("order_id", th.IntegerType),
    th.Property("carrier", _CarrierObject),
    th.Property("carrier_service", NullType),
    th.Property("carrier_country", NullType),
    th.Property("carrier_fees", th.ArrayType(th.ObjectType())),
    th.Property("carrier_fee", NullType),
    th.Property("shipped_by", EmployeeObject),
)


_AllocationPackageObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("allocation_id", th.IntegerType),
    th.Property("created_at", th.DateTimeType),
    th.Property("depth", th.IntegerType),
    th.Property("height", th.IntegerType),
    th.Property("package_id", NullType),
    th.Property("package_provider", NullType),
    th.Property("package_selection_source", th.StringType),  # ONE_OFF
    th.Property("package_name", th.StringType),
    th.Property("similarity_key", th.StringType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("weight", th.IntegerType),
    th.Property("width", th.IntegerType),
    WeightUnitProperty,
    DimensionsUnitProperty,
)


_AllocationObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("created_at", th.DateTimeType),
    th.Property("total_weight", th.NumberType),
    WeightUnitProperty,
    th.Property("allocated_by_id", th.IntegerType),
    th.Property("order_id", th.IntegerType),
    th.Property("packed_completely", NullType),
    th.Property("due_date", th.DateTimeType),
    th.Property("dispatch_date", th.DateTimeType),
    th.Property("line_items", th.ArrayType(_LineItemObject)),
    th.Property("recommended_shipping_options", NullType),
    th.Property("preferred_shipment_options", NullType),
    th.Property("matched_parcel_properties_criteria", NullType),
    th.Property("shipment", _ShipmentObject),
    th.Property("warehouse", WarehouseObject),
    th.Property("preferred_shipment_date", th.DateType),
    th.Property("allocation_package", _AllocationPackageObject),
    th.Property("from_gb_to_northern_ireland", th.BooleanType),
)


_ReturnLineItemObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("title", th.StringType),
    th.Property("sku_code", th.StringType),
    th.Property("quantity", th.IntegerType),
    th.Property("sellable_id", th.IntegerType),
    th.Property("received_quantity", th.IntegerType),
    th.Property("refund_amount", th.NumberType),
    th.Property("refund_amount_per_unit", th.NumberType),
    th.Property("refund_quantity", th.IntegerType),
)


_ReturnObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("number", th.StringType),
    th.Property("status", th.StringType),  # returning, returned
    th.Property("reason", NullType),
    th.Property("created_at", th.DateTimeType),
    th.Property(
        "type", th.StringType
    ),  # AllocatedItemsReturn, ShippedItemsReturn, UnallocatedItemsReturn
    th.Property("line_items", th.ArrayType(_ReturnLineItemObject)),
    th.Property("user", UserObject),
    th.Property("warehouse_name", th.StringType),
)


OrderObject = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("cancel_reason", th.StringType),
    th.Property("send_refund_email", th.BooleanType),
    th.Property("cancelled_at", th.DateTimeType),
    th.Property("created_at", th.DateTimeType),
    th.Property("delivery_cost", th.NumberType),
    th.Property("due_date", th.DateTimeType),
    th.Property("dispatch_date", th.DateTimeType),
    th.Property("international", th.BooleanType),
    th.Property("notes", th.StringType),
    th.Property("number", th.StringType),
    th.Property("receipt_printed", th.BooleanType),
    th.Property("send_notification_email", th.BooleanType),
    th.Property("can_pay_by_card", th.BooleanType),
    th.Property("shipped_at", th.DateTimeType),
    th.Property(
        "status",
        th.StringType,
        # awaiting_fulfillment
        # awaiting_payment
        # awaiting_stock
        # cancelled
        # on_hold
        # refunded
        # shipped
    ),
    th.Property("subtotal_price", th.NumberType),
    th.Property("total_discounts", th.NumberType),
    th.Property("total_price", th.NumberType),
    th.Property("total_tax", th.NumberType),
    th.Property("total_fees", th.NumberType),
    th.Property("buyer_user_id", th.IntegerType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("till_id", th.IntegerType),
    th.Property("fulfilled_by_amazon", th.BooleanType),
    th.Property("is_amazon_prime", th.BooleanType),
    th.Property("is_amazon_premium_order", th.BooleanType),
    th.Property("additional_order_level_taxless_discount", th.NumberType),
    th.Property("additional_order_level_taxless_discount_percentage", th.NumberType),
    th.Property("shipping_discount", th.NumberType),
    th.Property("restock_shipped_items", th.BooleanType),
    th.Property("adjustment_amount", th.NumberType),
    th.Property("currency_code", th.StringType),
    th.Property("contact_id", th.IntegerType),
    th.Property("business_customer_billing_address_id", th.IntegerType),
    th.Property("business_customer_shipping_address_id", th.IntegerType),
    th.Property("payment_due_date", th.DateTimeType),
    th.Property("payment_terms", th.IntegerType),  # 14
    th.Property("price_list_id", th.IntegerType),
    th.Property("picked_status", th.StringType),  # picked, unpicked
    th.Property("invoice_file_url", th.URIType),
    th.Property("invoice_date", th.DateTimeType),
    th.Property("mergable_checksum", th.StringType),
    th.Property("employee_notes", th.ArrayType(_EmployeeNoteObject)),
    th.Property("tags", th.ArrayType(TagObject)),
    th.Property("payment", _PaymentObject),
    th.Property("invoice_sent_ago", th.IntegerType),
    th.Property("invoice_viewed_at", NullType),
    th.Property("refund_amount", th.NumberType),
    th.Property("total_price", th.NumberType),
    th.Property("cancelled_by", EmployeeObject),
    th.Property("created_by", EmployeeObject),
    th.Property("updated_by", EmployeeObject),
    th.Property("delivery_method", _DeliveryMethodObject),
    th.Property("deliver_to", DeliveryAddressObject),
    th.Property("billing_address", BillingAddressObject),
    th.Property("channel", StoreObject),
    th.Property("customer", CustomerObject),
    th.Property("customer_note", _CustomerNoteObject),
    th.Property("allocations", th.ArrayType(_AllocationObject)),
    th.Property("returns", th.ArrayType(_ReturnObject)),
    th.Property("allocated_completely", th.BooleanType),
    th.Property("picked_completely", th.BooleanType),
    th.Property("fulfillment_channel_order", NullType),
    th.Property("mergeable_id", th.StringType),
    th.Property("merged_to_id", th.StringType),
    th.Property("merged_order", th.BooleanType),
    th.Property("with_duties", th.BooleanType),
    th.Property("can_be_shipped", th.BooleanType),
    th.Property("line_items", th.ArrayType(_LineItemObject)),
)
