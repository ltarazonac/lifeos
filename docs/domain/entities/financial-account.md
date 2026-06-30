# FinancialAccount

## Propósito

Representa cualquier lugar donde pueda existir dinero, una inversión o una obligación financiera dentro de LifeOS.

Una FinancialAccount no necesariamente corresponde a una cuenta bancaria.

También puede representar un objetivo financiero, una cartera de inversión, una tarjeta de crédito o un préstamo.

---

# Ejemplos

## Bancos

- BCP Soles
- BCP Dólares
- Caja Piura
- Pichincha

## Ahorro

- Fondo de Emergencia
- Departamento
- Carro
- Viajes

## Inversiones

- Cuenta Ahorro IBKR
- Interactive Brokers

## Pasivos

- Tarjeta Visa
- Tarjeta Mastercard
- Préstamo Vehicular
- Préstamo Hipotecario

---

# Responsabilidades

Una FinancialAccount debe permitir:

- conocer el saldo actual
- conocer la moneda
- conocer su propietario
- registrar movimientos
- registrar transferencias
- formar parte del patrimonio

---

# Reglas de negocio

1. Toda transacción afecta al menos una FinancialAccount.

2. Una transferencia afecta exactamente dos FinancialAccount.

3. Una cuenta puede pertenecer a un objetivo financiero.

4. Una cuenta puede formar parte del patrimonio.

5. Una cuenta puede estar activa o inactiva.

---

# Casos de uso

- Registrar sueldo en BCP.
- Transferir dinero al Fondo de Emergencia.
- Comprar dólares.
- Enviar dinero a IBKR.
- Registrar una compra con tarjeta.
- Registrar un préstamo.