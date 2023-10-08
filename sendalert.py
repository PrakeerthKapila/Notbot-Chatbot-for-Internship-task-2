#twilio first importing Client
from twilio.rest import Client
#record authentication and sid
sid='Enter your sid from Twilio'
authToken='Enter your authentication Token from Twilio'
client_usr=Client(sid,authToken)
#Passing Message Arguments from,to and body.
message=client_usr.messages.create(body='internship task',from_='whatsapp:+14155238886',to='whatsapp:+YourNumber')
#printing message sid
print(message.sid) 