from twilio.rest import Client

# Your Twilio credentials from the console
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="+19705365452",       # Your Twilio number
    to="+91XXXXXXXXXX",         # Your phone number in E.164 format
    body="Hello! This is a test from Twilio 🚀"
)

print(f"Message sent! SID: {message.sid}")

