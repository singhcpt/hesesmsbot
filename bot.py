import time
from user import *
from utilities import *
from commands import *
#from algorithm import *

def isCommand(inputStr):
    if(len(inputStr) == 0):
        return False
    return inputStr[0] == "#"

def processCommand(commandStr, user):
    if(len(user.cache) != 0):
        return "Cache not cleaned correctly abort program"
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
        return ls("")
    elif(commandStr[:end].casefold() == "clear" or commandStr[:end].casefold() == "c"):
        return clear()

def processByState(inputStr, user):
    if(user.getCmdState() == CommandState.Setup):
        return setup(inputStr, user)
    return "Unimplemented"

def processText(inputStr, number):
    if(not number in users):
        return setup(number, None)
    if(isCommand(inputStr)):
        return processCommand(inputStr[1:], users[number])
    #TODO State is not changed by a Command override currently 
    return processByState(inputStr, users[number])


    
