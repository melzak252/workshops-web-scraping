"""
Scraper: ładuje nieskończone przewijanie na https://quotes.toscrape.com/scroll i wyłapuje requesty z API
i zapisuje zebrane cytaty do pliku JSON.
"""

import json
import re
from playwright.sync_api import sync_playwright

BASE_URL = "https://quotes.toscrape.com/scroll"

quotes_data = []

with sync_playwright() as p:
    # headless=True dla pracy bez okna przeglądarki; na cele demonstracyjne jest ustawione na False
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(BASE_URL)

    rx = re.compile(
        r"/quotes(?:\?|$)"
    )  # Magiczny regex do wyłapywania requestów z API :P

    # Pętla: czekamy na kolejne odpowiedzi API i przewijamy w dół, aż strona przestanie zwracać dane
    while True:
        try:
            # Czekamy na odpowiedź, której URL pasuje do wzorca rx, i wyciągamy JSON z cytatami
            with page.expect_response(rx, timeout=5000) as response_info:
                quotes = response_info.value.json()["quotes"]
                quotes_data.extend(quotes)
        except Exception as e:
            # Brak kolejnych odpowiedzi lub timeout oznacza koniec danych
            break

        page.mouse.wheel(0, 10000)  # Scroll down

    page.close()
    browser.close()

with open("quotes_scroll.json", "w", encoding="utf-8") as f:
    json.dump(quotes_data, f, ensure_ascii=False, indent=4)
