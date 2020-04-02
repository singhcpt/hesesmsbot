import uuid
import time

class Event:
    eventId = 0
    headline = ""
    description = ""
    time = 0.0
    eventType = -1
    location = [0.0,0.0]
    

    def __init__(self, eventType, headline, description, location, time):
        self.headline = headline
        self.description = description
        self.location = location
        self.time = time
        self.eventType = eventType
        self.eventId = uuid.uuid1()
        
