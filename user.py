from enums import *
from cache import *

class User:
    
    def __init__(self, name="", number=0, reliability=0, county="", profession=""):
        self.name = name
        self.number = number
        self.reliability = reliability
        self.county = county
        self.profession = profession
        self.__commandState = CommandState.Default
        self.__cmdSubState = 0
        self.cache = Cache()

    def updateCmdState(self, state):
        self.__commandState = state
        __cmdSubState = 0

    def getCmdState(self):
        return self.__commandState

    def setCmdSubState(self, subState):
        self.__cmdSubState = subState

    def getCmdSubState(self):
        return self.__cmdSubState
    
    def setName(self, name):
        self.name = name
        return
    
    def getName(self):
        return self.name
    
    def setNumber(self, number):
        self.number = number
        return
    
    def getNumber(self):
        return self.number
    
    def getReliability(self):
        return self.reliability
    
    def setProfession(self, profession):
        self.profession = profession
        return
    
    def getProfession(self):
        return self.profession

    def setCounty(self, county):
        self.county = county
        return

    def getCounty(self):
        return self.county