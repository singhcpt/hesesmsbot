import uuid
import time

class Post: 

    def __init__(self, post_id, user_id, title, type, subType, quantity, location, price):
        self.post_id = post_id
        self.user_id = user_id
        self.title = title
        self.type = type
        self.subType = subType
        self.quantity = quantity
        self.location = location
        self.price = price

    def setTitle(self, title):
        self.title = title
        return

    def setType(self, typ):
        self.type = typ
        return

    def setQuantity(self, quantity):
        self.quantity = quantity
        return

    def setLocation(self, location):
        self.location = location
        return

    def setPrice(self, price):
        self.price = price
        return 

    def __str__(self):
        return "Item: " + self.title + " | Quantity: " + str(self.quantity) + " Units | Location: " + self.location + " | Price: " + str(self.price) + " sh "
    
    __repr__=__str__
        