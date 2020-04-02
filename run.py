# import all the libraries we will be using
from flask import Flask, request
#from twilio.twiml.messaging_response import MessagingResponse
import africastalking

from bot import *

# set up Flask to connect this code to the local host, which will
# later be connected to the internet through Ngrok
app = Flask(__name__)

class SMS:
    def __init__(self):
    		# Set your app credentials
        self.username = "sandbox"
        self.api_key = "cd971aefc05f7ae634e29e7f92400318b98b93c1ef4cd60da7566f1235b40660"
        # self.api_key = "fd3df98128192a78ec05c50d6ca1c09e88e5a6a09b2a5308a9f3390dac9e21e7"

		# Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        self.sms = africastalking.SMS

    
# Main method. When a POST request is sent to our local host through Ngrok 
# (which creates a tunnel to the web), this code will run. The Twilio service # sends the POST request - we will set this up on the Twilio website. So when # a message is sent over SMS to our Twilio number, this code will run
@app.route('/', methods=['POST'])
def sms():
    # Get the text in the message sent
    print(request.form.to_dict())
    message_body = request.form.get('text')
    number = request.form.get('from')
    i = number.find("+")
    number = number[i+1:]

    recipients = ["+" + number]
    replyText = processText(message_body, int(number))
    #whatsapp only
    if(replyText == REPORT_MESSAGE4):
        if("Latitude" in request.form.keys()):
            setLocation(request.form.get("Latitude"), request.form.get("Longitude"), int(number))
        else:
            replyText = "Location Error"
    shortCode = "3256"
    


    service = SMS()
    service.sms.send(replyText, recipients, shortCode)
    return str(replyText)
	
# when you run the code through terminal, this will allow Flask to work
if __name__ == '__main__':
    app.run()
