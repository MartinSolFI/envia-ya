# Changelog

Todos los cambios importantes de este proyecto se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
El versionado sigue [SemVer](https://semver.org/lang/es/).

## [2.1.1] - 2026-11-11

### Added

- Secciones de sustentación y capturas para el PDF en las Partes 5, 6 y 8.

### Changed

- Corregí las métricas, los code smells, la clasificación de cambios, el diagrama UML y la trazabilidad de las Partes 5, 6 y 8.

## [2.1.0] - 2026-11-11

### Added

- Cliente empresarial con 12 % de descuento.
- Regla: el cliente empresarial no paga recargo de zona si el peso supera 10 kg.
- Garantía: el descuento del cliente se aplica antes del cupón.
- Casos CE-01 a CE-06 en la suite.
- Documento `docs/08-cliente-empresarial.md`.

### Changed

- `calc` delega en la estrategia del cliente la decisión de aplicar el recargo de zona.

## [2.0.0] - 2026-11-11

### Added

- Suite de 43 casos CN/CB en `tests/test_envios.py`.
- Implementación de referencia con `Decimal` y `ROUND_HALF_UP`.
- Documentos `docs/05-defectos.md` y `docs/06-refactorizacion.md`.

### Changed

- Refactoricé `calc` en funciones pequeñas y constantes con nombre.
- Apliqué el patrón Estrategia para zona y cliente.
- Cambié el manejo de dinero de `float` a `Decimal`.
- El redondeo ahora usa `ROUND_HALF_UP`.

### Fixed

- DEF-01: límite del tramo 1 para el peso de 3 kg.
- DEF-02: recargo de fin de semana para el sábado.
- DEF-03: validación de la zona.
- DEF-04: validación del día.
- DEF-05: redondeo al múltiplo de $100 más cercano.
- DEF-06: mensaje "peso inválido" con tilde.

### Removed

- Argumento `flag` y `print` dentro de `calc`.
- Diccionario global mutable `CONFIG`.

## [1.0.0] - 2026-11-11

### Added

- Código heredado de `calc` con los parámetros del estudiante.
