# Pierwsza analiza wysokości satelity

Obliczysz średnią z trzech przykładowych pomiarów. Zacznij w katalogu projektu zawierającym `telemetria.py`.

## 1. Uruchom interpreter

Wpisz w terminalu `python`.

## 2. Oblicz średnią z trzech próbek

Zaimportuj funkcję, zapisz próbki i oblicz średnią.

```pycon
>>> from telemetria import srednia_wysokosc
>>> probki = [510.0, 520.0, 530.0]
>>> srednia_wysokosc(probki)
520.0
```

## 3. Dodaj kolejną próbkę

Dodaj pomiar `540.0` i sprawdź, jak zmieni się wynik.

```pycon
>>> probki.append(540.0)
>>> srednia_wysokosc(probki)
525.0
```

Teraz możesz użyć tej samej funkcji do [odczytu własnych próbek z CSV](../how-to/wysokosci-z-csv.md).
