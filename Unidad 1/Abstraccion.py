class Banco:
    def __init__(self, nombre):
        self.nombre = nombre

    def descripcion(self):
        print(f"Banco: {self.nombre}")

    def get_nombre(self):
        return self.nombre


class CuentaBancaria(Banco):
    def __init__(self, nombre, numero_cuenta, saldo):
        super().__init__(nombre)
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
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
cuenta_ahorro = CuentaAhorro("Banco Nacional", "1234567890", 1000, 5)
cuenta_corriente = CuentaCorriente("Banco Internacional", "9876543210", 500, 2000)
cuenta_hipotecaria = CuentaHipotecaria("Banco de la Vivienda", "1111111111", 200000, 20)
cuenta_pension = CuentaPension("Banco de la Pension", "2222222222", 50000, 65)

# Llamar métodos
cuenta_ahorro.descripcion()
print(f"Número de cuenta: {cuenta_ahorro.get_numero_cuenta()}")
print(f"Saldo: ${cuenta_ahorro.get_saldo():,.2f}")
cuenta_ahorro.depositar(500)
print(f"Saldo después de depositar: ${cuenta_ahorro.get_saldo():,.2f}")
print(f"Interés: ${cuenta_ahorro.calcular_interes():,.2f}")

cuenta_corriente.descripcion()
print(f"Número de cuenta: {cuenta_corriente.get_numero_cuenta()}")
print(f"Saldo: ${cuenta_corriente.get_saldo():,.2f}")
cuenta_corriente.retirar(200)
print(f"Saldo después de retirar: ${cuenta_corriente.get_saldo():,.2f}")
print(f"Crédito disponible: ${cuenta_corriente.calcular_credito():,.2f}")

cuenta_hipotecaria.descripcion()
print(f"Número de cuenta: {cuenta_hipotecaria.get_numero_cuenta()}")
print(f"Saldo: ${cuenta_hipotecaria.get_saldo():,.2f}")
print(f"Cuota mensual: ${cuenta_hipotecaria.calcular_cuota():,.2f}")

cuenta_pension.descripcion()
print(f"Número de cuenta: {cuenta_pension