"""Schema definitions for inventory objects."""

from singer_sdk import typing as th

InventoryObject = th.PropertiesList(
    th.Property("infinite", th.BooleanType),
    th.Property("physical_stock_level_at_all_warehouses", th.IntegerType),
    th.Property("allocated_stock_level_at_all_warehouses", th.IntegerType),
    th.Property("available_stock_level_at_all_warehouses", th.IntegerType),
    th.Property("incoming_stock_level_at_all_warehouses", th.IntegerType),
    th.Property("transit_outgoing_stock_level_at_all_warehouses", th.IntegerType),
    th.Property("transit_incoming_stock_level_at_all_warehouses", th.IntegerType),
)
