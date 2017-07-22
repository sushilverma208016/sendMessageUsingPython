
from twilio.rest import Client

account_sid = "AC732364900f7d394645da00ffcdfccb08"
auth_token = "<TWILIO AUTH TOKEN>"
to_= "+91<YOUR NUMBER>"
from_= "+14155275117"
body_= "My dummy message"

client = Client(account_sid, auth_token)

client.messages.create(
    to= to_,
    from_= from_,
    body= body_)
print "done" 
