import orders

class LogisticSystem:
    """
    """

    def __init__(self, orders: list, vehicles: list):
        self.orders = orders
        self.vehicles = vehicles

    def placeOrder(self, order: object) -> None:
        """
        """
        pass

    def trackOrder(self, orderId: int) -> str:
        """
        """
        pass

class Vehicle:
    """
    """

    def __init__(self, vehicleNo: int, isAvailable: bool):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable
