import json
import requests
import parsel

URL = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(URL)
response.raise_for_status()

html_content = response.text
selector = parsel.Selector(html_content)
countries = selector.css(".country")
countries_data = []
for country in countries:
    # Nazwa kraju ma w sobie dodatkowy tag, który utrudnia nam ekstrakcję bezpośrednią
    name = "".join(country.css(".country-name::text").getall()).strip()

    # Dodatkowe informacje o kraju
    capital = "".join(country.css(".country-capital::text").getall()).strip()
    population = country.css(".country-population::text").get().strip()
    area = country.css(".country-area::text").get().strip()

    countries_data.append(
        {
            "name": name,
            "capital": capital,
            "population": int(population),
            "area": float(area),
        }
    )

with open("countries.json", "w", encoding="utf-8") as f:
    json.dump(countries_data, f, ensure_ascii=False, indent=4)
