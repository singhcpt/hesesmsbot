from enums import *
from cache import *

class User:

    def __init__(self, number, name = "", baseLocation = [0.0], reliability = 1):
        self.name = ""
        self.number = number
        self.reliability = 1
        self.baseLocation = [0.0,0.0]
        #self.preferences = list()
        self.verifyingEventId = -1
        self.__commandState = CommandState.Default
        self.__cmdSubState = 0
        self.cache = Cache()

    def addPreference(self, addition):
        self.preferences.append(addition)

    def updateCmdState(self, state):
        self.__commandState = state
        __cmdSubState = 0

    def getCmdState(self):
        return self.__commandState

    def setCmdSubState(self, subState):
        self.__cmdSubState = subState

    def getCmdSubState(self):
        return self.__cmdSubState

