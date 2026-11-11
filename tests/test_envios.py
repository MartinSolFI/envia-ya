from decimal import Decimal, ROUND_HALF_UP

import pytest

from envios import calc


CIEN = Decimal("100")


def referencia(p, z, c, d, cup=None):
    peso = Decimal(str(p))
    if peso <= 0 or peso > 50:
        raise ValueError("peso inválido")
    if z not in ("urbana", "rural", "nacional"):
        raise ValueError("zona inválida")
    if d < 1 or d > 7:
        raise ValueError("día inválido")

    if peso < 3:
        total = Decimal("6000")
    elif peso <= 10:
        total = Decimal("9000")
    else:
        total = Decimal("9000") + (peso - Decimal("10")) * Decimal("800")

    aplica_zona = not (c == "empresarial" and peso > Decimal("10"))
    if aplica_zona:
        if z == "rural":
            total = total * Decimal("1.20")
        elif z == "nacional":
            total = total * Decimal("1.40")

    if d >= 6:
        total = total + Decimal("2000")

    if c == "frecuente":
        total = total * Decimal("0.95")
    elif c == "vip":
        total = total * Decimal("0.85")
    elif c == "empresarial":
        total = total * Decimal("0.88")

    if cup == "ENVIO10":
        total = total * Decimal("0.90")

    if total < Decimal("5000"):
        total = Decimal("5000")

    return int((total / CIEN).quantize(Decimal("1"), rounding=ROUND_HALF_UP) * CIEN)


CASOS_VALIDOS = [
    ("CN-04", {"p": 50, "z": "urbana", "c": "normal", "d": 1}, 41000),
    ("CN-08", {"p": 0.1, "z": "urbana", "c": "normal", "d": 1}, 6000),
    ("CN-09", {"p": 2.9, "z": "urbana", "c": "normal", "d": 1}, 6000),
    ("CN-10", {"p": 3, "z": "urbana", "c": "normal", "d": 3}, 9000),
    ("CN-11", {"p": 10, "z": "urbana", "c": "normal", "d": 2}, 9000),
    ("CN-12", {"p": 10.1, "z": "urbana", "c": "normal", "d": 2}, 9100),
    ("CN-13", {"p": 20, "z": "urbana", "c": "normal", "d": 2}, 17000),
    ("CN-14", {"p": 6, "z": "rural", "c": "normal", "d": 3}, 10800),
    ("CN-15", {"p": 6, "z": "nacional", "c": "normal", "d": 3}, 12600),
    ("CN-16", {"p": 12, "z": "nacional", "c": "normal", "d": 2}, 14800),
    ("CN-17", {"p": 2, "z": "urbana", "c": "normal", "d": 6}, 8000),
    ("CN-18", {"p": 2, "z": "rural", "c": "normal", "d": 7}, 9200),
    ("CN-19", {"p": 2, "z": "rural", "c": "vip", "d": 6, "cup": "ENVIO10"}, 7000),
    ("CN-20", {"p": 2, "z": "urbana", "c": "frecuente", "d": 1}, 5700),
    ("CN-21", {"p": 10, "z": "urbana", "c": "vip", "d": 1, "cup": "ENVIO10"}, 6900),
    ("CN-22", {"p": 2, "z": "urbana", "c": "normal", "d": 1, "cup": "ENVIO10"}, 5400),
    ("CN-23", {"p": 2, "z": "urbana", "c": "normal", "d": 1, "cup": "XYZ"}, 6000),
    ("CN-24", {"p": 0.1, "z": "urbana", "c": "vip", "d": 1, "cup": "ENVIO10"}, 5000),
    ("CN-25", {"p": 12, "z": "nacional", "c": "frecuente", "d": 7}, 16000),
    ("CN-26", {"p": 3, "z": "urbana", "c": "frecuente", "d": 1}, 8600),
    ("CB-01", {"p": 2, "z": "urbana", "c": "normal", "d": 1}, 6000),
    ("CB-04", {"p": 6, "z": "urbana", "c": "normal", "d": 1}, 9000),
    ("CB-05", {"p": 12, "z": "urbana", "c": "normal", "d": 1}, 10600),
    ("CB-06", {"p": 2, "z": "rural", "c": "normal", "d": 1}, 7200),
    ("CB-07", {"p": 2, "z": "nacional", "c": "normal", "d": 1}, 8400),
    ("CB-09", {"p": 2, "z": "urbana", "c": "normal", "d": 7}, 8000),
    ("CB-10", {"p": 2, "z": "urbana", "c": "frecuente", "d": 1}, 5700),
    ("CB-11", {"p": 2, "z": "urbana", "c": "vip", "d": 1}, 5100),
    ("CB-12", {"p": 2, "z": "urbana", "c": "normal", "d": 1, "cup": "XYZ"}, 6000),
    ("CB-13", {"p": 2, "z": "urbana", "c": "normal", "d": 1, "cup": "ENVIO10"}, 5400),
    ("CB-14", {"p": 1, "z": "urbana", "c": "vip", "d": 1, "cup": "ENVIO10"}, 5000),
    ("CB-15", {"p": 2, "z": "urbana", "c": "normal", "d": 1}, 6000),
    ("CB-16", {"p": 6, "z": "rural", "c": "frecuente", "d": 7, "cup": "ENVIO10"}, 10900),
    ("CB-17", {"p": 12, "z": "nacional", "c": "vip", "d": 1}, 12600),
    ("CE-01", {"p": 2, "z": "urbana", "c": "empresarial", "d": 1}, 5300),
    ("CE-02", {"p": 2, "z": "rural", "c": "empresarial", "d": 1}, 6300),
    ("CE-03", {"p": 12, "z": "nacional", "c": "empresarial", "d": 1}, 9300),
    ("CE-04", {"p": 10, "z": "nacional", "c": "empresarial", "d": 1}, 11100),
    ("CE-05", {"p": 2, "z": "urbana", "c": "empresarial", "d": 1, "cup": "ENVIO10"}, 5000),
    ("CE-06", {"p": 12, "z": "rural", "c": "empresarial", "d": 6, "cup": "ENVIO10"}, 10000),
]

CASOS_INVALIDOS = [
    ("CN-01", {"p": 0, "z": "urbana", "c": "normal", "d": 1}, "peso inválido"),
    ("CN-02", {"p": -1, "z": "urbana", "c": "normal", "d": 1}, "peso inválido"),
    ("CN-03", {"p": 50.1, "z": "urbana", "c": "normal", "d": 1}, "peso inválido"),
    ("CN-05", {"p": 2, "z": "aérea", "c": "normal", "d": 1}, None),
    ("CN-06", {"p": 2, "z": "urbana", "c": "normal", "d": 0}, None),
    ("CN-07", {"p": 2, "z": "urbana", "c": "normal", "d": 8}, None),
    ("CB-02", {"p": 0, "z": "urbana", "c": "normal", "d": 1}, "peso inválido"),
    ("CB-03", {"p": 51, "z": "urbana", "c": "normal", "d": 1}, "peso inválido"),
    ("CB-08", {"p": 2, "z": "aérea", "c": "normal", "d": 1}, None),
]


@pytest.mark.parametrize(
    "caso, kwargs, esperado",
    CASOS_VALIDOS,
    ids=[caso[0] for caso in CASOS_VALIDOS],
)
def test_costo_esperado(caso, kwargs, esperado):
    assert calc(**kwargs) == esperado


@pytest.mark.parametrize(
    "caso, kwargs, mensaje",
    CASOS_INVALIDOS,
    ids=[caso[0] for caso in CASOS_INVALIDOS],
)
def test_error_esperado(caso, kwargs, mensaje):
    if mensaje is None:
        with pytest.raises(ValueError):
            calc(**kwargs)
    else:
        with pytest.raises(ValueError, match=mensaje):
            calc(**kwargs)


@pytest.mark.parametrize(
    "caso, kwargs, esperado",
    CASOS_VALIDOS,
    ids=[caso[0] for caso in CASOS_VALIDOS],
)
def test_referencia_casos_validos(caso, kwargs, esperado):
    assert referencia(**kwargs) == esperado


@pytest.mark.parametrize(
    "caso, kwargs, mensaje",
    CASOS_INVALIDOS,
    ids=[caso[0] for caso in CASOS_INVALIDOS],
)
def test_referencia_casos_invalidos(caso, kwargs, mensaje):
    if mensaje is None:
        with pytest.raises(ValueError):
            referencia(**kwargs)
    else:
        with pytest.raises(ValueError, match=mensaje):
            referencia(**kwargs)
