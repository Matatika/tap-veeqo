"""Stream type classes for tap-veeqo."""

from __future__ import annotations

from typing_extensions import override

from tap_veeqo.client import VeeqoStream
from tap_veeqo.schemas.customer import CustomerObject
from tap_veeqo.schemas.delivery_method import DeliveryMethodObject
from tap_veeqo.schemas.employee import EmployeeObject
from tap_veeqo.schemas.order import OrderObject
from tap_veeqo.schemas.product import ProductObject
from tap_veeqo.schemas.product_brand import ProductBrandObject
from tap_veeqo.schemas.purchase_order import PurchaseOrderObject
from tap_veeqo.schemas.sellable import SellableObject
from tap_veeqo.schemas.store import StoreObject
from tap_veeqo.schemas.supplier import SupplierObject
from tap_veeqo.schemas.tag import TagObject
from tap_veeqo.schemas.warehouse import WarehouseObject


class CustomersStream(VeeqoStream):
    """Define customers stream."""

    name = "customers"
    path = "/customers"
    schema = CustomerObject.to_dict()


class DeliveryMethodsStream(VeeqoStream):
    """Define delivery methods stream."""

    name = "delivery_methods"
    path = "/delivery_methods"
    schema = DeliveryMethodObject.to_dict()


class EmployeesStream(VeeqoStream):
    """Define employees stream."""

    name = "employees"
    path = "/employees"
    schema = EmployeeObject.to_dict()


class OrdersStream(VeeqoStream):
    """Define orders stream."""

    name = "orders"
    path = "/orders"
    replication_key = "updated_at"
    schema = OrderObject.to_dict()


class ProductsStream(VeeqoStream):
    """Define products stream."""

    name = "products"
    path = "/products"
    replication_key = "updated_at"
    schema = ProductObject.to_dict()


class ProductBrandsStream(VeeqoStream):
    """Define product brands stream."""

    name = "product_brands"
    path = "/product_brands"
    schema = ProductBrandObject.to_dict()


class ProductTagsStream(VeeqoStream):
    """Define product tags stream."""

    name = "product_tags"
    path = "/products/tags"
    schema = TagObject.to_dict()


class PurchaseOrdersStream(VeeqoStream):
    """Define purchase orders stream."""

    name = "purchase_orders"
    path = "/purchase_orders"
    schema = PurchaseOrderObject.to_dict()

    @override
    def post_process(self, row, context):
        # credit_limit can be either a string or decimal, so coerce to string
        credit_limit = row.get("supplier", {}).get("credit_limit")

        if credit_limit is not None:
            row["supplier"]["credit_limit"] = str(credit_limit)

        return row


class SellablesStream(VeeqoStream):
    """Define sellables stream."""

    name = "sellables"
    path = "/sellables"
    schema = SellableObject.to_dict()


class StoresStream(VeeqoStream):
    """Define stores stream."""

    name = "stores"
    path = "/channels"
    schema = StoreObject.to_dict()


class SuppliersStream(VeeqoStream):
    """Define suppliers stream."""

    name = "suppliers"
    path = "/suppliers"
    schema = SupplierObject.to_dict()


class TagsStream(VeeqoStream):
    """Define tags stream."""

    name = "tags"
    path = "/tags"
    schema = TagObject.to_dict()


class WarehousesStream(VeeqoStream):
    """Define warehouses stream."""

    name = "warehouses"
    path = "/warehouses"
    schema = WarehouseObject.to_dict()
