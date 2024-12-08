class CuentaBancaria:
    def __init__(self, nombre, numero_cuenta, saldo):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad} en la cuenta de {self.nombre}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f"No hay suficiente saldo en la cuenta de {self.nombre}")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} de la cuenta de {self.nombre}")

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

    def verificar_limite_credito(self, cantidad):
        if cantidad > self.limite_credito:
            print(f"La cantidad supera el límite de crédito de {self.limite_credito}")
            return False
        else:
            return True

# Crear objetos
cuenta_ahorro = CuentaAhorro("Juan", "123456789", 1000, 5)
cuenta_corriente = CuentaCorriente("María", "987654321", 500, 2000)

# Utilizar métodos
cuenta_ahorro.depositar(500)
cuenta_ahorro.retirar(200)
print(f"Intereses de la cuenta de ahorro: {cuenta_ahorro.calcular_interes()}")

cuenta_corriente.depositar(1000)
cuenta_corriente.retirar(1500)
if cuenta_corriente.verificar_limite_credito(2500):
    cuenta_corriente.retirar(2500)
