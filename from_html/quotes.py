import csv
import json
import requests
import parsel
from urllib.parse import urljoin

BASE_URL = "https://quotes.toscrape.com/page/{}"
page = 1
quotes_data = []
author_data = {}  # cache danych autorów, aby nie pobierać wielokrotnie


def get_author_data(author, author_url):
    """Pobiera i cache'uje informacje o autorze ze strony autora."""
    if author in author_data:
        return author_data[author]

    response = requests.get(urljoin(BASE_URL, author_url))
    response.raise_for_status()
    selector = parsel.Selector(response.text)
    birth_date = selector.css(".author-born-date::text").get().strip()
    birth_location = selector.css(".author-born-location::text").get().strip()
    author_description = selector.css(".author-description::text").get().strip()
    return {
        "url": urljoin(BASE_URL, author_url),
        "birth_date": birth_date,
        "birth_location": birth_location,
        "description": author_description,
    }


while True:
    print("Scraping page:", page)
    url = BASE_URL.format(page)
    response = requests.get(url.format(page))
    selector = parsel.Selector(response.text)

    quotes = selector.css(".quote")

    if not quotes:
        break

    for quote in quotes:
        text = quote.css(".text::text").get().strip()
        author = quote.css(".author::text").get().strip()
        tags = quote.css(".tags .tag::text").getall()

        quotes_data.append({"text": text, "author": author, "tags": tags})

        author_url = quote.css("span a::attr(href)").get()
        author_data[author] = get_author_data(author, author_url)

    page += 1

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes_data, f, ensure_ascii=False, indent=4)

with open("authors.json", "w", encoding="utf-8") as f:
    json.dump(author_data, f, ensure_ascii=False, indent=4)
