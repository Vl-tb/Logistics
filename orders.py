import tracking

class Order:
    """
    """

    def __init__(self, orderId: int, user_name: str, location: object, items: list, vehicle: None):
        self.orderId = orderId
        self.user_name = user_name
        self.location = location
        self.items = items
        self.vehicle = vehicle

    def __str__(self) -> str:
        """
        """
        pass

    def calculateAmount(self) -> int:
        """
        """
        pass

    def assignVehicle(self, vehicle: object) -> None:
        """
        """
        pass

class Item:
    """
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        """
        pass