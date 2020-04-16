#Written Fore HESE 453 2020
import time
from user import *
from utilities import *
from commands import *
#from algorithm import *

def isCommand(inputStr):
    if(inputStr == None or len(inputStr) == 0):
        return False
    return inputStr[0] == "#"

def processCommand(commandStr, user):
    if(len(user.cache) != 0):
        user.cache.clear()
    end = commandStr.find(" ")
    length = len(commandStr)
    if(end == -1):
        end = length
    if(commandStr[:end].casefold() == "report" or commandStr[:end].casefold() == "r"):
        if(end >= length-1):
            return report("", user)
        else:
            return report(commandStr[end+1:])
    elif(commandStr[:end].casefold() == "list" or commandStr[:end].casefold() == "l"):
        return ls("", user)
    elif(commandStr[:end].casefold() == "clear" or commandStr[:end].casefold() == "c"):
        return clear()

def processByState(inputStr, user):
    if(user.getCmdState() == CommandState.Setup):
        return setup(inputStr, user)
    if(user.getCmdState() == CommandState.Reporting):
        return report(inputStr, user)
    if(user.getCmdState() == CommandState.Browsing):
        return ls(inputStr, user)
    return "Unimplemented"

def processText(inputStr, number):
    if(not number in users):
        return setup(number, None)
    if(isCommand(inputStr)):
        return processCommand(inputStr[1:], users[number])
    #TODO State is not changed by a Command override currently 
    return processByState(inputStr, users[number])

def getUserInfo():
    return users

def getEventInfo():
    return events

#Whatsapp workaround
def setLocation(lat, long, number):
    users[number].cache.append([lat, long])
    


    
