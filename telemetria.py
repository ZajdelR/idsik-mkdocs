"""Podstawowe statystyki wysokości satelity."""

from math import isfinite
from statistics import mean


def srednia_wysokosc(wysokosci_km: list[float]) -> float:
    """Oblicz średnią arytmetyczną wysokości satelity.

    Args:
        wysokosci_km: Niepusta lista skończonych, nieujemnych wysokości
            w kilometrach, mierzonych względem tej samej powierzchni
            odniesienia.

    Returns:
        Średnia wysokość w kilometrach, z jednakową wagą każdej próbki.

    Raises:
        ValueError: Gdy lista jest pusta lub zawiera ujemną albo
            nieskończoną wartość bądź NaN.

    Examples:
        >>> srednia_wysokosc([510.0, 520.0, 530.0])
        520.0
    """
    if not wysokosci_km:
        raise ValueError("Podaj co najmniej jedną wysokość.")
    if any(not isfinite(wysokosc) or wysokosc < 0 for wysokosc in wysokosci_km):
        raise ValueError("Podaj skończone, nieujemne wysokości w kilometrach.")
    return float(mean(wysokosci_km))
