from enums import *

class User:
    name = ""
    number = 0
    reliability = 1
    baseLocation = [0.0,0.0]
    preferences = list()
    __commandState = CommandState.Default
    __cmdSubState = 0
    cache = list()

    def initialize(self, name, number):
        self.name = name
        self.number = number

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

