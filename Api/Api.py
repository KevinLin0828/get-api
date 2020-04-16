from http.client import HTTPException
from requests.exceptions import MissingSchema
import requests

try:
    date = input("What is the date?Type in YYYY-MM-DD format \n")
    hdInput = input("Do you want your picture in HD?Y/N\n")
    if hdInput == "Y":
        hd = True
    else:
        hd = False
    key = input("What is the Api key?\n")
    userInput = input("What is the url?\n")
    param = {"date": date, "hd": hdInput, "api_key": key}
    r = requests.get(userInput, params=param)
    r.json()
    if r == 200:
        print(r.url)
except MissingSchema:
    print("please type in a valid url with https:// in the front")
except HTTPException:
    print("Error http request failed. ")
except ValueError:
    print("decoding json has failed")
