# This script scrapes CO2 from ElectricityMap for France country

import requests
import subprocess
import re
import sys

response = requests.get("https://app-backend.electricitymap.org/v6/details/hourly/FR",
headers= {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept" : "*/*",
    "Accept-Language" : "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "electricitymap-token" : "kUp26@Zg4fv$9Pm",
    "x-request-timestamp" : "1688713817661",
    "x-signature" : "e2e3b0d4becf6df4011f9ea0c0d4e027d93c531ea04a1a482d21609785f21081",
    "Sec-Fetch-Dest" : "empty",
    "Sec-Fetch-Mode" : "cors",
    "Sec-Fetch-Site" : "cross-site",
    "Pragma" : "no-cache",
    "Cache-Control" : "no-cache",
    "Referer" : "https://app.electricitymaps.com/",
    'Origin' : 'https://app.electricitymaps.com',
    'TE' : 'trailers'
})

stat = response.json()

# Gets measures dictionary, converts to list of tuple, sorts by timestamp and extracts the last measure
lastMeasure = sorted(stat['data']['zoneStates'].items())[-1]
print(str(lastMeasure[1]['co2intensityProduction']) + ' gCO₂eq/kWh')

# Gets nvidia graphic card consumption
output = subprocess.run(['nvidia-detector'], stdout=subprocess.PIPE, text=True, check=True)

if (None != re.search('^None', output.stdout)):
    print('No nvidia cards')
    sys.exit()
