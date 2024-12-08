class CuentaBancaria:
    def __init__(self, nombre, numero_cuenta, saldo):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def descripcion(self):
        print(f"Cuenta bancaria de {self.nombre}")

    def get_saldo(self):
        return self.saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
        else:
            print("No hay suficiente saldo")

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre, numero_cuenta, saldo, tasa_interes):
        super().__init__(nombre, numero_cuenta, saldo)
        self.tasa_interes = tasa_interes

    def calcular_interes(self):
        return self.get_saldo() * self.tasa_interes / 100

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre, numero_cuenta, saldo, limite_credito):
        super().__init__(nombre, numero_cuenta, saldo)
        self.limite_credito = limite_credito

    def calcular_credito(self):
        return self.limite_credito - self.get_saldo()

class CuentaHipotecaria(CuentaBancaria):
    def __init__(self, nombre, numero_cuenta, saldo, plazo):
        super().__init__(nombre, numero_cuenta, saldo)
        self.plazo = plazo

    def calcular_cuota(self):
        return self.get_saldo() / self.plazo

class CuentaPension(CuentaBancaria):
    def __init__(self, nombre, numero_cuenta, saldo, edad):
        super().__init__(nombre, numero_cuenta, saldo)
        self.edad = edad

    def calcular_pension(self):
        if self.edad >= 65:
            return self.get_saldo() * 0.1
        else:
            return 0

# Instanciar objetos
cuentas = [
    CuentaAhorro("Banco Nacional", "1234567890", 1000, 5),
    CuentaCorriente("Banco Internacional", "9876543210", 500, 2000),
    CuentaHipotecaria("Banco de la Vivienda", "1111111111", 200000, 20),
    CuentaPension("Banco de la Pension", "2222222222", 50000, 65)
]

# Llamar métodos
for cuenta in cuentas:
    cuenta.descripcion()
    print(f"Número de cuenta: {cuenta.numero_cuenta}")
    print(f"Saldo: ${cuenta.get_saldo():,.2f}")
    if isinstance(cuenta, CuentaAhorro):
        print(f"Interés: ${cuenta.calcular_interes():,.2f}")
    elif isinstance(cuenta, CuentaCorriente):
        print(f"Crédito disponible: ${cuenta.calcular_credito():,.2f}")
    elif isinstance(cuenta, CuentaHipotecaria):
        print(f"Cuota mensual: ${cuenta.calcular_cuota():,.2f}")
    elif isinstance(cuenta, CuentaPension):
        print(f"Pensión: ${cuenta.calcular_pension():,.2f}")
    print()