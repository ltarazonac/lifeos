# Domain Model v1

Este documento representa el modelo conceptual del dominio de LifeOS.

No representa la base de datos.

No representa la implementación.

Representa únicamente los conceptos del negocio y sus relaciones.

---

```mermaid
classDiagram

class FinancialPlan

class FinancialGoal

class FinancialAccount

class Transaction

FinancialPlan "1" --> "*" FinancialGoal

FinancialGoal "1" --> "*" FinancialAccount

FinancialAccount "1" --> "*" Transaction
```