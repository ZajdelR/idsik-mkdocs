# Oblicz średnią wysokość z CSV

Przygotuj plik `pomiary.csv` z kolumną `wysokosc_km`. Wartości zapisz w kilometrach z kropką dziesiętną. Możesz zacząć od [danych przykładowych](../dane/probki.csv).

Zapisz poniższy kod jako `raport.py` obok `telemetria.py` i `pomiary.csv`.

```python
import csv

from telemetria import srednia_wysokosc

with open("pomiary.csv", encoding="utf-8-sig", newline="") as plik:
    wysokosci = [float(wiersz["wysokosc_km"]) for wiersz in csv.DictReader(plik)]

print(f"Średnia wysokość: {srednia_wysokosc(wysokosci):.1f} km")
```

Uruchom `python raport.py` w katalogu projektu. Dla danych przykładowych wynik to `Średnia wysokość: 520.0 km`. Jeśli funkcja zgłosi `ValueError`, sprawdź [warunki wejściowe](../reference/api.md).
