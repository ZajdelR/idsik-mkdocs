# Satellite Telemetry · MkDocs i Diátaxis

Projekt oblicza średnią z przykładowych wysokości satelity. Dokumentacja odpowiada na cztery różne potrzeby czytelnika.

- [Samouczek](docs/tutorials/pierwsza-analiza.md) prowadzi przez pierwszą analizę.
- [Instrukcja](docs/how-to/wysokosci-z-csv.md) pokazuje, jak obliczyć średnią z własnego CSV.
- [Referencja](docs/reference/api.md) wskazuje obiekt, którego docstring przetwarza `mkdocstrings`.
- [Wyjaśnienie](docs/explanation/srednia-a-probkowanie.md) omawia wpływ próbkowania na interpretację średniej.

## Środowisko wirtualne

Otwórz terminal w katalogu projektu, obok pliku `telemetria.py`. Utwórz środowisko `.venv` za pomocą Pythona 3.12, a następnie je aktywuj.

**Windows (PowerShell)**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS i Linux**

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Przy ponownym otwarciu terminala wystarczy wykonać polecenie aktywacji. Aby opuścić środowisko, wpisz `deactivate`.

## Uruchomienie

Po aktywacji środowiska zainstaluj zależności, uruchom doctest i włącz podgląd.

```powershell
python -m pip install -r requirements-docs.txt
python -m doctest -v telemetria.py
python -m mkdocs serve --watch telemetria.py
```

Otwórz [lokalny podgląd](http://127.0.0.1:8000/). Zmień pierwsze zdanie docstringa funkcji `srednia_wysokosc` i sprawdź referencję API. Następnie zatrzymaj podgląd przez Ctrl+C i zbuduj witrynę.

```powershell
python -m mkdocs build --strict
```

Gotowe pliki HTML pojawią się w `site/`. W konfiguracji jest wbudowany motyw MkDocs.

[MkDocs — Getting Started](https://www.mkdocs.org/getting-started/) · [mkdocstrings dla Pythona](https://mkdocstrings.github.io/python/usage/)
