import twilio
import twilio.rest

account_sid='ACa2d57349cb39e168488319f97a5e9b9d'
auth_token='f6e9c759b714561b02a9f6d1774136fe'
client=Client(account_token,auth_token)

message=client.messages\
         .create(body='Hello from sois',
                 from_='+12029151874',
                 to='+918275066686'
                 )


print(message.sid)
