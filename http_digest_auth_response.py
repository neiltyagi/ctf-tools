#!/usr/bin/python3
import hashlib

qop="auth"
realm="HackIT"
nonce="aUkrF7nsBAA=3b0d48c13dd6d068e844691205593171236635fe"
uri="/t1/"
cnonce="7facec84ad20f49a"
nc="00000001"
username="hackit" 
password="Password1234" 
method="GET"


h1=username+":"+realm+":"+password
h1=hashlib.md5(h1.encode('utf-8')).hexdigest()

h2=method+":"+uri
h2=hashlib.md5(h2.encode('utf-8')).hexdigest()

response=h1+":"+nonce+":"+nc+":"+cnonce+":"+qop+":"+h2
response=hashlib.md5(response.encode('utf-8')).hexdigest()

print(response)

