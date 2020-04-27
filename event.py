import uuid
import time

class Event:   

    def __init__(self, eventId, weatherType, description, location, time):
        #self.headline = headline
        #self.eventType = eventType
        self.description = description
        self.location = location
        self.time = time
        self.weatherType = weatherType
        self.eventId = eventId
        self.verifications = list()
        
