"""
This module contains classes Order, Item.
They are basis of creating orders system.
"""

from tracking import Location
import random
from random import seed

seed(23221221)

class Order:
    """
    This class represents created order. Contains
    attributes: location, user_name, items, vehicle, orderId;
    methods: __str__(), calculateAmount(), assignVehicle().
    """

    def __init__(self, user_name: str, city: str, postoffice: int, items: list):
        """
        Here we initialize attributes:
            self.location
            self.user_name
            self.items
            self.vehicle
            self.orderId
        """
        self.location = Location(city, postoffice)
        self.user_name = user_name
        self.items = items
        self.vehicle = None
        self.orderId = random.randint(100000000, 999999999)
        print(str(self))

    def __str__(self) -> str:
        """
        This function returns f-string containing orderId
        of created order.
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', posto\
ffice = 53, items = my_items)
        Your order number is 928221043.
        """
        return f"Your order number is {self.orderId}."

    def calculateAmount(self) -> int:
        """
        This function calculates total price
        of items in created order.
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', posto\
ffice = 53, items = my_items)
        Your order number is 553286946.
        >>> my_order.calculateAmount()
        154
        """
        lst = []
        for i in self.items:
            lst.append(float(i.price))
        if str(sum(lst))[-1] == "0":
            return int(sum(lst))
        return sum(lst)

    def assignVehicle(self, vehicle: object) -> None:
        """
        This function assign typed vehicle to
        this order.
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', posto\
ffice = 53, items = my_items)
        Your order number is 156817082.
        >>> my_order.assignVehicle("Traktor")
        """
        self.vehicle = vehicle

class Item:
    """
    This class represents any items, which can occure in
    order. Has attributes:
        name
        price
    methods:
        __str__()
    """
    def __init__(self, name: str, price: float):
        """
        Here we initialize the only two attributes:
            self.name
            self.price
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        This funtion returns string, which
        represents itself.
        >>> my_Item = Item('book',110)
        >>> print(my_Item)
        Item('book',110)
        """
        return f"Item('{self.name}',{self.price})"
