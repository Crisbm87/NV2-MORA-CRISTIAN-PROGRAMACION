# Clase base: Vehículo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self.modelo = modelo  # Atributo público
        self._precio = None  # Atributo protegido

    def mostrar_informacion(self):
        """ Método para mostrar la información básica del vehículo """
        print(f"Vehículo: {self.marca} {self.modelo}")

    def calcular_impuesto(self):
        """ Método para calcular el impuesto básico """
        return 0  # Impuesto básico, puede variar por tipo de vehículo

    # Getter y Setter para el atributo protegido _precio
    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        if precio > 0:
            self._precio = precio
        else:
            print("El precio debe ser mayor que cero.")

    # Método que puede ser sobreescrito en la clase derivada
    def describir(self):
        """ Método genérico para describir el vehículo """
        print(f"Este vehículo es de marca {self.marca}, modelo {self.modelo}")


# Clase derivada: Coche, hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)
        self.tipo_motor = tipo_motor  # Atributo específico de Coche

    def describir(self):
        """ Método sobreescrito para describir un coche específicamente """
        print(f"Este coche es un {self.marca} {self.modelo} con motor {self.tipo_motor}")

    def calcular_impuesto(self):
        """ Método sobreescrito para calcular impuestos de coches """
        return super().calcular_impuesto() + 5000  # Impuesto específico para coches + básico


# Ejemplo de polimorfismo con función que usa los objetos de manera genérica
def mostrar_informacion_vehiculos(vehiculos):
    for vehiculo in vehiculos:
        vehiculo.mostrar_informacion()
        print(f"Impuesto a pagar: ${vehiculo.calcular_impuesto()}")

# Programa principal
if __name__ == "__main__":
    # Crear instancias de las clases
    vehiculo_generico = Vehiculo("MarcaGen", "ModeloGen")
    coche = Coche("Toyota", "Corolla", "Gasolina")

    # Utilización de métodos y demostración de la funcionalidad
    vehiculo_generico.mostrar_informacion()
    print(f"Precio actual: ${vehiculo_generico.get_precio()}")
    vehiculo_generico.set_precio(15000)
    print(f"Precio actualizado: ${vehiculo_generico.get_precio()}")

    print()  # Línea en blanco para separar la salida

    coche.describir()
    print(f"Impuesto a pagar por el coche: ${coche.calcular_impuesto()}")

    print()  # Línea en blanco para separar la salida

    # Ejemplo de polimorfismo usando la función mostrar_informacion_vehiculos
    vehiculos = [vehiculo_generico, coche]
    mostrar_informacion_vehiculos(vehiculos)
