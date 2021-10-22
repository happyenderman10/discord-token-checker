import requests
from requests import get
token = input("Enter the account token : ")
checker = {
	"Authorization": token
	}
res = requests.post('https://discord.com/api/v9/auth/login', 
headers=checker)

if res.status_code == 200:
    print("The token is Valid!")
if res.status_code == 400:
    print("The token is Invalid")
      
