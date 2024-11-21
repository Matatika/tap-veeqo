"""Veeqo tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th
from typing_extensions import override

from tap_veeqo import streams

STREAM_TYPES = [
    streams.CustomersStream,
    streams.DeliveryMethodsStream,
    streams.EmployeesStream,
    streams.OrdersStream,
    streams.ProductsStream,
    streams.ProductBrandsStream,
    streams.ProductPropertiesStream,
    streams.ProductTagsStream,
    streams.PurchaseOrdersStream,
    streams.SellablesStream,
    streams.StoresStream,
    streams.SuppliersStream,
    streams.TagsStream,
    streams.WarehousesStream,
]


class TapVeeqo(Tap):
    """Veeqo tap class."""

    name = "tap-veeqo"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,
            description="API key",
        ),
    ).to_dict()

    @override
    def discover_streams(self):
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapVeeqo.cli()
