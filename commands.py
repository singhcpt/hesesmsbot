import bloomdataservices as bds
import time
from user import *
from post import *
from strings import *
from utilities import *

def setup(inputStr, user):
    if(user == None):
        newUser = User()
        newUser.updateCmdState(CommandState.Setup)
        newUser.setCmdSubState(0)
        newUser.setNumber(int(inputStr))
        users[int(inputStr)] = newUser
        return NEW_USER_MESSAGE
    elif(user.getCmdSubState() == 0):
        user.setName(inputStr)
        user.setCmdSubState(1)
        return SETUP_MESSAGE2
    elif(user.getCmdSubState() == 1):
        profession = int(inputStr)
        if profession == 1:
            user.setProfession('buyer')
        elif profession == 2:
            user.setProfession('seller')
        else:
            return SETUP_ERROR_MESSAGE2
        user.setCmdSubState(2)
        return SETUP_MESSAGE3
    elif(user.getCmdSubState() == 2):
        user.setCounty(inputStr)
        user.updateCmdState(CommandState.Default)
        bds.create_user(user)
        return SETUP_MESSAGE4
    return "State out of Range Error (probably stale state)"
    
# add price
def post(inputStr, user):
    if(user.getCmdState() != CommandState.Posting):
        user.updateCmdState(CommandState.Posting)
        user.setCmdSubState(0)
        user.cache.clearCache()
        return REPORT_MESSAGE1
    elif(user.getCmdSubState() == 0):
        user.cache.setCrop(inputStr)
        user.setCmdSubState(1)
        return REPORT_MESSAGE2
    elif(user.getCmdSubState() == 1):
        user.cache.setKilograms(int(inputStr))
        user.setCmdSubState(2)
        return REPORT_MESSAGE3
    elif(user.getCmdSubState() == 2):
        user.cache.setLocation(inputStr)
        user.setCmdSubState(3)
        
        return REPORT_MESSAGE4
    elif(user.getCmdSubState() == 3):
        user.cache.setPrice(int(inputStr))
        user.setCmdSubState(4)
        
        newPost = Post(bds.get_user_id(user.number), user.cache.crop, user.cache.kilograms, user.cache.location, user.cache.price)
        bds.create_post(newPost)

        user.updateCmdState(CommandState.Default)
        return REPORT_MESSAGE5
    return "State out of Range Error (probably stale state)"
    
        
def ls(inputStr, user):
    if(user.getCmdState() != CommandState.Browsing):
        user.updateCmdState(CommandState.Browsing)
        user.setCmdSubState(0)
        user.cache.clearCache()
        return LIST_MESSAGE1        
    elif(user.getCmdSubState() == 0):
        user.cache.setCrop(inputStr)  
        user.setCmdSubState(1)
        return LIST_MESSAGE2
    elif(user.getCmdSubState() == 1):
        user.cache.setLocation(inputStr)
        user.setCmdSubState(2)
        return LIST_MESSAGE3
    elif(user.getCmdSubState() == 2):
        user.cache.setKilograms(int(inputStr))
        user.setCmdSubState(3)
        return LIST_MESSAGE4
    elif(user.getCmdSubState() == 3):
        user.cache.setPrice(int(inputStr))
        user.setCmdSubState(4)
        
        posts = bds.get_posts(user.cache.crop, user.cache.price, user.cache.location)
        
        post_string = ""
        post_count = 1

        for post in posts:
            post_string += "(" + str(post_count) + ") " + str(post) + "\n"

        return LIST_MESSAGE5 + "\n" + post_string

def clear():
    events.clear()
    return "Cleared!"
