import requests
from requests import get
token = input("Enter the account token : ")
ttype = input("Enter the token type (user/bot) : ")
if ttype == 'user':
    checker = {
	    "Authorization": token
	    }
    res = requests.post('https://discord.com/api/v9/auth/login', 
    headers=checker)
    if res.status_code == 200:
        print("The token is Valid!")
    if res.status_code == 400:
        print("The token is Invalid")
if ttype == 'bot':
    checker = {
	    "Authorization": f"Bot {token}"
	    }
    res = requests.post('https://discord.com/api/v9/auth/login', 
    headers=checker)
    if res.status_code == 200:
        print("The token is Valid!")
    if res.status_code == 400:
        print("The token is Invalid")
