# Parte 1 · Requisitos y criterios de aceptación

Estudiante: Martín Alejandro Solano Finol · Código: 0182410126

## Mis parámetros
| A | B | C | D | E | F | PMAX | L1 | L2 | RR | RN | V | S | CAMBIO |
|---|---|---|---|---|---|------|----|----|----|----|---|---|--------|
| 4 | 1 | 0 | 1 | 2 | 6 | 50 | 3 | 10 | 20 % | 40 % | 15 % | $2.000 | 1 |

Reglas por paridad: D=1 impar (tramo 1: peso < 3) · E=2 par (fin de semana antes de descuentos) · B=1 impar (se aplican cliente y luego cupón) · F=6 par (cupón inexistente se ignora).

## 1. Especificación (R1–R8 con mis valores)
- **R1** El peso debe cumplir 0 < peso ≤ 50. Si no, error "peso inválido".
- **R2** Si la zona no es urbana, rural o nacional, o el día no está entre 1 y 7, se lanza un error.
- **R3** Tarifa base. Tramo 1 (peso < 3): $6.000. Tramo 2 (3 ≤ peso ≤ 10): $9.000. Más de 10 kg: $9.000 + $800 por cada kg sobre 10, proporcional.
- **R4** Recargo por zona. Rural +20 %. Nacional +40 %. Urbana sin recargo.
- **R5** Sábado (6) y domingo (7): +$2.000, antes de los descuentos.
- **R6** Descuento de cliente: frecuente 5 %, VIP 15 %. Cupón ENVIO10: 10 %. Si hay cliente y cupón se aplican ambos: primero el del cliente y luego el cupón.
- **R7** Un cupón que no existe se ignora.
- **R8** El costo nunca es menor que $5.000. Se redondea al múltiplo de $100 más cercano; los $50 suben.

## 2. Historias de usuario

### HU-01 · Validación de datos (R1, R2)
Como operador de EnvíaYa quiero que el sistema rechace datos inválidos para no cobrar envíos imposibles.
- Dado un peso de 0 kg, cuando calculo el costo, entonces se lanza el error "peso inválido".
- Dado un peso de 50,1 kg, cuando calculo el costo, entonces se lanza el error "peso inválido".
- Dada la zona "aérea", cuando calculo el costo, entonces se lanza un error.
- Dado el día 8, cuando calculo el costo, entonces se lanza un error.

### HU-02 · Tarifa según peso, zona y día (R3, R4, R5)
Como cliente quiero conocer el costo según el peso, la zona y el día para decidir si envío.
- Dado un paquete de 3 kg, urbana, cliente normal, día 3, cuando calculo, entonces el costo es $9.000 (3 ya no es tramo 1).
- Dado un paquete de 2 kg, rural, cliente normal, día 6, cuando calculo, entonces el costo es $9.200 (6.000 × 1,20 + 2.000 de sábado).
- Dado un paquete de 12 kg, nacional, cliente normal, día 2, cuando calculo, entonces el costo es $14.800 (10.600 × 1,40 = 14.840, redondeado).

### HU-03 · Descuentos, mínimo y redondeo (R6, R7, R8)
Como cliente frecuente quiero que se apliquen mis descuentos y cupones para pagar menos.
- Dado 10 kg, urbana, VIP, día 1, cupón ENVIO10, cuando calculo, entonces el costo es $6.900 (9.000 × 0,85 × 0,90 = 6.885).
- Dado 2 kg, urbana, normal, día 1, cupón "XYZ" (no existe), cuando calculo, entonces el cupón se ignora y el costo es $6.000.
- Dado 0,1 kg, urbana, VIP, día 1, cupón ENVIO10, cuando calculo, entonces el costo es $5.000 (el mínimo).

## 3. Matriz de trazabilidad (se completa en las partes 3 a 5)
| Requisito | Historia | Casos de prueba |
|---|---|---|
| R1 | HU-01 | (pendiente) |
| R2 | HU-01 | (pendiente) |
| R3 | HU-02 | (pendiente) |
| R4 | HU-02 | (pendiente) |
| R5 | HU-02 | (pendiente) |
| R6 | HU-03 | (pendiente) |
| R7 | HU-03 | (pendiente) |
| R8 | HU-03 | (pendiente) |