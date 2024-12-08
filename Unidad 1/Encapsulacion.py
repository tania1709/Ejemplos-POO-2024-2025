class Banco:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

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
        self.__tasa_interes = tasa_interes

    def get_tasa_interes(self):
        return self.__tasa_interes

    def calcular_interes(self):
        return self.get_saldo() * self.__tasa_interes / 100

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre, numero_cuenta, saldo, limite_credito):
        super().__init__(nombre, numero_cuenta, saldo)
        self.__limite_credito = limite_credito

    def get_limite_credito(self):
        return self.__limite_credito

    def calcular_credito(self):
        return self.__limite_credito - self.get_saldo()

class CuentaHipotecaria(CuentaBancaria):
    def __init__(self, nombre, numero_cuenta, saldo, plazo):
        super().__init__(nombre, numero_cuenta, saldo)
        self.__plazo = plazo

    def get_plazo(self):
        return self.__plazo

    def calcular_cuota(self):
        return self.get_saldo() / self.__plazo

class CuentaPension(CuentaBancaria):
    def __init__(self, nombre, numero_cuenta, saldo, edad):
        super().__init__(nombre, numero_cuenta, saldo)
        self.__edad = edad

    def get_edad(self):
        return self.__edad

    def calcular_pension(self):
        if self.__edad >= 65:
            return self.get_saldo() * 0.1
        else:
            return 0

# Instanciar objetos
cuenta_ahorro = CuentaAhorro("Banco Nacional", "1234567890", 1000, 5)
cuenta_corriente = CuentaCorriente("Banco Internacional", "9876543210", 500, 2000)
cuenta_hipotecaria = CuentaHipotecaria("Banco de la Vivienda", "1111111111", 200000, 20)
cuenta_pension = CuentaPension("Banco de la Pension", "2222222222", 50000, 65)

# Llamar métodos
print(cuenta_ahorro.get_nombre())
print(cuenta_ahorro.get_numero_cuenta())
print(cuenta_ahorro.get_saldo())
cuenta_ahorro.depositar(500)
print(cuenta_ahorro.get_saldo())
print(cuenta_ahorro.get_tasa_interes())
print(cuenta_ahorro.calcular_interes())

print(cuenta_corriente.get_nombre())
print(cuenta_corriente.get_numero_cuenta())
print(cuenta_corriente.get_saldo())
cuenta_corriente.retirar(200)
print(cuenta_corriente.get_saldo())
print(cuenta_corriente.get_limite_credito())
print(cuenta_corriente.calcular_credito())

print(cuenta_hipotecaria.get_nombre())
print(cuenta_hipotecaria.get_numero_cuenta())
print(cuenta_hipotecaria.get_saldo())
print(cuenta_hipotecaria.get_plazo())
print(cuenta_hipotecaria.calcular_cuota())

print(cuenta_pension.get_nombre())
print(cuenta_pension.get_numero_cuenta())
print(cuenta_pension.get_saldo())
print(cuenta_pension.get_edad())
print(cuenta_pension.calcular_pension())
