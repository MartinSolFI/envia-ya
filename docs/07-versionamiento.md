# Parte 7 · Versionamiento

Estudiante: Martín Alejandro Solano Finol · Código: 0182410126

## 1. Ramas creadas e integradas

| Rama | Qué contiene | Integración |
|---|---|---|
| `test/suite` | Suite de 43 casos y `docs/05-defectos.md` | `merge --no-ff` a `main` |
| `fix/DEF-01` | Corrección del límite del tramo 1 | `merge --no-ff` a `main` |
| `fix/DEF-02` | Corrección del recargo del sábado | `merge --no-ff` a `main` |
| `fix/DEF-03` | Validación de zona | `merge --no-ff` a `main` |
| `fix/DEF-04` | Validación de día | `merge --no-ff` a `main` |
| `fix/DEF-05` | Redondeo con `ROUND_HALF_UP` | `merge --no-ff` a `main` |
| `fix/DEF-06` | Mensaje "peso inválido" | `merge --no-ff` a `main` |
| `refactor/estrategia` | Funciones, constantes y patrón Estrategia | `merge --no-ff` a `main` |

## 2. Estrategia de integración

Usé `git merge --no-ff` para que cada rama deje un commit de unión visible. Así el historial muestra qué rama aportó cada corrección y no se pierde la trazabilidad.

Comandos principales:

```powershell
git switch main
git merge --no-ff test/suite -m "test: integrar suite de pruebas a main"
git merge --no-ff fix/DEF-01 -m "merge: integrar fix/DEF-01"
git merge --no-ff fix/DEF-02 -m "merge: integrar fix/DEF-02"
git merge --no-ff fix/DEF-03 -m "merge: integrar fix/DEF-03"
git merge --no-ff fix/DEF-04 -m "merge: integrar fix/DEF-04"
git merge --no-ff fix/DEF-05 -m "merge: integrar fix/DEF-05"
git merge --no-ff fix/DEF-06 -m "merge: integrar fix/DEF-06"
git merge --no-ff refactor/estrategia -m "refactor: integrar estrategia y funciones a main"
```

En la integración de `refactor/estrategia` hubo un conflicto en `envios.py`. Resolví tomando la versión refactorizada, porque esa rama contiene el código final. Después ejecuté las pruebas y las 86 pasaron.

## 3. Justificación de v2.0.0 con SemVer

SemVer usa tres números: MAYOR.MENOR.PARCHE.

- **MAYOR = 2**: eliminé el argumento `flag`. Eso rompe la compatibilidad para quien llamara `calc(..., flag=True)`. Además, los resultados cambiaron porque corregí defectos de cálculo.
- **MENOR = 0**: no agregué funcionalidad nueva. Solo refactoricé y corregí lo existente.
- **PARCHE = 0**: no es un parche sobre la versión anterior. Es una versión mayor porque el contrato público cambió.

Por eso la versión es `v2.0.0` y no `v1.1.0` ni `v1.0.1`.

## 4. Grafo de commits

Salida de `git log --oneline --graph --all`:

```text
* 4bae9a6 docs: agregar CHANGELOG de la version 2.0.0
*   097668a refactor: integrar estrategia y funciones a main
|\
| * f261222 docs: documentar refactorizacion y metricas de la Parte 6
| * 006de88 refactor: separar calculo en funciones y estrategia de zona y cliente
* |   b4007b3 merge: integrar fix/DEF-06
|\ \
| * | 93eb725 fix: corregir mensaje de peso invalido (DEF-06)
|/ /
* |   ee6d85d merge: integrar fix/DEF-05
|\ \
| * | f528a4a fix: redondear con ROUND_HALF_UP (DEF-05)
|/ /
* |   06567e7 merge: integrar fix/DEF-04
|\ \
| * | f999a5f fix: validar dia (DEF-04)
|/ /
* |   3d4f325 merge: integrar fix/DEF-03
|\ \
| * | 21ca729 fix: validar zona (DEF-03)
|/ /
* |   5070c5f merge: integrar fix/DEF-02
|\ \
| * | 1497b9c fix: aplicar recargo de fin de semana el sabado (DEF-02)
|/ /
* |   6e1ab84 merge: integrar fix/DEF-01
|\ \
| * | 5e411ec fix: corregir limite del tramo 1 (DEF-01)
|/ /
* | 1f2aae0 test: integrar suite de pruebas a main
|\|
| * 473c6e0 docs: registrar defectos y metricas de la Parte 5
| * e7ec8de test: agregar suite CN y CB contra el codigo heredado
|/
* dffe6da docs: caminos independientes y cobertura (Parte 4, 2/2)
* 3385437 docs: grafo de flujo y complejidad ciclomática (Parte 4, 1/2)
* 810c1bc docs: matriz de 26 casos de caja negra con cálculos (Parte 3, 2/2)
* 883d314 docs: particiones, valores límite y tabla de decisión (Parte 3, 1/2)
* 07297aa docs: plan de pruebas (Parte 2)
* eac21bb docs: requisitos, historias de usuario y trazabilidad (Parte 1)
* 4e6d90d fix: agregar código heredado en envios.py (el commit anterior lo dejó vacío)
* c20ff41 chore: código heredado con CONFIG del estudiante
```

La salida se capturó antes de crear este documento. El tag `v2.0.0` queda en el commit que contiene este archivo.

## 5. Estado final

- `main` tiene el código refactorizado, la suite y los documentos.
- `v1.0.0` conserva el código heredado.
- `v2.0.0` marca la refactorización y las correcciones.
- Las 86 pruebas pasan y la cobertura es 100 % de sentencias y ramas.

## 6. Versión 2.1.0 (Parte 8)

La Parte 8 agregó el cliente empresarial y publicó `v2.1.0` sobre el commit `db3eadd`.

SemVer:

- **MAYOR = 2**: se mantiene la versión mayor de la refactorización.
- **MENOR = 1**: funcionalidad nueva y retrocompatible.
- **PARCHE = 0**: no es una corrección.

El grafo de la sección 4 es el de la Parte 7 y no incluye la rama `feature/cliente-empresarial` ni el tag `v2.1.0`. El detalle está en `08-cliente-empresarial.md`.

## 7. Versión 2.1.1 (corrección de documentación)

La versión `v2.1.1` es un parche de documentación sobre `v2.1.0`. No cambia el código ni las pruebas: corrige las métricas de la Parte 5, completa el análisis de la Parte 6 y alinea la trazabilidad de la Parte 8.

- **MAYOR = 2**: se mantiene.
- **MENOR = 1**: se mantiene.
- **PARCHE = 1**: corrige documentación sin cambiar la funcionalidad.

El tag `v2.1.1` apunta al commit final de `main` con las correcciones. `v2.1.0` se conserva en `db3eadd` para la entrega de la Parte 8.
