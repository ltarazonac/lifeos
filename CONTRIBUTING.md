# Contributing Guide - LifeOS

## 1. Convención de nombres

- Código en inglés.
- Variables, funciones y clases en **camelCase** o **PascalCase**.
- Archivos en **kebab-case** o **snake_case** según el lenguaje.
- No usar español en el código.

---

## 2. Commits (Conventional Commits)

Usamos el estándar:

- feat: nueva funcionalidad
- fix: corrección de errores
- docs: cambios en documentación
- style: formato (sin cambiar lógica)
- refactor: refactorización de código
- test: pruebas
- chore: tareas internas

Ejemplo:

feat: add user authentication module

---

## 3. Ramas (Git Flow simplificado)

- main → producción
- develop → desarrollo
- feature/* → nuevas funcionalidades
- fix/* → correcciones

Ejemplo:

feature/login-system

---

## 4. Estilo de código

- Python: PEP 8
- Frontend: ESLint + Prettier
- Código limpio y legible
- Funciones pequeñas y reutilizables

---

## 5. Flujo de trabajo

1. Crear rama desde develop
2. Desarrollar funcionalidad
3. Hacer commits pequeños
4. Abrir Pull Request (más adelante)
5. Revisar antes de merge

---

## 6. Regla principal

El código no solo debe funcionar, debe ser mantenible.