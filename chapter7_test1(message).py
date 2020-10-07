from twilio.rest import Client

account_sid = 'ACc95d325d735edd56a356e113c193bbc6'

#權杖，加密用，用來和account_sid搭配，此代表你要有權杖和sid才代表你這個人，只有其中一個沒用。
auth_token = 'a0dfc21fa79151fb27c0c1f193aca1a8'

#twilio是server端，我們去辦帳號是client端
client = Client(account_sid, auth_token) #client是一個物件，型別是Client()

#create()是message這型別內的function。
message = client.messages.create(
	to="+886938582158",
	from_="+14062044739",
	body="你好。")

print(message.sid)