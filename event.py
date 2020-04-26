import uuid
import time
from chirpdataservices import *

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

    def verificationString(self):
        confirmations = 0
        verifications = getVerificationsForEvent(self)
        for ver in verifications:
            if(ver.verdict):
                confirmations += 1
        if(len(verifications) == 0):
            return ""
        return "Certainty: " + str(confirmations*100/len(self.verifications)) + "% with " + str(confirmations) + " verification(s)"
        
