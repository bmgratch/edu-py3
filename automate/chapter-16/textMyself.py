#! python3
# textMyself.py - Defines the textmyself() function to text a message
# passed to it as a string
from twilio_values.py import *

# preset values
accountSid = ACCOUNT_SID
authToken = AUTH_TOKEN
myNumber = MY_NUMBER
twilioNumber = TWILIO_NUMBER

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSid, authToken)
    twilioCli.messages.create(
        to=myNumber,
        from_=twilioNumber,
        body=message)
