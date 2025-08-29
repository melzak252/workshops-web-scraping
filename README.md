# Web scraping – start

Zestaw prostych skryptów przygotowanych na warsztaty **Koła Naukowego Data Science Club PJATK**. Materiały mają pomóc rozpocząć pracę z web scrapingiem od realnych przykładów oraz dobrych praktyk.

Web scraping to automatyczne pobieranie danych z serwisów [WWW](http://WWW). Pozwala budować własne zbiory danych do analiz, projektów inżynierskich i magisterskich oraz prototypów ML.

## Zawartość

Repozytorium jest podzielone na trzy foldery, odpowiadające trzem głównym źródłom danych:

• `from_html/` – strony statyczne (Requests + Parsel)
• `from_js/` – strony statyczne, które zawierają dane w JS (Requests + Parsel + Playwright)
• `from_api/` – dane dostępne przez API (XHR/JSON) wykorzystywane przez witryny lub wyłapywanie API przez Playwright. 

Pliki wyjściowe zapisywane są w formacie JSON w katalogu roboczym, np. `quotes_scroll.json`, `books.json`, `authors.json`, `countries.json`.

## Szybki start

Wymagany jest Python 3.10 lub nowszy.

1. Utwórz i aktywuj wirtualne środowisko
   Linux/macOS:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Zainstaluj zależności

   ```bash
   pip install -U pip
   pip install -r requirements.txt
   ```

   Jeśli nie masz `requirements.txt`, użyj:

   ```bash
   pip install requests parsel playwright tqdm
   playwright install
   ```

3. Uruchom skrypty

   ```bash
   python from_html/countries.py
   python from_js/idealwine.py
   ...
   ```

## Start

👉 Zanim uruchomisz gotowe skrypty, polecam spróbować samodzielnie napisać proste scrapery i rozpocząć zabawę z web scrapingiem na stronach treningowych:

- https://www.scrapethissite.com/pages/
- https://toscrape.com


## Dodatkowe wyzwania

Dodatkowe wyzwania

Poza stronami treningowymi warto sprawdzić swoje umiejętności na prawdziwych serwisach, które korzystają z różnych technik dostarczania danych:

### HTML + CSS + (Opcjonalnie) Playwright
- https://www.betclic.pl

### HTML + CSS (proste)

- https://lubimyczytac.pl/katalog/ksiazki

### HTML + CSS (średnie)

- https://www.bricklink.com/catalogList.asp?pg=1&catType=S&v=1
- https://myanimelist.net/topanime.php
- https://gol.gg/tournament/list/

### API 

- https://www.filmweb.pl/search#/film?orderBy=popularity&descending=DESC - 
- https://www.swiatksiazki.pl/ksiazki/ksiazki-3799.html - KSIĄŻKI
- https://www.premierleague.com/en/matches - MECZE PIŁKI NOŻNEJ
- https://www.sts.pl - BUKMACHERKA

### JS/NEXT_DATA

- https://www.imdb.com/event/ev0000003 - OSKARY FILMOWE
- https://www.idealwine.com/en/buy-wine - DANE WIN

Spróbuj samodzielnie zaimplementować scrapery na tych stronach – to świetny sposób, aby zweryfikować swoje umiejętności w różnych scenariuszach.
