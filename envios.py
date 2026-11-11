from decimal import Decimal, ROUND_HALF_UP


PESO_MINIMO = Decimal("0")
PESO_MAXIMO = Decimal("50")
LIMITE_TRAMO_1 = Decimal("3")
LIMITE_TRAMO_2 = Decimal("10")
TARIFA_TRAMO_1 = Decimal("6000")
TARIFA_TRAMO_2 = Decimal("9000")
TARIFA_KG_EXTRA = Decimal("800")
RECARGO_RURAL = Decimal("0.20")
RECARGO_NACIONAL = Decimal("0.40")
RECARGO_FINDE = Decimal("2000")
DESCUENTO_FRECUENTE = Decimal("0.05")
DESCUENTO_VIP = Decimal("0.15")
DESCUENTO_EMPRESARIAL = Decimal("0.12")
DESCUENTO_ENVIO10 = Decimal("0.10")
COSTO_MINIMO = Decimal("5000")
UNIDAD_REDONDEO = Decimal("100")
DIA_INICIO = 1
DIA_FIN = 7
DIA_SABADO = 6
CUPON_ENVIO10 = "ENVIO10"


class Zona:
    def recargo(self, total: Decimal) -> Decimal:
        return total


class ZonaUrbana(Zona):
    pass


class ZonaRural(Zona):
    def recargo(self, total: Decimal) -> Decimal:
        return total + total * RECARGO_RURAL


class ZonaNacional(Zona):
    def recargo(self, total: Decimal) -> Decimal:
        return total + total * RECARGO_NACIONAL


ZONAS = {
    "urbana": ZonaUrbana(),
    "rural": ZonaRural(),
    "nacional": ZonaNacional(),
}


class Cliente:
    def descuento(self, total: Decimal) -> Decimal:
        return total

    def aplica_recargo_zona(self, peso: Decimal) -> bool:
        return True


class ClienteNormal(Cliente):
    pass


class ClienteFrecuente(Cliente):
    def descuento(self, total: Decimal) -> Decimal:
        return total - total * DESCUENTO_FRECUENTE


class ClienteVip(Cliente):
    def descuento(self, total: Decimal) -> Decimal:
        return total - total * DESCUENTO_VIP


class ClienteEmpresarial(Cliente):
    def descuento(self, total: Decimal) -> Decimal:
        return total - total * DESCUENTO_EMPRESARIAL

    def aplica_recargo_zona(self, peso: Decimal) -> bool:
        return peso <= LIMITE_TRAMO_2


CLIENTES = {
    "normal": ClienteNormal(),
    "frecuente": ClienteFrecuente(),
    "vip": ClienteVip(),
    "empresarial": ClienteEmpresarial(),
}


def _validar_peso(peso) -> Decimal:
    peso_decimal = Decimal(str(peso))
    if peso_decimal <= PESO_MINIMO or peso_decimal > PESO_MAXIMO:
        raise ValueError("peso inválido")
    return peso_decimal


def _validar_zona(zona) -> Zona:
    if zona not in ZONAS:
        raise ValueError("zona inválida")
    return ZONAS[zona]


def _validar_dia(dia) -> int:
    if dia < DIA_INICIO or dia > DIA_FIN:
        raise ValueError("día inválido")
    return dia


def _tarifa_base(peso: Decimal) -> Decimal:
    if peso < LIMITE_TRAMO_1:
        return TARIFA_TRAMO_1
    if peso <= LIMITE_TRAMO_2:
        return TARIFA_TRAMO_2
    return TARIFA_TRAMO_2 + (peso - LIMITE_TRAMO_2) * TARIFA_KG_EXTRA


def _recargo_finde(dia: int, total: Decimal) -> Decimal:
    if dia >= DIA_SABADO:
        return total + RECARGO_FINDE
    return total


def _descuento_cupon(cupon, total: Decimal) -> Decimal:
    if cupon == CUPON_ENVIO10:
        return total - total * DESCUENTO_ENVIO10
    return total


def _aplicar_minimo(total: Decimal) -> Decimal:
    return max(total, COSTO_MINIMO)


def _redondear(total: Decimal) -> int:
    multiplos = (total / UNIDAD_REDONDEO).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
    return int(multiplos * UNIDAD_REDONDEO)


def calc(p, z, c, d, cup=None):
    peso = _validar_peso(p)
    zona = _validar_zona(z)
    dia = _validar_dia(d)
    cliente = CLIENTES.get(c, CLIENTES["normal"])

    total = _tarifa_base(peso)
    if cliente.aplica_recargo_zona(peso):
        total = zona.recargo(total)
    total = _recargo_finde(dia, total)
    total = cliente.descuento(total)
    total = _descuento_cupon(cup, total)
    total = _aplicar_minimo(total)
    return _redondear(total)
