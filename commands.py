import time
import sys
from user import *
from event import *
from strings import *
from utilities import *
from chirpdataservices import *

def setup(inputStr, user):
    if(user == None):
        newUser = User(int(inputStr))
        newUser.updateCmdState(CommandState.Setup)
        newUser.setCmdSubState(0)
        users[int(inputStr)] = newUser
        return NEW_USER_MESSAGE
    elif(user.getCmdSubState() == 0):
        location = Utilities.parseCoordinatesFromLink(inputStr)
        if(location == [-1,-1]):
            return "Location Formatting Error"
        user.baseLocation = location
        user.updateCmdState(CommandState.Default)
        return SETUP_MESSAGE3

    #used in first prototype
    """elif(user.getCmdSubState() == 1):
        choices = inputStr.split(",")
        for choice in choices:
            if("1" in choice.casefold()):
                user.addPreference(EventType.Sales)
            elif("2" in choice.casefold()):
                user.addPreference(EventType.Social)
            elif("3" in choice.casefold()):
                user.addPreference(EventType.Criminal)
            elif("4" in choice.casefold()):
                user.addPreference(EventType.Political)
        user.updateCmdState(CommandState.Default)
        return SETUP_MESSAGE3"""

    return "State out of Range Error (probably stale state)"
    

def report(inputStr, user):
    if(user.getCmdState() != CommandState.Reporting):
        user.updateCmdState(CommandState.Reporting)
        user.setCmdSubState(0)
        return REPORT_MESSAGE1
    elif(user.getCmdSubState() == 0):
        if("1" in inputStr):
            user.cache.weatherType = WeatherType.Sunny
        elif("2" in inputStr):
            user.cache.weatherType = WeatherType.Partly_Cloudy
        elif("3" in inputStr):
            user.cache.weatherType = WeatherType.Mostly_Cloudy
        elif("4" in inputStr):
            user.cache.weatherType = WeatherType.Cloudy
        elif("5" in inputStr):
            user.cache.weatherType = WeatherType.Rainy
        elif("6" in inputStr):
            user.cache.weatherType = WeatherType.Storming
        elif("7" in inputStr):
            user.cache.weatherType = WeatherType.Windy
        elif("8" in inputStr):
            user.cache.weatherType = WeatherType.Emergency
        else:
            return "you must choose one."
        user.setCmdSubState(1)
        return REPORT_MESSAGE2
    elif(user.getCmdSubState() == 1):
        if(len(inputStr) > 100):
            return REPORT_ERROR1
        if(len(inputStr) == 1 and "0" in inputStr):
            user.cache.description = ""
        else:
            user.cache.description = inputStr
        newEvent = Event(1, user.cache.weatherType, user.cache.description, user.baseLocation, str(datetime.now())[:-7])
        create_event(newEvent)
        trigger.set()
        user.updateCmdState(CommandState.Default)
        return REPORT_MESSAGE5
    
    #used in first prototype
    """elif(user.getCmdSubState() == 2):
        #for sms:
        location = Utilities.parseCoordinatesFromLink(inputStr)
        if(location == [-1,-1]):
            return "Location Formatting Error"
        user.cache.append(location)
        user.setCmdSubState(3)
        return REPORT_MESSAGE4
    elif(user.getCmdSubState() == 3):
        user.cache.append(inputStr)
        newEvent = Event(user.cache[0],user.cache[1],user.cache[3], user.cache[2], time.time())
        events[newEvent.eventId] = newEvent;
        trigger.set()
        user.updateCmdState(CommandState.Default)
        return REPORT_MESSAGE5"""

    return "State out of Range Error (probably stale state)"
    
        
def ls(inputStr, user):
    if(user.getCmdState() != CommandState.Browsing):
        shortest = sys.maxsize
        closestEvent = None
        events = get_events()
        for event in events.values():
            eventDist = Utilities.calculateDistance(event.location, user.baseLocation)
            if(eventDist < shortest):
                shortest = eventDist
                closestEvent = event
        if(closestEvent is None):
            return "No Weather Reported"
        verifications = get_verifications(closestEvent.eventId)
        
        return LIST_MESSAGE2 + "\n\n" + str(WeatherType(closestEvent.weatherType))[11:] + "\nDescription:\n" + closestEvent.description + "\nReport Location: " + Utilities.createLinkFromCoords(closestEvent.location) + "\n" + Utilities.verificationString(verifications) 

    """elif(user.getCmdSubState() == 0):
        eType = -1
        if("1" in inputStr):
            eType = EventType.Sales
        elif("2" in inputStr):
            eType = EventType.Social
        elif("3" in inputStr):
            eType = EventType.Criminal
        elif("4" in inputStr):
            eType = EventType.Political
        out = ""
        out += LIST_MESSAGE2 + Utilities.eTypeToString[eType] + " events." #dont hardcode this -TODO
        print(events)
        i = 1
        for uid in events:
            if(events[uid].eventType == eType):
                out+= "\n\n(" + str(i) + ")" + events[uid].headline + "\nat " + Utilities.createLinkFromCoords(events[uid].location)
                user.cache.append(events[uid])
                i += 1                
        user.setCmdSubState(1)
        return out + "\n" + LIST_MESSAGE3
    elif(user.getCmdSubState() == 1):
        try:
            if(int(inputStr) > len(user.cache) or int(inputStr) <= 0):
                user.updateCmdState(CommandState.Default)
                return ""
            return user.cache[int(inputStr)-1].description
        except ValueError as e:
            user.updateCmdState(CommandState.Default)
            return "";"""
    return "State out of Range Error (probably stale state)"

def verify(inputStr, user):
    verdict = False
    if("1" in inputStr):
        verdict = True
    events = get_events()
    event = events[user.cache.eventId]
    create_verification(event.eventId, user.number, verdict)
    return VERIFY_MESSAGE

