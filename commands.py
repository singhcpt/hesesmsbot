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
        return TYPE_MESSAGE
    elif(user.getCmdSubState() == 2):
        inValue = -1
        try:
            inValue = int(inputStr)
        except ValueError as e:
            return "please only enter a number"
        
        user.cache.setType(ProductType(inValue))
        
        if (inValue == 1):
            user.setCmdSubState(3)
            return SUBTYPE_FOOD
        elif (inValue == 2):
            user.setCmdSubState(3)
            return SUBTYPE_CLOTHES
        elif (inValue == 3):
            user.setCmdSubState(3)
            return SUBTYPE_FOOTWEAR
        elif (inValue == 4):
            user.setCmdSubState(3)
            return SUBTYPE_BEDDING
        elif (inValue == 5):
            user.setCmdSubState(4)
            return REPORT_MESSAGE3
        else:
            return "pick a listed number"


    elif(user.getCmdSubState() == 3):
        inValue = -1
        try:
            inValue = int(inputStr)
        except ValueError as e:
            return "please only enter a number"

        typ = user.cache.productType
        try:
            if(typ == ProductType.Food):
                user.cache.setSubType(FoodType(inValue))
            elif (typ == ProductType.Clothes):
                user.cache.setSubType(ClothesType(inValue))
            elif (typ == ProductType.Footwear):
                user.cache.setSubType(FootwearType(inValue))
            elif (typ == ProductType.Bedding):
                user.cache.setSubType(BeddingType(inValue))
            else:
                user.cache.setSubType(-1)
        except ValueError as e:
            return "please choose a listed number"

        user.setCmdSubState(4)        
        return REPORT_MESSAGE3
    elif(user.getCmdSubState() == 4):
        user.cache.setLocation(inputStr)
        user.setCmdSubState(5)
        return REPORT_MESSAGE4
    elif(user.getCmdSubState() == 5):
        try:
            int(inputStr)
        except ValueError as e:
            return "Please enter only a number."

        user.cache.setPrice(int(inputStr))
        
        newPost = Post(0, bds.get_user_id(user.number), user.cache.crop, user.cache.productType, user.cache.subType, user.cache.kilograms, user.cache.location, user.cache.price)
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
        return TYPE_MESSAGE
    elif(user.getCmdSubState() == 1):
        inValue = -1
        try:
            inValue = int(inputStr)
        except ValueError as e:
            return "please only enter a number"
        
        try:
            user.cache.setType(ProductType(inValue))
        except ValueError as e:
            return "please choose a listed number"
        
        if (inValue == 1):
            user.setCmdSubState(2)
            return SUBTYPE_FOOD
        elif (inValue == 2):
            user.setCmdSubState(2)
            return SUBTYPE_CLOTHES
        elif (inValue == 3):
            user.setCmdSubState(2)
            return SUBTYPE_FOOTWEAR
        elif (inValue == 4):
            user.setCmdSubState(2)
            return SUBTYPE_BEDDING
        elif (inValue == 5):
            user.setCmdSubState(3)
            return Utilities.createListingString(user.cache.productType, FoodType.Other, user.cache.crop, user)
        else:
            return "pick a listed number"

    elif(user.getCmdSubState() == 2):
        inValue = -1
        try:
            inValue = int(inputStr)
        except ValueError as e:
            return "please only enter a number"

        typ = user.cache.productType
        try:
            if(typ == ProductType.Food):
                user.cache.setSubType(FoodType(inValue))
            elif (typ == ProductType.Clothes):
                user.cache.setSubType(ClothesType(inValue))
            elif (typ == ProductType.Footwear):
                user.cache.setSubType(FootwearType(inValue))
            elif (typ == ProductType.Bedding):
                user.cache.setSubType(BeddingType(inValue))
            else:
                user.cache.setSubType(-1)
        except ValueError as e:
            return "please enter a number listed"

        user.setCmdSubState(3)        
        return Utilities.createListingString(user.cache.productType, user.cache.subType, user.cache.crop, user)

    elif(user.getCmdSubState() == 3):
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
        auth_token = 'update locally'
        client = Client(account_sid, auth_token)

        seller = bds.get_user_by_id(chosenPost.user_id)
        msg = user.name + " has bought " + str(amount) + " units of " + chosenPost.title + "! location: " + user.county + "\nTotal Price is " + str(chosenPost.price*amount) + " KES\nPayment should be made at pickup/dropoff"
        message = client.messages.create(body=msg, from_="+18604847971", to="+" + str(seller.number))

        if(chosenPost.quantity - amount < 1):
            bds.delete_post(user.cache.posts[0].post_id)
        else:
            bds.update_post_quantity(chosenPost.post_id, chosenPost.quantity-amount)
        
        user.updateCmdState(CommandState.Default)
        return LIST_MESSAGE7 + "\nTotal price is " + str(chosenPost.price*amount) + " KES"

def clear():
    events.clear()
    return "Cleared!"
