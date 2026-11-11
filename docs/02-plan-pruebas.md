# Parte 2 · Plan de pruebas

Estudiante: Martín Alejandro Solano Finol · Código: 0182410126

> Nota: este plan se escribió para la versión 1.0.0. La Parte 8 lo amplía con R9-R11 y los casos CE-01 a CE-06; la regresión final es de 98 pruebas.

## 1. Alcance
Voy a probar la función `calc` de `envios.py` (versión 1.0.0). Esto incluye:
- validar peso, zona y día (R1, R2)
- tarifa base según el peso (R3)
- recargo por zona (R4) y por fin de semana (R5)
- descuentos de cliente y cupón (R6, R7)
- mínimo de $5.000 y redondeo (R8)

No voy a probar la interfaz, la base de datos, los pagos, la velocidad ni la seguridad. El parcial solo trata de `calc`.

## 2. Niveles de prueba
| Nivel | Cómo lo aplico en este caso |
|---|---|
| Unidad | Pruebo `calc` sola, con pytest. Es el único nivel que automatizo en este trabajo. |
| Integración | Reviso que `calc` reciba bien los datos del módulo que registra el envío; en `v1.0.0` también revisaba que leyera `CONFIG` sin problema. Lo describo, no lo automatizo. |
| Sistema | Registro un envío completo (peso, zona, cliente, día, cupón) y compruebo que el costo cobrado sea el de la especificación. |
| Aceptación | EnvíaYa revisa unos casos con resultado calculado a mano y confirma que se cumplen R1 a R8; la Parte 8 agrega R9 a R11. |

## 3. Estrategia
- **Caja negra:** diseño casos solo con la especificación, usando particiones de equivalencia, valores límite y tabla de decisión.
- **Caja blanca:** miro el código, dibujo el grafo, calculo la complejidad ciclomática y busco caminos independientes.
- **Resultados esperados:** los calculo yo a mano con la especificación. No los copio de lo que devuelve el código, porque así nunca encontraría los defectos.
- **Regresión:** cada vez que corrijo algo, vuelvo a correr todos los casos.

## 4. Ambiente y herramientas
Windows 11, Python 3, pytest, pytest-cov, radon, Git, GitHub y Visual Studio Code.

## 5. Roles
| Rol | Quién |
|---|---|
| Diseño de pruebas | Martín Solano |
| Ejecución de pruebas | Martín Solano |
| Correcciones | Martín Solano |
| Aprobación | Docente Robert Damián Quintero Laverde |

## 6. Riesgos y mitigación
| Riesgo | Probabilidad | Impacto | Qué hago |
|---|---|---|---|
| Calcular mal un resultado esperado a mano | Media | Alto | Revisar cada cálculo dos veces |
| Confundir las reglas de paridad (D, E, B, F) | Media | Alto | Tenerlas escritas con mis valores en el documento de requisitos |
| Errores de decimales en el redondeo | Alta | Medio | Incluir casos cerca de múltiplos de $50 |
| Cobertura baja | Media | Medio | Medir con pytest-cov y agregar casos donde falten |
| Que al corregir un defecto se dañe otra cosa | Media | Alto | Correr toda la regresión después de cada corrección |

## 7. Criterios de entrada
Empiezo a probar cuando tenga:
- la especificación R1 a R8 con mis valores
- `CONFIG` lleno con mis parámetros (solo en `v1.0.0`)
- el código heredado con la etiqueta `v1.0.0`
- Python, pytest y pytest-cov instalados

## 8. Criterios de salida
Termino cuando:
- se hayan ejecutado todos los casos
- la cobertura de sentencias sea de al menos 95 % y la de ramas de al menos 90 %
- todos los defectos estén registrados con severidad y prioridad
- después de corregir, todos los casos pasen
- no quede ningún defecto crítico o alto abierto