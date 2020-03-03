import time
from user import *
from event import *
from strings import *
from utilities import *

def setup(inputStr, user):
    if(user == None):
        newUser = User()
        newUser.updateCmdState(CommandState.Setup)
        newUser.setCmdSubState(0)
        newUser.number = int(inputStr)
        users[int(inputStr)] = newUser
        return NEW_USER_MESSAGE
    elif(user.getCmdSubState() == 0):
        user.initialize(inputStr, user.number)
        user.setCmdSubState(1)
        return SETUP_MESSAGE2
    elif(user.getCmdSubState() == 1):
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
        return SETUP_MESSAGE3
    return "State out of Range Error (probably stale state)"
    

def report(inputStr, user):
    if(user.getCmdState() != CommandState.Reporting):
        user.updateCmdState(CommandState.Reporting)
        user.setCmdSubState(0)
        return REPORT_MESSAGE1
    elif(user.getCmdSubState() == 0):
        user.cache.append(list())
        if("1" in inputStr):
            user.cache[0].append(EventType.Sales)
        elif("2" in inputStr):
            user.cache[0].append(EventType.Social)
        elif("3" in inputStr):
            user.cache[0].append(EventType.Criminal)
        elif("4" in inputStr):
            user.cache[0].append(EventType.Political)
        user.setCmdSubState(1)
        return REPORT_MESSAGE2
    elif(user.getCmdSubState() == 1):
        if(len(inputStr.split(" ")) > 5):
            return REPORT_ERROR1
        user.cache.append(inputStr)
        user.setCmdSubState(2)
        return REPORT_MESSAGE3
    elif(user.getCmdSubState() == 2):
        location = Utilities.parseCoordinatesFromLink(inputStr)
        if(location == [-1,-1]):
            return "Location Formatting Error"
        user.cache.append(location)
        user.setCmdSubState(3)
        return REPORT_MESSAGE4
    elif(user.getCmdSubState() == 3):
        user.cache.append(inputStr)
        newEvent = Event(user.cache[0],user.cache[1],user.cache[2], user.cache[3])
        events[newEvent.eventId] = newEvent;
        user.cache.clear()
        user.updateCmdState(CommandState.Default)
        return REPORT_MESSAGE5
    return "State out of Range Error (probably stale state)"
    
        
def ls(arguments):
    args = arguments.split(",")#could use "  " as delimeter if it is easier
    length = len(args)
    if(args[0] != ''):
        return "list has the incorrect number of arguments"
    out = ""
    for evt in events:
        out += evt[0] + " at " + evt[1] + "\n"
    return out

def clear():
    events.clear()
    return "Cleared!"
