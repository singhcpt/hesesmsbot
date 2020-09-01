# import all the libraries we will be using
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import asyncio

from bot import *
from strings import *
from user import *
from event import *
from utilities import *

# set up Flask to connect this code to the local host, which will
# later be connected to the internet through Ngrok
app = Flask(__name__)
    
# Main method. When a POST request is sent to our local host through Ngrok 
# (which creates a tunnel to the web), this code will run. The Twilio service # sends the POST request - we will set this up on the Twilio website. So when # a message is sent over SMS to our Twilio number, this code will run
@app.route('/', methods=['POST'])
def sms():
    # Get the text in the message sent
    message_body = request.form.get('Body')
    number = request.form.get('From')
    i = number.find("+")
    number = number[i+1:]
    
    # Create a Twilio response object to be able to send a reply back (as per         # Twilio docs)
    resp = MessagingResponse()

    # Send the message body to the getReply message, where 
    # we will query the String and formulate a response
    replyText = processText(message_body, int(number))

    #whatsapp only
    """if(replyText == REPORT_MESSAGE4):
        if("Latitude" in request.form.keys()):
            setLocation(float(request.form.get("Latitude")), float(request.form.get("Longitude")), int(number))
        else:
            replyText = "Location Error";"""
	# Text back our response!
    resp.message(replyText)
    return str(resp)

def validate():
    account_sid = 'AC50b76a11d713b405f2c1f4d120ed0d5e'
    auth_token = '216f6cf46184c4888234573c552ca821'
    client = Client(account_sid, auth_token)

    while(trigger.wait()):
        print("hit")
        trigger.clear()
        events = get_events()
        recentEvent = list(events.values())[0]
        for event in events.values():
            if(event.time > recentEvent.time):
                recentEvent = event
        for user in users.values():
            if(user.number not in get_users_verified(recentEvent.eventId) or ((user.baseLocation[0]-recentEvent.location[0])**2 + (user.baseLocation[1]-recentEvent.location[1])**2)**.5 < 0.00101035615 and user.verifyingEventId == -1):
                msg = VALIDATE_MESSAGE + "\n\n" + str(WeatherType(recentEvent.weatherType)) + "\n" + recentEvent.description + "\nReport Location: " + Utilities.createLinkFromCoords(recentEvent.location)
                message = client.messages.create(body=msg, from_="+18604847971", to="+" + str(user.number))
                user.cache.eventId = recentEvent.eventId
                user.updateCmdState(CommandState.Verifying)
                user.verifyingEventId = recentEvent.eventId


	
# when you run the code through terminal, this will allow Flask to work
if __name__ == '__main__': 
    task = threading.Thread(None, validate)
    task.start()
    app.run()
    task.join()
