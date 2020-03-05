import uuid
import time

class Event:
    eventId = 0
    headline = ""
    description = ""
    time = 0.0
    evnetType = -1
    location = [0.0,0.0]
    

    def __init__(self, eventType, headline, description, location, time):
        self.headline = headline
        self.description = description
        self.location = location
        self.time = time
        self.eventType = eventType
        eventId = uuid.uuid1()
        
