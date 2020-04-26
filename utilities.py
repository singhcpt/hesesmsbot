from strings import *
from enums import *
import threading

trigger = threading.Event()
#events = dict()
users = dict()
unsafe = False

class Utilities:

    #eTypeToString = {EventType.Sales: "sales", EventType.Social: "social", EventType.Criminal: "criminal", EventType.Political: "political"} 

    @staticmethod
    def parseCoordinatesFromLink(locationLink):
        i = locationLink.find("(")
        if(i == -1):
            i = locationLink.find("/place/") + 6
            if(i == -1):
                return[-1,-1]
        
        j = locationLink[i:].find(",") + i

        k = locationLink.find(")")
        if(i == -1):
            k = locationLink[j:].find("/") + j
        if(k == -1):
            return [-1,-1]
        #print(i, j, k, locationLink)
        latitude = float(locationLink[i+1:j])
        longitude = float(locationLink[j+1:k])
        return [latitude, longitude]
    @staticmethod
    def createLinkFromCoords(coords):
        locationString = "(" + str(coords[0]) + "," + str(coords[1]) + ")"
        return MAPS_FORMAT_STRING + locationString

    @staticmethod
    def calculateDistance(loc1, loc2):
        return ((loc1[0]-loc2[0])**2 + (loc1[1]-loc2[1])**2)**.5
        


class verification:
    userNum = None
    verdict = False

    def __init__(self, userNum, verdict):
        self.userNum = userNum
        self.verdict = verdict


        
