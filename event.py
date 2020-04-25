import uuid
import time

class Event:   

    def __init__(self, weatherType, description, location, time):
        #self.headline = headline
        #self.eventType = eventType
        self.description = description
        self.location = location
        self.time = time
        self.weatherType = weatherType
        self.eventId = uuid.uuid1()
        self.verifications = list()

    def numsVerified(self):
        nums = list()
        for ver in self.verifications:
            nums.append(ver.userNum)
        return nums

    def verificationString(self):
        confirmations = 0
        for ver in self.verifications:
            if(ver.verdict):
                confirmations += 1
        return "Certainty: " + str(confirmations*100/len(self.verifications)) + "% with " + str(confirmations) + " verification(s)"
        
