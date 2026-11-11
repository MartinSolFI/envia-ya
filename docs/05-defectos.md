# Parte 5 · Pruebas automatizadas y defectos

Estudiante: Martín Alejandro Solano Finol · Código: 0182410126

## 1. Qué hice

- Creé la rama `test/suite`.
- Automaticé los 26 casos CN y los 17 casos CB en `tests/test_envios.py`.
- Escribí los resultados esperados a mano, tomados de `03b-matriz-casos.md` y `04b-caminos-cobertura.md`.
- Agregué una implementación de referencia independiente con `Decimal` y `ROUND_HALF_UP` para verificar esos 43 resultados.
- Ejecuté las pruebas contra el código heredado `v1.0.0` sin modificar `envios.py`.

La referencia coincide con los 43 resultados documentados. Por eso los fallos que aparecen son del código heredado y no de los valores esperados.

## 2. Comandos ejecutados

```powershell
git switch -c test/suite
python -m pytest tests -v
python -m pytest --cov=envios --cov-branch --cov-report=term-missing -q
```

## 3. Resultado de la ejecución

| Métrica | Valor |
|---|---|
| Casos CN automatizados | 26 |
| Casos CB automatizados | 17 |
| Total de casos | 43 |
| Pruebas ejecutadas | 86 (43 contra `calc` y 43 contra la referencia) |
| Pruebas aprobadas | 70 |
| Pruebas fallidas | 16 |
| Defectos encontrados | 6 |
| Cobertura de sentencias | 100 % (29 de 29) |
| Cobertura de ramas | 100 % (26 de 26) |
| Líneas sin cubrir | Ninguna |

La cobertura es alta porque los casos CB recorren todos los caminos del código. La cobertura no mide si el resultado es correcto; eso lo hacen las aserciones.

## 4. Defectos encontrados

| ID | Defecto | Requisito | Evidencia | Esperado | Obtenido | Severidad | Prioridad |
|---|---|---|---|---|---|---|---|
| DEF-01 | El tramo 1 usa `p <= L1` e incluye los 3 kg. Debe ser `p < 3`. | R3 | CN-10: 3 kg, urbana, normal, día 3 | $9.000 | $6.000 | Alta | Alta |
| DEF-02 | El recargo de fin de semana solo aplica con `d > 6`. Ignora el sábado (día 6). | R5 | CN-17: 2 kg, urbana, normal, día 6 | $8.000 | $6.000 | Alta | Alta |
| DEF-03 | No valida la zona. Una zona distinta de urbana, rural o nacional no lanza error. | R2 | CN-05 y CB-08: zona "aérea" | Error | $6.000 | Alta | Alta |
| DEF-04 | No valida el día. Un día fuera de 1 a 7 no lanza error. | R2 | CN-06 con día 0 y CN-07 con día 8 | Error | $6.000 | Alta | Alta |
| DEF-05 | El redondeo trunca con `int(t / 100) * 100` en vez de redondear al múltiplo de $100 más cercano con los $50 hacia arriba. | R8 | CN-12: 9.080 → $9.000; CN-21: 6.885 → $6.800; CN-25: 15.998 → $15.900 | $9.100; $6.900; $16.000 | $9.000; $6.800; $15.900 | Alta | Alta |
| DEF-06 | El mensaje de error dice "peso invalido" sin tilde. La especificación pide "peso inválido". | R1 | CN-01, CN-02, CN-03, CB-02 y CB-03 | "peso inválido" | "peso invalido" | Baja | Media |

### Casos que fallan por cada defecto

| Defecto | Casos |
|---|---|
| DEF-01 | CN-10, CN-26 |
| DEF-02 | CN-17, CN-19 |
| DEF-03 | CN-05, CB-08 |
| DEF-04 | CN-06, CN-07 |
| DEF-05 | CN-12, CN-19, CN-21, CN-25 |
| DEF-06 | CN-01, CN-02, CN-03, CB-02, CB-03 |

CN-19 combina DEF-02 y DEF-05; CN-26 combina DEF-01 y DEF-05. Por eso aparecen en dos defectos.

## 5. Detalle de los fallos más importantes

### DEF-01 · Límite del tramo 1

En `envios.py` la condición es `if p <= CONFIG["L1"]`. Con `L1 = 3`, un paquete de 3 kg entra en el tramo 1 y paga $6.000. La especificación dice que el tramo 1 es peso menor que 3, así que 3 kg debe pagar $9.000.

### DEF-02 · Sábado sin recargo

En `envios.py` la condición es `if d > 6`. Solo el domingo (7) recibe los $2.000. La especificación dice que sábado (6) y domingo (7) llevan el recargo. Por eso CN-17 y CN-19 pagan de menos.

### DEF-03 y DEF-04 · Validaciones incompletas

El código solo valida el peso. No revisa que la zona sea urbana, rural o nacional. Tampoco revisa que el día esté entre 1 y 7. En los cuatro casos inválidos el programa devuelve un costo en lugar de lanzar un error.

### DEF-05 · Redondeo

El código usa `int(t / 100) * 100`. Eso siempre baja al múltiplo de $100 anterior. La especificación pide el múltiplo más cercano y que los $50 suban. Por ejemplo, 9.080 debe quedar en $9.100, pero el código devuelve $9.000.

### DEF-06 · Mensaje sin tilde

El error se lanza bien, pero el texto no coincide con R1. No cambia el dinero cobrado, por eso la severidad es baja.

## 6. Observaciones para la refactorización

- El argumento `flag` y el `print` mezclan el cálculo con la salida por consola. Lo voy a tratar como code smell en la Parte 6.
- El código usa `float` para manejar dinero. En la refactorización voy a usar `Decimal` para evitar errores de precisión.
- La función tiene muchas decisiones en un solo bloque. Voy a separar el cálculo en funciones pequeñas y usar el patrón Estrategia para la zona.

## 7. Trazabilidad de requisitos

| Requisito | Estado | Defecto relacionado |
|---|---|---|
| R1 | Con defecto menor | DEF-06 |
| R2 | Con defecto | DEF-03, DEF-04 |
| R3 | Con defecto | DEF-01 |
| R4 | Cumple | Ninguno |
| R5 | Con defecto | DEF-02 |
| R6 | Cumple | Ninguno |
| R7 | Cumple | Ninguno |
| R8 | Con defecto | DEF-05 |

## 8. Para la sustentación

- Puedo mostrar los 16 fallos con `python -m pytest tests -v` y explicar que los valores esperados salen de los documentos, no del código.
- Puedo mostrar que la referencia con `Decimal` y `ROUND_HALF_UP` pasa los 43 casos. Eso demuestra que los resultados esperados están bien calculados.
- Puedo mostrar la cobertura del 100 % y aclarar que una cobertura alta no garantiza resultados correctos, porque el código heredado recorre todas sus ramas y aun así falla 16 pruebas.

## 9. Estado final de los defectos

| Defecto | Rama | Commit | Merge | Estado | Pruebas |
|---|---|---|---|---|---|
| DEF-01 | `fix/DEF-01` | `5e411ec` | `6e1ab84` | Corregido | CN-10, CN-26 |
| DEF-02 | `fix/DEF-02` | `1497b9c` | `5070c5f` | Corregido | CN-17, CN-19 |
| DEF-03 | `fix/DEF-03` | `21ca729` | `3d4f325` | Corregido | CN-05, CB-08 |
| DEF-04 | `fix/DEF-04` | `f999a5f` | `06567e7` | Corregido | CN-06, CN-07 |
| DEF-05 | `fix/DEF-05` | `f528a4a` | `ee6d85d` | Corregido | CN-12, CN-19, CN-21, CN-25, CN-26 |
| DEF-06 | `fix/DEF-06` | `93eb725` | `b4007b3` | Corregido | CN-01, CN-02, CN-03, CB-02, CB-03 |

La suite final tiene 49 casos (43 CN/CB + 6 CE) y 98 pruebas. Los seis defectos se corrigieron en `v2.0.0`. La regresión de `v2.0.0` fue 86/86; en `v2.1.0` es 98/98. No queda ningún defecto crítico o alto abierto.
