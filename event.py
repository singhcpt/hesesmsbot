import uuid
import time

class Event:
    eventId = 0
    #headline = ""
    description = ""
    time = 0.0
    #eventType = -1
    weatherType = -1
    location = [0.0,0.0]
    verifications = list()
    

    def __init__(self, weatherType, description, location, time):
        #self.headline = headline
        self.description = description
        self.location = location
        self.time = time
        self.weatherType = weatherType
        self.eventId = uuid.uuid1()

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
        
