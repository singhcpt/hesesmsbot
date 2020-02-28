import uuid
import time

class Event:
    eventId = 0
    headline = ""
    description = ""
    time = 0.0
    location = [0.0,0.0]
    

    def __init__(self, headline, description, location, time):
        self.headline = headline
        self.description = description
        self.location = location
        self.time = time
        eventId = uuid.uuid1()
        
