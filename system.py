"""
This module contains classes LogisticSystem
and Vehicle. Those are part of program, main
purpose of which is to create order (like post
system).
"""

import orders
from orders import Item, Order
from random import seed
import blessed

seed(23221221)

class LogisticSystem:
    """
    This is the main class of program. It
    has attributes: orders and vehicles;
    and methods: placeOrder, trackOrder.
    """

    def __init__(self, vehicles: list):
        """
        We initialize the only two attributes:
        self.orders
        self.vehicles.
        """
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: object) -> str:
        """
        This function is used to place yet created
        order. Returns None if success, attention
        string otherwise.
        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', post\
office = 53, items = my_items)
        Your order number is 928221043.
        >>> logSystem.placeOrder(my_order)
        """
        term = blessed.Terminal()
        if len(self.vehicles) > len(self.orders):
            self.orders.append(order)
            return
        print(term.clear + term.move_y(term.height//3) + term.center(f"The\
re is {term.red}no available{term.normal} vehicle to deliver a\
n {term.purple}order{term.normal}."))
        return "fail"

    def trackOrder(self, orderId: int) -> None:
        """
        This function is used to track info about
        created and placed order. Return string with
        info about transportation, or attention string
        if there are no such order in base.
        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', post\
office = 53, items = my_items)
        Your order number is 156817082.
        >>> logSystem.placeOrder(my_order)
        >>> logSystem.trackOrder(156817082)
        Your order #156817082 is sent to Lviv. Total price: 154 UAH.
        """
        term = blessed.Terminal()
        for i in self.orders:
            if i.orderId == orderId:
                order = i
                break
        try:
            total = order.calculateAmount()
        except UnboundLocalError:
            print(term.clear + term.move_y(term.height//3) +
            term.center(f"{term.red}No{term.normal} such order."))
            return 0
        output = f"Your {term.purple}order{term.normal} {term.yellow}#\
{orderId}{term.normal} is sent to {order.location.city}\
. Total price: {total} UAH."
        print(term.clear + term.move_y(term.height//3) + term.center(output))
        return 1

class Vehicle:
    """
    This class is used to describe a transportation vehicle.
    Contains attributes vehicleNo and isAvailable;
    methods: None.
    """

    def __init__(self, vehicleNo, isAvailable = True):
        """
        We initialize the only two attributes:
        self.vehicleNo and self.isAvailable.
        """
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable
