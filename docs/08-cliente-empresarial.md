# Parte 8 · Cliente empresarial

Estudiante: Martín Alejandro Solano Finol · Código: 0182410126

## 1. Requerimientos nuevos

- **R9**: agregar el cliente empresarial con 12 % de descuento.
- **R10**: si el peso supera 10 kg, no aplicar recargo de zona al cliente empresarial.
- **R11**: aplicar el descuento empresarial antes del cupón.

## 2. Trazabilidad

| Requerimiento | Casos | Qué verifica |
|---|---|---|
| R9 | CE-01, CE-02, CE-05, CE-06 | Descuento del 12 % |
| R10 | CE-03, CE-04, CE-06 | Sin recargo de zona si el peso supera 10 kg; con 10 kg sí se aplica |
| R11 | CE-05, CE-06 | Descuento del cliente antes del cupón |

| Caso | Peso | Zona | Cliente | Día | Cupón | Esperado | Regla |
|---|---|---|---|---|---|---|---|
| CE-01 | 2 | urbana | empresarial | 1 | — | 5300 | R9 |
| CE-02 | 2 | rural | empresarial | 1 | — | 6300 | R9 |
| CE-03 | 12 | nacional | empresarial | 1 | — | 9300 | R10 |
| CE-04 | 10 | nacional | empresarial | 1 | — | 11100 | R10, límite |
| CE-05 | 2 | urbana | empresarial | 1 | ENVIO10 | 5000 | R9, R11, mínimo |
| CE-06 | 12 | rural | empresarial | 6 | ENVIO10 | 10000 | R9, R10, R11, fin de semana |

## 3. Análisis de impacto

Cambios en `envios.py`:

- Nueva constante `DESCUENTO_EMPRESARIAL`.
- Nuevo método `Cliente.aplica_recargo_zona`.
- Nueva clase `ClienteEmpresarial`.
- Registro de `"empresarial"` en `CLIENTES`.
- `calc` consulta la estrategia del cliente antes de aplicar el recargo de zona.

No cambian las validaciones, las tarifas, los recargos de zona, el recargo de fin de semana, el cupón, el mínimo ni el redondeo.

Riesgos y mitigación:

- **Regresión en clientes existentes**: las 86 pruebas anteriores siguen pasando. En el estado rojo pasaron 92 porque incluían las 6 pruebas de la referencia de los casos CE.
- **Límite de 10 kg**: CE-04 prueba el borde exacto y CE-03 prueba un peso mayor.
- **Orden descuento/cupón**: se conserva el orden; `calc` aplica `cliente.descuento` antes de `_descuento_cupon`.
- **Compatibilidad**: los clientes existentes conservan su comportamiento. El cambio es retrocompatible.

## 4. Diseño

Usé el patrón Estrategia que ya existía para los clientes:

- `Cliente` define `descuento` y `aplica_recargo_zona`.
- `ClienteEmpresarial` sobrescribe ambos métodos.
- `calc` no pregunta por el tipo de cliente; delega en la estrategia.

Esto respeta el principio Abierto/Cerrado: agregar un cliente nuevo no obliga a modificar `calc`, solo el registro `CLIENTES`.

## 5. Ciclo rojo-verde

1. Escribí primero los casos CE-01 a CE-06 y actualicé la función de referencia.
2. **Estado rojo**: 6 fallos y 92 pruebas aprobadas. De esas 92, 86 eran las pruebas anteriores y 6 eran las pruebas de la referencia CE. Los fallos fueron CE-01 a CE-06 porque `calc` no conocía el cliente empresarial.
3. Implementé el cliente y la regla de zona.
4. **Estado verde**: 98 pruebas aprobadas.

## 6. Métricas

- Pruebas: 98 aprobadas.
- Cobertura: 100 % de sentencias (97) y 100 % de ramas (16).
- Radon: complejidad máxima 3; `calc` tiene complejidad 2.
- Tamaño: LOC 153, SLOC 108.

## 7. Mantenimiento perfectivo

Este cambio es mantenimiento perfectivo: agrega una funcionalidad nueva y mejora la utilidad del sistema. No corrige un defecto ni adapta el programa a un entorno nuevo. La suite de pruebas y el patrón Estrategia reducen el riesgo de regresión.

## 8. Versión

La versión es `v2.1.0`:

- **MAYOR = 2**: se mantiene la versión mayor de la refactorización.
- **MENOR = 1**: hay funcionalidad nueva y retrocompatible.
- **PARCHE = 0**: no es una corrección.

La API no cambia: `calc(p, z, c, d, cup=None)` sigue igual. El cliente empresarial se selecciona con `c="empresarial"`.

## 9. Archivos modificados

- `envios.py`
- `tests/test_envios.py`
- `CHANGELOG.md`
- `docs/08-cliente-empresarial.md`

## 10. Estado final

- Rama: `feature/cliente-empresarial`.
- Commits: `cca2196` (pruebas), `00551bd` (implementación), `d5ef3d2` (documentación).
- Merge a `main`: `db3eadd`.
- Tag: `v2.1.0`.
- Pruebas: 98 aprobadas.
- Cobertura: 100 % (97 sentencias, 16 ramas).
