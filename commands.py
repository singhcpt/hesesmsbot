import database.bloomdataservices as bds
import time
from objects.user import *
from objects.post import *
from constants.strings import *
from objects.utilities import *
from twilio.rest import Client

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
        profession = 0
        try:
            profession = int(inputStr)
        except ValueError as e:
            return SETUP_ERRORMESSAGE2

        if profession == 1:
            user.setProfession('buyer')
        elif profession == 2:
            user.setProfession('seller')
        else:
            return SETUP_ERRORMESSAGE2
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
        try:
            float(inputStr)
        except ValueError as e:
            return "please only enter a number"

        user.cache.setKilograms(float(inputStr))
        user.setCmdSubState(2)
        return REPORT_MESSAGE3
    elif(user.getCmdSubState() == 2):
        user.cache.setLocation(inputStr)
        user.setCmdSubState(3)
        return REPORT_MESSAGE4
    elif(user.getCmdSubState() == 3):
        try:
            int(inputStr)
        except ValueError as e:
            return "Please enter only a number."

        user.cache.setPrice(int(inputStr))
        user.setCmdSubState(4)
        
        newPost = Post(0, bds.get_user_id(user.number), user.cache.crop, user.cache.kilograms, user.cache.location, user.cache.price)
        bds.create_post(newPost)

        user.updateCmdState(CommandState.Default)
        return REPORT_MESSAGE5
    return "State out of Range Error (probably stale state)"
    
        
def ls(inputStr, user):
    if(user.getCmdState() != CommandState.Browsing):
        user.updateCmdState(CommandState.Browsing)
        user.setCmdSubState(3)
        user.cache.clearCache()
        return LIST_MESSAGE1        
    # elif(user.getCmdSubState() == 0):
    #     user.cache.setCrop(inputStr)  
    #     user.setCmdSubState(3)
    #     return LIST_MESSAGE2
    # elif(user.getCmdSubState() == 1):
    #     user.cache.setLocation(inputStr)
    #     user.setCmdSubState(2)
    #     return LIST_MESSAGE3
    # elif(user.getCmdSubState() == 2):
    #     user.cache.setKilograms(float(inputStr))
    #     user.setCmdSubState(3)
    #     return LIST_MESSAGE4
    elif(user.getCmdSubState() == 3):
        user.cache.setCrop(inputStr)
        user.setCmdSubState(4)
        
        posts = bds.get_posts_by_type(user.cache.crop)
        user.cache.posts = posts.copy()
        
        post_string = ""
        post_count = 1

        for post in posts:
            post_string += "(" + str(post_count) + ") " + str(post) + "\n"

        return LIST_MESSAGE5 + "\n" + post_string
    elif(user.getCmdSubState() == 4):
        if(inputStr.casefold() == "none"):
            user.updateCmdState(CommandState.Default)
            return LIST_MESSAGE6

        postNum = 0
        try:
            postNum = int(inputStr)
        except ValueError as e:
            return LIST_ERRORMESSAGE5
        
        if(postNum > len(user.cache.posts) or postNum < 1):
            return LIST_ERRORMESSAGE5

        selectedPost = user.cache.posts[postNum-1]
        user.cache.posts = [selectedPost]

        user.setCmdSubState(5)
        return LIST_MESSAGE3

    elif(user.getCmdSubState() == 5):
        #update table and notify seller
        chosenPost = user.cache.posts[0]
        amount = 0
        try:
            amount = float(inputStr)
        except ValueError as e:
            return "please enter as only a number"

        if(amount > chosenPost.quantity or amount < 0):
            return "that amount is not available, please choose again"        

        account_sid = 'AC50b76a11d713b405f2c1f4d120ed0d5e'
        auth_token = '713a0a523ee484949c56164b944156f0'
        client = Client(account_sid, auth_token)

        seller = bds.get_user_by_id(chosenPost.user_id)
        msg = user.name + " has bought " + str(amount) + " kilograms of " + chosenPost.crop + "! location: " + user.county + "\nPayment should be made at pickup/dropoff"
        message = client.messages.create(body=msg, from_="+18604847971", to="+" + str(seller.number))

        if(chosenPost.quantity - amount < 1):
            bds.delete_post(user.cache.posts[0].post_id)
        else:
            bds.update_post_quantity(chosenPost.post_id, chosenPost.quantity-amount)
        
        user.updateCmdState(CommandState.Default)
        return LIST_MESSAGE7

def clear():
    events.clear()
    return "Cleared!"
