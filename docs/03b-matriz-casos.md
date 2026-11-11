# Parte 3 · Matriz de casos de prueba (caja negra)

Estudiante: Martín Alejandro Solano Finol · Código: 0182410126

Formato de entradas: peso, zona, cliente, día, cupón. Los resultados esperados están calculados a mano con mi especificación (tramo 1: peso < 3; fin de semana antes de descuentos; cliente y cupón se aplican ambos; cupón inexistente se ignora).

| ID | Req. | Entradas | Resultado esperado | Técnica |
|---|---|---|---|---|
| CN-01 | R1 | 0, urbana, normal, 1, - | Error "peso inválido" | Valor límite |
| CN-02 | R1 | -1, urbana, normal, 1, - | Error "peso inválido" | Partición inválida |
| CN-03 | R1 | 50,1, urbana, normal, 1, - | Error "peso inválido" | Valor límite |
| CN-04 | R1, R3 | 50, urbana, normal, 1, - | $41.000 | Valor límite |
| CN-05 | R2 | 2, aérea, normal, 1, - | Error | Partición inválida |
| CN-06 | R2 | 2, urbana, normal, 0, - | Error | Valor límite |
| CN-07 | R2 | 2, urbana, normal, 8, - | Error | Valor límite |
| CN-08 | R3 | 0,1, urbana, normal, 1, - | $6.000 | Valor límite |
| CN-09 | R3 | 2,9, urbana, normal, 1, - | $6.000 | Valor límite |
| CN-10 | R3 | 3, urbana, normal, 3, - | $9.000 | Valor límite |
| CN-11 | R3 | 10, urbana, normal, 2, - | $9.000 | Valor límite |
| CN-12 | R3 | 10,1, urbana, normal, 2, - | $9.100 | Valor límite |
| CN-13 | R3 | 20, urbana, normal, 2, - | $17.000 | Partición válida |
| CN-14 | R4 | 6, rural, normal, 3, - | $10.800 | Partición válida |
| CN-15 | R4 | 6, nacional, normal, 3, - | $12.600 | Partición válida |
| CN-16 | R3, R4 | 12, nacional, normal, 2, - | $14.800 | Partición válida |
| CN-17 | R5 | 2, urbana, normal, 6, - | $8.000 | Tabla de decisión |
| CN-18 | R4, R5 | 2, rural, normal, 7, - | $9.200 | Tabla de decisión |
| CN-19 | R5, R6 | 2, rural, vip, 6, ENVIO10 | $7.000 | Tabla de decisión |
| CN-20 | R6 | 2, urbana, frecuente, 1, - | $5.700 | Tabla de decisión |
| CN-21 | R6 | 10, urbana, vip, 1, ENVIO10 | $6.900 | Tabla de decisión |
| CN-22 | R6 | 2, urbana, normal, 1, ENVIO10 | $5.400 | Tabla de decisión |
| CN-23 | R7 | 2, urbana, normal, 1, XYZ | $6.000 | Partición válida |
| CN-24 | R8 | 0,1, urbana, vip, 1, ENVIO10 | $5.000 | Valor límite (mínimo) |
| CN-25 | R8 | 12, nacional, frecuente, 7, - | $16.000 | Valor límite (redondeo) |
| CN-26 | R8 | 3, urbana, frecuente, 1, - | $8.600 | Valor límite ($50 sube) |

## Cálculos paso a paso

### CN-10: 3 kg, urbana, normal, día 3, sin cupón
1. Tramo: D = 1 es impar, el tramo 1 es peso < 3. Como 3 no es menor que 3, va al tramo 2 → $9.000
2. Zona urbana: sin recargo → $9.000
3. Día 3, no es fin de semana → $9.000
4. Cliente normal y sin cupón: sin descuento → $9.000
5. Es mayor que $5.000. Se redondea a $100 → **$9.000**

### CN-16: 12 kg, nacional, normal, día 2, sin cupón
1. Más de 10 kg: 9.000 + 2 × 800 = $10.600
2. Nacional +40 %: 10.600 × 1,40 = $14.840
3. Día 2, no es fin de semana → $14.840
4. Sin descuentos → $14.840
5. Se redondea a $100 → **$14.800**

### CN-19: 2 kg, rural, vip, día 6, ENVIO10
1. Tramo 1 (2 < 3) → $6.000
2. Rural +20 %: 6.000 × 1,20 = $7.200
3. Sábado, E = 2 es par: el recargo va antes de los descuentos → 7.200 + 2.000 = $9.200
4. B = 1 es impar: se aplican ambos, primero el cliente. VIP 15 %: 9.200 × 0,85 = $7.820
5. Cupón ENVIO10 10 %: 7.820 × 0,90 = $7.038
6. Se redondea a $100 → **$7.000**

### CN-25: 12 kg, nacional, frecuente, día 7, sin cupón
1. Más de 10 kg: 9.000 + 2 × 800 = $10.600
2. Nacional +40 %: $14.840
3. Domingo, antes de descuentos: 14.840 + 2.000 = $16.840
4. Frecuente 5 %: 16.840 × 0,95 = $15.998
5. Se redondea al múltiplo de $100 más cercano → **$16.000** (15.998 está más cerca de 16.000 que de 15.900)

### CN-26: 3 kg, urbana, frecuente, día 1, sin cupón
1. 3 no es menor que 3, va al tramo 2 → $9.000
2. Urbana, sin recargo → $9.000
3. Día 1, no es fin de semana → $9.000
4. Frecuente 5 %: 9.000 × 0,95 = $8.550
5. Redondeo: $8.550 está justo en la mitad y los $50 suben → **$8.600**