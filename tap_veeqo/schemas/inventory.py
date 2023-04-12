from singer_sdk.typing import BooleanType, IntegerType, PropertiesList, Property

from tap_veeqo.schemas import CustomObject


class InventoryObject(CustomObject):
    properties = PropertiesList(
        Property("infinite", BooleanType),
        Property("physical_stock_level_at_all_warehouses", IntegerType),
        Property("allocated_stock_level_at_all_warehouses", IntegerType),
        Property("available_stock_level_at_all_warehouses", IntegerType),
        Property("incoming_stock_level_at_all_warehouses", IntegerType),
        Property("transit_outgoing_stock_level_at_all_warehouses", IntegerType),
        Property("transit_incoming_stock_level_at_all_warehouses", IntegerType),
    )
