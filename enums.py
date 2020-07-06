import enum
class EventType(enum.Enum):
    #These will probably need to be changed
    Sales = 1
    Social = 2
    Criminal = 3
    Political = 4

class CommandState(enum.Enum):
    Default = 1
    Setup = 2
    Posting = 3
    Verifying = 4
    Browsing = 5
    
