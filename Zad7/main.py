import requests
from utils.Brawery import Brawery

api_url = 'https://api.openbrewerydb.org/breweries'
response = requests.get(api_url)
json = response.json()
firstTwenty = json[:20]
for i in firstTwenty:
    print(i['id'])
