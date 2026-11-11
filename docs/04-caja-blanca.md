# Parte 4 · Caja blanca

Estudiante: Martín Alejandro Solano Finol · Código: 0182410126

## 1. Objetivo y alcance

Analicé el código heredado `v1.0.0` de `envios.py` para construir el grafo de flujo, calcular la complejidad ciclomática y identificar los caminos independientes. El detalle de los caminos y la cobertura está en `04b-caminos-cobertura.md`.

## 2. Grafo de flujo

El grafo tiene 29 nodos y 42 aristas. La numeración coincide con los caminos de `04b-caminos-cobertura.md`.

| Nodo | Condición o acción | Rama verdadera | Rama falsa |
|---|---|---|---|
| 1 | `p <= 0` | 3 (error) | 2 |
| 2 | `p > 50` | 3 (error) | 4 |
| 3 | `raise ValueError("peso invalido")` | 29 (salida) | — |
| 4 | `p <= L1` | 5 (`t = 6000`) | 6 |
| 5 | `t = 6000` | 9 | — |
| 6 | `p <= L2` | 7 (`t = 9000`) | 8 |
| 7 | `t = 9000` | 9 | — |
| 8 | `t = 9000 + ...` | 9 | — |
| 9 | `z == "urbana"` | 10 | 11 |
| 10 | `t = t` | 15 | — |
| 11 | `z == "rural"` | 12 | 13 |
| 12 | `t = t + t * 0.20` | 15 | — |
| 13 | `z == "nacional"` | 14 | 15 |
| 14 | `t = t + t * 0.40` | 15 | — |
| 15 | `d > 6` | 16 | 17 |
| 16 | `t = t + 2000` | 17 | — |
| 17 | `c == "frecuente"` | 18 | 19 |
| 18 | `t = t - t * 0.05` | 19 | — |
| 19 | `c == "vip"` | 20 | 21 |
| 20 | `t = t - t * 0.15` | 21 | — |
| 21 | `cup != None` | 22 | 24 |
| 22 | `cup == "ENVIO10"` | 23 | 24 |
| 23 | `t = t - t * 0.10` | 24 | — |
| 24 | `t < 5000` | 25 | 26 |
| 25 | `t = 5000` | 26 | — |
| 26 | `flag` | 27 | 28 |
| 27 | `print("costo:", t)` | 28 | — |
| 28 | `return int(t / 100) * 100` | 29 | — |
| 29 | Salida | — | — |

## 3. Complejidad ciclomática

Aplico la fórmula de McCabe:

```text
V(G) = E - N + 2P
V(G) = 42 - 29 + 2(1)
V(G) = 15
```

El resultado coincide con los 15 caminos independientes de `04b-caminos-cobertura.md` y con la complejidad 15 que reporta `radon` para `calc` en `v1.0.0`.

## 4. Caminos independientes

Los 15 caminos P1 a P15 están en `04b-caminos-cobertura.md`, cada uno con su caso CB y su resultado esperado. P1 es el camino base y cada camino siguiente cambia una decisión.

## 5. Cobertura

Los casos CB-02, CB-14, CB-16 y CB-17 cubren el 100 % de las sentencias. Los casos CB-02, CB-03, CB-08, CB-12, CB-14, CB-16 y CB-17 cubren el 100 % de las ramas. El detalle está en `04b-caminos-cobertura.md`.

## 6. Conclusión

La cobertura del 100 % no garantiza que los resultados sean correctos. El código heredado recorre todas sus sentencias y ramas, pero falla 16 pruebas porque calcula mal el tramo, el sábado, las validaciones y el redondeo. La caja blanca sirve para medir qué se ejecuta; las aserciones y los valores esperados son los que verifican el resultado.
