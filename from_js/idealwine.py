import requests
import parsel
import json

BASE_URL = "https://www.idealwine.com/en/buy-wine"

response = requests.get(BASE_URL)

selector = parsel.Selector(response.text)

# Tag z danymi :P
json_str = selector.css("#__NEXT_DATA__::text").get()

data = json.loads(json_str)

with open("idealwine.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
