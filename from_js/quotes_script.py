import json
import parsel
import requests
import re

URL = "https://quotes.toscrape.com/js/page/{}/"

quotes_data = []
for page in range(1, 6):
    print("Scraping page:", page)
    response = requests.get(URL.format(page))
    response.raise_for_status()

    selector = parsel.Selector(response.text)

    script = selector.css("script::text")
    script = script[0].get()

    data = re.search(
        r"var data = (\[[\s\S]*?\])(?=\s*;)", script, re.DOTALL
    )  # Regex magic - Pobiera dane w formacie JSON z tagu <script>

    json_data = data.group(1)
    data = json.loads(json_data)

    quotes_data.extend(data)

with open("quotes_script.json", "w", encoding="utf-8") as f:
    json.dump(quotes_data, f, ensure_ascii=False, indent=4)
