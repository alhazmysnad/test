import requests
import datetime

url = "https://integram.org/webhook/cVDxXgaHVAu"
data = "Test from python script {}".format(datetime.datetime.now())
payload = {'text':data}
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "5259df84-3fad-43c4-bdca-1d35165a7de6"
    }

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)