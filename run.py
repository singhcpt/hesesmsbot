print("print works")
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
        self.username = "BloomPT1"
        self.api_key = "60529f7fc8cb78903800f71b921ad61749b7b0be9dc2d745bd67837be4783bd6"
        #self.api_key = "143eab860f6abdb935e855b402348cd6698fb562e5f67313a2fc85ac94698d61"

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
    shortCode = "22384"
    
    print(replyText)

    service = SMS()
    response = service.sms.send(replyText, recipients, shortCode)
    print(response)
    return str(replyText)
	
# when you run the code through terminal, this will allow Flask to work
if __name__ == '__main__':
    app.run()
