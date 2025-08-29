import parsel
import requests
import json
from urllib.parse import urljoin
import tqdm

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

PAGES = 50


def get_book_data(book: parsel.Selector):
    """Funkcja odpowiedzialna za ekstrakcję danych o książce."""

    # Podstawowe informacje o książce
    title = book.css("a::attr(title)").get()
    price = book.css(".price_color::text").get()
    book_url = book.css("h3 a::attr(href)").get()
    book_url = urljoin(BASE_URL, book_url)
    rating = book.css(".star-rating::attr(class)").get().split(" ")[-1]

    # Strona książki
    resp = requests.get(book_url)
    resp.raise_for_status()
    book_selector = parsel.Selector(resp.text)

    # Szczegółowe informacje o książce
    genre = book_selector.css(".breadcrumb a::text").getall()[-1].strip()
    book_description = book_selector.css("#product_description + p::text").get()
    book_image = book_selector.css("#product_gallery img::attr(src)").get()
    book_image = urljoin(book_url, book_image)

    # Informacje o produkcie
    table = book_selector.css(".table-striped")
    rows = table.css("tr")
    product_info = {}
    for row in rows:
        key = row.css("th::text").get().strip()
        value = row.css("td::text").get().strip()
        product_info[key] = value

    return {
        "title": title,
        "price": price,
        "url": book_url,
        "description": book_description,
        "image": book_image,
        "rating": rating,
        "genre": genre,
        "product_info": product_info,
    }


books_data = []
for page in range(1, PAGES + 1):
    response = requests.get(BASE_URL.format(page))
    response.raise_for_status()

    html_content = response.text
    selector = parsel.Selector(html_content)

    books = selector.css(".product_pod")
    for book in tqdm.tqdm(books, desc=f"Processing page {page}/{PAGES}"):
        book_info = get_book_data(book)
        books_data.append(book_info)


with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books_data, f, ensure_ascii=False, indent=4)
