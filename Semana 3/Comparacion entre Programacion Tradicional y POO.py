Programación Tradicional


def obtener_temperaturas_semanales():
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_temperatura(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultados_promedio(promedio):
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

def main():
    temperaturas = obtener_temperaturas_semanales()
    promedio = calcular_promedio_temperatura(temperaturas)
    mostrar_resultados_promedio(promedio)

if __name__ == "__main__":
    main()




Programación Orientada a Objetos (POO)


class ClimaSemana:
    def __init__(self):
        self.temperaturas = []

    def agregar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio_temperatura(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_resultados_promedio(self):
        promedio = self.calcular_promedio_temperatura()
        print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

def main():
    clima = ClimaSemana()
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        clima.agregar_temperatura(temperatura)
    clima.mostrar_resultados_promedio()

if __name__ == "__main__":
    main()