import json
from urllib.request import urlopen

gdzie = input('Podaj lokację: ')

with urlopen(f'https://www.metaweather.com/api/location/search/?query={gdzie}') as file:
   data = json.loads(file.read().decode('utf-8'))

print(data)
woeid = data[0]['woeid']
print(woeid)

with urlopen(f'https://www.metaweather.com/api/location/{woeid}') as f:
   data = json.loads(f.read().decode('utf-8'))

print(data)

pogoda = data["consolidated_weather"]
for prognozy in pogoda:
    print(f"Dzień {prognozy}{[applicable_date]}")
print(pogoda)