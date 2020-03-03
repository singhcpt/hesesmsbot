#in format (Thing, Where, When)
events = dict()
users = dict()
unsafe = False

class Utilities:

    @staticmethod
    def parseCoordinatesFromLink(locationLink):
        i = locationLink.find("(")
        j = locationLink.find(",")
        k = locationLink.find(")")
        latitude = float(locationLink[i+1:j])
        longitude = float(locationLink[j+1:k])
        return [latitude, longitude]

    @staticmethod
    def cleanLists():
        return 0
        #should check lists and remove partially created items

        
