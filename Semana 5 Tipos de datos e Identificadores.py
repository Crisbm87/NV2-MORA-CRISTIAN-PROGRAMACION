# Calculadora de Áreas de Figuras Geométricas
# Este programa permite calcular el área de un círculo, cuadrado o triángulo según la elección del usuario.

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    import math
    return math.pi * (radio ** 2)


def calcular_area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el tamaño de uno de sus lados."""
    return lado ** 2


def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dada su base y altura."""
    return (base * altura) / 2


def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("Calculadora de Áreas")
    print("1. Calcular área de un círculo")
    print("2. Calcular área de un cuadrado")
    print("3. Calcular área de un triángulo")
    print("4. Salir")


def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area:.2f}")
        elif opcion == '2':
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            print(f"El área del cuadrado es: {area:.2f}")
        elif opcion == '3':
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print(f"El área del triángulo es: {area:.2f}")
        elif opcion == '4':
            print("Gracias por utilizar la calculadora de áreas.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        print()  # Imprimir una línea en blanco para mejor legibilidad.


# Ejecutar la función principal
if __name__ == "__main__":
    main()
