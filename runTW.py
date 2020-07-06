# import all the libraries we will be using
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from bot import *
from strings import *

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

    print(request.form.to_dict())
    
    # Create a Twilio response object to be able to send a reply back (as per         # Twilio docs)
    resp = MessagingResponse()

    # Send the message body to the getReply message, where 
    # we will query the String and formulate a response
    replyText = processText(message_body, int(number))

	# Text back our response!
    resp.message(replyText)
    return str(resp)
	
# when you run the code through terminal, this will allow Flask to work
if __name__ == '__main__':
    app.run()
