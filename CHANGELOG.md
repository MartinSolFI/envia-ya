# Changelog

Todos los cambios importantes de este proyecto se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
El versionado sigue [SemVer](https://semver.org/lang/es/).

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
