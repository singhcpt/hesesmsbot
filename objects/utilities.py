from constants.strings import *
from constants.enums import *
import database.bloomdataservices as bds

events = dict()
users = dict()
unsafe = False

class Utilities:

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
    def createListingString(type, subtype, title, user):
        posts = bds.get_posts_by_title(title)
        if (len(posts) == 0):
            posts = bds.get_posts_by_subtype(type, subtype)
        user.cache.posts = posts.copy()
        
        post_string = LIST_MESSAGE5 + "\n"
        post_count = 1

        for post in posts:
            post_string += "(" + str(post_count) + ") " + str(post) + "\n"
            post_count += 1

        return post_string
        

    @staticmethod
    def cleanLists():
        return 0
        #should check lists and remove partially created items

        
