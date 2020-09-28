class Cache:
    
    def __init__(self):
        self.crop = ""
        self.kilograms = -1
        self.productType = -1
        self.subType = -1
        self.location = ""
        self.price = 0
        self.posts = list()
    
    def setCrop(self, crop):
        self.crop = crop
        return 
    
    def setKilograms(self, kgs):
        self.kilograms = kgs
        return

    def setLocation(self, location):
        self.location = location
        return

    def setPrice(self, price):
        self.price = price
        return

    def setType(self, typ):
        self.productType = typ
        return

    def setSubType(self, typ):
        self.subType = typ
        return

    def clearCache(self):
        self.crop = ""
        self.kilograms = -1
        self.location = ""
        self.price = 0
        return
