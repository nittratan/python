import json
import requests

cityName = input("Enter city name ")
apikey = 'fbfd11ddb85e4d53a8d4145ad68145ca'
apiUrl = f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apikey}&units=metric'
response = requests.get(apiUrl)
print(response.status_code)
data = response.json() # server information
print(data)

jsonData = json.dumps(data, indent = 4)
print(jsonData)

# to fetch specific data from json
print(data['main']['temp'])

print(data['weather'][0]['description'])
