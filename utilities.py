from strings import *
from enums import *

events = dict()
users = dict()
unsafe = False

class Utilities:

    eTypeToString = {EventType.Sales: "sales", EventType.Social: "social", EventType.Criminal: "criminal", EventType.Political: "political"} 

    @staticmethod
    def parseCoordinatesFromLink(locationLink):
        i = locationLink.find("(")
        j = locationLink.find(",")
        k = locationLink.find(")")
        print(i, j, k, locationLink)
        latitude = float(locationLink[i+1:j])
        longitude = float(locationLink[j+1:k])
        return [latitude, longitude]
    @staticmethod
    def createLinkFromCoords(coords):
        locationString = "(" + str(coords[0]) + "," + str(coords[1]) + ")"
        return MAPS_FORMAT_STRING + locationString
        

    @staticmethod
    def cleanLists():
        return 0
        #should check lists and remove partially created items

        
