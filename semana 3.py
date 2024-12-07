def ingresar_temperaturas():
    """
    Solicita al usuario que ingrese las temperaturas diarias para una semana.
    :return: Una lista de temperaturas diarias.
    """
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias_semana:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura para el {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    :param temperaturas: Lista de temperaturas.
    :return: El promedio de las temperaturas.
    """
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal que organiza la entrada de datos y el cálculo del promedio.
    """
    print("Programa para calcular el promedio de temperaturas semanales.")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)

    print(f"Las temperaturas ingresadas son: {temperaturas}")
    print(f"El promedio de las temperaturas es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()

