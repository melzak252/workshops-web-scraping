# Web scraping – start

Zestaw prostych skryptów przygotowanych na warsztaty. To nie są wszystkie przykłady, z jakimi możesz się spotkać, ale pokazuje tu najbardziej podstawowe i edukacyjne scenariusze.

Zestaw prostych skryptów przygotowanych na warsztaty **Koła Naukowego Data Science Club PJATK**. Materiały mają pomóc rozpocząć pracę z web scrapingiem od realnych przykładów oraz dobrych praktyk.

Web scraping to automatyczne pobieranie danych z serwisów [WWW](http://WWW). Pozwala budować własne zbiory danych do analiz, projektów inżynierskich i magisterskich oraz prototypów ML.

## Legalność

Scraping jest co do zasady legalny, ale należy uważać na kwestie takie jak: ochrona danych osobowych (RODO), prawa autorskie i własność intelektualna, prawo konkurencji, bezpieczeństwo systemów IT oraz zakłócanie działania usług.

## Scraper vs Crawler

- Scraper – pobiera dane z określonej strony lub sekcji serwisu.

- Crawler – automatycznie przeszukuje wiele stron, często w sposób szeroki i systematyczny.

## Co warto znać przed startem

- Podstawy HTML (tagi, struktura, atrybuty)
- Nawigację przy pomocy CSS i XPath
- Podstawy pracy z API
- Wyrażenia regularne (regex) do czyszczenia i dopasowania danych

## Zawartość

Repozytorium jest podzielone na trzy foldery, odpowiadające trzem głównym źródłom danych:

- `from_html/` – strony statyczne (Requests + Parsel)

- `from_js/` – strony statyczne, które zawierają dane w JS (Requests + Parsel + Playwright)
- `from_api/` – dane dostępne przez API (XHR/JSON) wykorzystywane przez witryny lub wyłapywanie API przez Playwright. 

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
- https://www.betclic.pl - BUKMACHERKA

### HTML + CSS (proste)

- https://lubimyczytac.pl/katalog/ksiazki - KSIĄŻKI

### HTML + CSS (średnie)

- https://www.bricklink.com/catalogList.asp?pg=1&catType=S&v=1 - KLOCKI LEGO
- https://myanimelist.net/topanime.php - ANIME
- https://gol.gg/tournament/list/ - MECZE ESPORTOWE W LOLA

### API 

- https://www.filmweb.pl/search#/film?orderBy=popularity&descending=DESC - NAJLEPSZE FILMY 
- https://www.swiatksiazki.pl/ksiazki/ksiazki-3799.html - KSIĄŻKI
- https://www.premierleague.com/en/matches - MECZE PIŁKI NOŻNEJ
- https://www.sts.pl - BUKMACHERKA

### JS/NEXT_DATA

- https://www.imdb.com/event/ev0000003 - OSKARY FILMOWE
- https://www.idealwine.com/en/buy-wine - DANE WIN

Spróbuj samodzielnie zaimplementować scrapery na tych stronach – to świetny sposób, aby zweryfikować swoje umiejętności w różnych scenariuszach.

## Wsparcie i konsultacje

Jeśli przygotujesz własny scraper i chcesz feedback, wyślij wiadomość na dsc@pjwstk.edu.pl z `[DSC WS]` w tytule. Pomogę ocenić rozwiązanie i podpowiem, co można ulepszyć.

## Prezentacja

W repozytorium znajdziesz również prezentację z warsztatów. Jest ona poglądowa – większość treści została omówiona ustnie podczas spotkania, więc warto było być obecnym na zajęciach ;)