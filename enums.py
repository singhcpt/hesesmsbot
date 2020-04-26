import enum
#used in first prototype
"""class EventType(enum.Enum):
    #These will probably need to be changed
    Sales = 1
    Social = 2
    Criminal = 3
    Political = 4"""

class CommandState(enum.Enum):
    Default = 1
    Setup = 2
    Reporting = 3
    Verifying = 4
    Browsing = 5

class WeatherType(enum.Enum):
    Sunny = 1
    Partly_Cloudy = 2
    Mostly_Cloudy = 3
    Cloudy = 4
    Rainy = 5
    Storming = 6    
    Windy = 7
    Emergency = 8

    
