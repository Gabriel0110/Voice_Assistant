from twilio.rest import Client

# put your own credentials here
account_sid = "insert_ID"
auth_token = "insert_token"

client = Client(account_sid, auth_token)

def sendText(message):
	client.messages.create(
	  to="insert_destination_number",
	  from_="insert_your_twilio_number",
	  body=message)
