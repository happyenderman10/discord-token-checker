import requests
from requests import get
token = input("Enter the account token : ")
checker = {
	"Authorization": token
	}
e = requests.post('https://discord.com/api/v9/auth/login', 
headers=checker)

if e.status_code == 200:
    print("The token is Valid!")
if e.status_code == 400:
    print("The token is Invalid")
      
