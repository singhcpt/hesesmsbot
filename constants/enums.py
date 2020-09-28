import enum
class ProductType(enum.Enum):
    Food = 1
    Clothes = 2
    Footwear = 3
    Bedding = 4
    Other = 5

class FoodType(enum.Enum):
    Beverages = 1
    Bakery = 2
    Canned = 3
    Dairy = 4
    Dry = 5
    Frozen = 6
    Produce = 7
    Other = 8

class ClothesType(enum.Enum):
    Office = 1
    Casual = 2
    Child = 3

class FootwearType(enum.Enum):
    Adult = 1
    Child = 2

class BeddingType(enum.Enum):
    Bedsheets = 1
    Bedcovers = 2
    Pillowcases = 3

class CommandState(enum.Enum):
    Default = 1
    Setup = 2
    Posting = 3
    Verifying = 4
    Browsing = 5
    
