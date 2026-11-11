# Parte 4 · Caminos independientes y cobertura

Estudiante: Martín Alejandro Solano Finol · Código: 0182410126

Los resultados esperados salen de mi especificación, no del código. Formato de entradas: peso, zona, cliente, día, cupón.

## 4. Caminos independientes (15) y su caso de prueba

| Camino | Nodos recorridos | Caso | Entradas | Resultado esperado |
|---|---|---|---|---|
| P1 (base) | 1-2-4-5-9-10-15-17-19-21-24-26-28-29 | CB-01 | 2, urbana, normal, 1, - | $6.000 |
| P2 | 1-3-29 | CB-02 | 0, urbana, normal, 1, - | Error "peso inválido" |
| P3 | 1-2-3-29 | CB-03 | 51, urbana, normal, 1, - | Error "peso inválido" |
| P4 | 1-2-4-6-7-9-10-15-17-19-21-24-26-28-29 | CB-04 | 6, urbana, normal, 1, - | $9.000 |
| P5 | 1-2-4-6-8-9-10-15-17-19-21-24-26-28-29 | CB-05 | 12, urbana, normal, 1, - | $10.600 |
| P6 | 1-2-4-5-9-11-12-15-17-19-21-24-26-28-29 | CB-06 | 2, rural, normal, 1, - | $7.200 |
| P7 | 1-2-4-5-9-11-13-14-15-17-19-21-24-26-28-29 | CB-07 | 2, nacional, normal, 1, - | $8.400 |
| P8 | 1-2-4-5-9-11-13-15-17-19-21-24-26-28-29 | CB-08 | 2, aérea, normal, 1, - | Error (zona inválida) |
| P9 | 1-2-4-5-9-10-15-16-17-19-21-24-26-28-29 | CB-09 | 2, urbana, normal, 7, - | $8.000 |
| P10 | 1-2-4-5-9-10-15-17-18-19-21-24-26-28-29 | CB-10 | 2, urbana, frecuente, 1, - | $5.700 |
| P11 | 1-2-4-5-9-10-15-17-19-20-21-24-26-28-29 | CB-11 | 2, urbana, vip, 1, - | $5.100 |
| P12 | 1-2-4-5-9-10-15-17-19-21-22-24-26-28-29 | CB-12 | 2, urbana, normal, 1, XYZ | $6.000 |
| P13 | 1-2-4-5-9-10-15-17-19-21-22-23-24-26-28-29 | CB-13 | 2, urbana, normal, 1, ENVIO10 | $5.400 |
| P14 | 1-2-4-5-9-10-15-17-19-20-21-22-23-24-25-26-28-29 | CB-14 | 1, urbana, vip, 1, ENVIO10 | $5.000 |
| P15 | 1-2-4-5-9-10-15-17-19-21-24-26-27-28-29 | CB-15 | 2, urbana, normal, 1, -, flag=True | $6.000 |

Notas:
- P1 es el camino base. Cada camino siguiente cambia una decisión respecto a P1, así cada uno tiene una arista propia.
- P14 combina VIP y cupón porque el mínimo de $5.000 solo se activa con descuentos: con la tarifa mínima de $6.000 y sin descuento nunca baja de $5.000.
- CB-14: 6.000 × 0,85 × 0,90 = 4.590, menor que 5.000, queda en $5.000.
- CB-08: la especificación (R2) pide error. El código heredado no lo lanza.

## 5. Cobertura

Casos extra para la cobertura:

| Caso | Entradas | Resultado esperado |
|---|---|---|
| CB-16 | 6, rural, frecuente, 7, ENVIO10, flag=True | $10.900 |
| CB-17 | 12, nacional, vip, 1, - | $12.600 |

Cálculo CB-16: 9.000 → rural 10.800 → domingo 12.800 → frecuente 12.160 → cupón 10.944 → **$10.900**.
Cálculo CB-17: 10.600 → nacional 14.840 → vip 12.614 → **$12.600**.

### Cobertura de sentencias (100 %)
Casos: **CB-02, CB-14, CB-16, CB-17** (4 casos).
- CB-02: `raise`
- CB-14: `t = 6000`, `t = t`, vip, `t = 5000`
- CB-16: `t = 9000`, rural, fin de semana, frecuente, cupón, `print`, `return`
- CB-17: `t = 9000 + ...`, nacional, vip

### Cobertura de ramas (100 %)
Casos: **CB-02, CB-03, CB-08, CB-12, CB-14, CB-16, CB-17** (7 casos).

| Nodo | Verdadero | Falso |
|---|---|---|
| 1 | CB-02 | CB-14 |
| 2 | CB-03 | CB-14 |
| 4 | CB-14 | CB-16 |
| 6 | CB-16 | CB-17 |
| 9 | CB-14 | CB-16 |
| 11 | CB-16 | CB-17 |
| 13 | CB-17 | CB-08 |
| 15 | CB-16 | CB-14 |
| 17 | CB-16 | CB-14 |
| 19 | CB-14 | CB-16 |
| 21 | CB-16 | CB-17 |
| 22 | CB-16 | CB-12 |
| 24 | CB-14 | CB-16 |
| 26 | CB-16 | CB-14 |

Los 15 casos CB-01 a CB-15 juntos también dan 100 % de ramas, porque un conjunto de caminos independientes recorre todas las aristas.

## 6. Nota de actualización

Estos casos se diseñaron contra `v1.0.0`. En `v2.0.0` se eliminó el argumento `flag`; en la suite final, CB-15 y CB-16 ya no lo pasan. La cobertura final de `v2.1.0` es 100 % de 97 sentencias y 16 ramas. El detalle está en `06-refactorizacion.md` y `08-cliente-empresarial.md`.