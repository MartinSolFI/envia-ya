# Parte 3 · Diseño de casos de caja negra

Estudiante: Martín Alejandro Solano Finol · Código: 0182410126

Para todos los cálculos: tramo 1 es peso < 3, el recargo de fin de semana va antes de los descuentos, y si hay cliente y cupón se aplican ambos (primero cliente, luego cupón).

## 1. Particiones de equivalencia

| Entrada | Clase | Tipo | Representante |
|---|---|---|---|
| Peso | p ≤ 0 | Inválida | -1 |
| Peso | 0 < p < 3 (tramo 1) | Válida | 2 |
| Peso | 3 ≤ p ≤ 10 (tramo 2) | Válida | 6 |
| Peso | 10 < p ≤ 50 (tramo 3) | Válida | 20 |
| Peso | p > 50 | Inválida | 60 |
| Zona | urbana | Válida | "urbana" |
| Zona | rural | Válida | "rural" |
| Zona | nacional | Válida | "nacional" |
| Zona | cualquier otro valor | Inválida | "aérea" |
| Cliente | normal | Válida | "normal" |
| Cliente | frecuente | Válida | "frecuente" |
| Cliente | vip | Válida | "vip" |
| Cliente | empresarial | Válida | "empresarial" |
| Día | 1 a 5 (entre semana) | Válida | 3 |
| Día | 6 (sábado) | Válida | 6 |
| Día | 7 (domingo) | Válida | 7 |
| Día | menor que 1 | Inválida | 0 |
| Día | mayor que 7 | Inválida | 8 |
| Cupón | sin cupón | Válida | None |
| Cupón | ENVIO10 | Válida | "ENVIO10" |
| Cupón | no existe | Válida (se ignora, F par) | "XYZ" |

La especificación define normal, frecuente, vip y empresarial. Para un cliente distinto de esos cuatro no hay regla explícita, así que no diseño casos para eso.

## 2. Valores límite del peso (urbana, cliente normal, día 1, sin cupón)

| Límite | Peso | Resultado esperado | Cálculo |
|---|---|---|---|
| 0 | 0 | Error "peso inválido" | no cumple 0 < peso |
| 0 | 0,1 | $6.000 | tramo 1 |
| L1 = 3 | 2,9 | $6.000 | tramo 1 (2,9 < 3) |
| L1 = 3 | 3 | $9.000 | 3 no es menor que 3, va a tramo 2 |
| L1 = 3 | 3,1 | $9.000 | tramo 2 |
| L2 = 10 | 10 | $9.000 | tramo 2 incluye el 10 |
| L2 = 10 | 10,1 | $9.100 | 9.000 + 0,1 × 800 = 9.080, redondea a 9.100 |
| PMAX = 50 | 49,9 | $40.900 | 9.000 + 39,9 × 800 = 40.920, redondea a 40.900 |
| PMAX = 50 | 50 | $41.000 | 9.000 + 40 × 800 |
| PMAX = 50 | 50,1 | Error "peso inválido" | 50,1 > 50 |

## 3. Tabla de decisión: cliente × cupón × fin de semana

Base: 2 kg, urbana → $6.000. Con fin de semana: 6.000 + 2.000 = $8.000 (antes de descuentos, por E par). Con cliente y cupón se aplican ambos, cliente primero (por B impar).

| Regla | Cliente | Cupón ENVIO10 | Fin de semana | Cálculo | Resultado |
|---|---|---|---|---|---|
| T1 | normal | No | No | 6.000 | $6.000 |
| T2 | normal | No | Sí | 8.000 | $8.000 |
| T3 | normal | Sí | No | 6.000 × 0,90 = 5.400 | $5.400 |
| T4 | normal | Sí | Sí | 8.000 × 0,90 = 7.200 | $7.200 |
| T5 | frecuente | No | No | 6.000 × 0,95 = 5.700 | $5.700 |
| T6 | frecuente | No | Sí | 8.000 × 0,95 = 7.600 | $7.600 |
| T7 | frecuente | Sí | No | 6.000 × 0,95 × 0,90 = 5.130 | $5.100 |
| T8 | frecuente | Sí | Sí | 8.000 × 0,95 × 0,90 = 6.840 | $6.800 |
| T9 | vip | No | No | 6.000 × 0,85 = 5.100 | $5.100 |
| T10 | vip | No | Sí | 8.000 × 0,85 = 6.800 | $6.800 |
| T11 | vip | Sí | No | 6.000 × 0,85 × 0,90 = 4.590, mínimo | $5.000 |
| T12 | vip | Sí | Sí | 8.000 × 0,85 × 0,90 = 6.120 | $6.100 |

## 4. Cliente empresarial (Parte 8)

Reglas nuevas:

- El cliente empresarial recibe un 12 % de descuento.
- Si el peso supera 10 kg, no se aplica recargo de zona.
- Con 10 kg o menos, el recargo de zona sí se aplica.
- El descuento del cliente se aplica antes del cupón.

Valores límite del peso para el cliente empresarial (nacional, día 1, sin cupón):

| Peso | Recargo de zona | Cálculo | Resultado |
|---|---|---|---|
| 10 | Sí | 9.000 × 1,40 × 0,88 = 11.088 | $11.100 |
| 12 | No | 10.600 × 0,88 = 9.328 | $9.300 |

Los casos CE-01 a CE-06 y sus cálculos completos están en `03b-matriz-casos.md` y `08-cliente-empresarial.md`.