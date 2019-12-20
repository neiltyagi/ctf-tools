#!/usr/bin/python3
import base64
print("1.For generating a basic Auth header \n2.For decoding a basic Auth Header ")
a=int(input("option>"))

if a==1 :
	username=input("enter username=")
	password=input("enter password=")
	h1=username+":"+password
	message_bytes = h1.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
	header="Authorisation: "+"Basic " + base64_message
	print(header)

elif a==2:
	token=input("enter Base64 token after Basic=")
	base64_bytes = token.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	message = message_bytes.decode('ascii')
	username,password=message.split(":")
	print("username=",username)
	print("password=",password)






