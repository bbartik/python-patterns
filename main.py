import json
from abc import abstractmethod, ABC
import pdb

class InventoryInterface(ABC):
    # no decorators here, they cause errors - why?
    def get_inventory(self):
        print(self.inventory)

    def get_inventory_by_site(self, site):
        self.inventory = [x for x in self.inventory if site in x["site"]]
        print(self.inventory)


class ViptelaInventory(InventoryInterface):
    def __init__(self):
        with open("viptela.json", "r") as f:
            self.inventory = json.load(f)


class PaloInventory(InventoryInterface):
    def __init__(self):
        with open("palo.json", "r") as f:
            self.inventory = json.load(f)


class InventoryFactory():
    @staticmethod
    def createInventory(inventoryType):
        if inventoryType == "viptela":
            return ViptelaInventory()
        elif inventoryType == "palo":
            return PaloInventory()
        else:
            print("No inventory of that type")


class Inventory():
    def __init__(self, inventoryType):
        self.inventory = InventoryFactory.createInventory(inventoryType)


'''
v = ViptelaInventory()
v.get_inventory()

p = PaloInventory()
p.get_inventory()

v.get_inventory_by_site("Seattle")
'''

print("Getting inventory by type:")
i = Inventory("viptela").inventory
i.get_inventory()



