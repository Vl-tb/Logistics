"""
This module contains only one class Location, which
represents some data about order. 
"""

class Location:
    """
    This class is used to contain data about
    order. Has attributes:
        city
        postoffice
    methods:
        None
    """
    
    def __init__(self, city: str, postoffice: int):
        self.city = city
        self.postoffice = postoffice
