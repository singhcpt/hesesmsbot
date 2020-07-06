class Cache:
    
    def __init__(self):
        self.crop = ""
        self.kilograms = -1
        self.location = ""
        self.price = 0
    
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

    def clearCache(self):
        self.crop = ""
        self.kilograms = -1
        self.location = ""
        self.price = 0
        return