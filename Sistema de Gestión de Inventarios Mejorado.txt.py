class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}"

    @classmethod
    def from_string(cls, producto_str):
        codigo, nombre, cantidad, precio = producto_str.strip().split(',')
        return cls(codigo, nombre, int(cantidad), float(precio))
import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    producto = Producto.from_string(linea)
                    self.productos[producto.codigo] = producto
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Creando uno nuevo.")
            self.guardar_inventario()
        except PermissionError:
            print(f"Error: Permisos insuficientes para leer el archivo {self.archivo}.")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
        except PermissionError:
            print(f"Error: Permisos insuficientes para escribir en el archivo {self.archivo}.")

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print(f"Error: El producto con código {producto.codigo} ya existe.")
        else:
            self.productos[producto.codigo] = producto
            self.guardar_inventario()
            print(f"Producto {producto.nombre} agregado exitosamente.")

    def actualizar_producto(self, codigo, nombre=None, cantidad=None, precio=None):
        if codigo in self.productos:
            producto = self.productos[codigo]
            if nombre:
                producto.nombre = nombre
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto {codigo} actualizado exitosamente.")
        else:
            print(f"Error: El producto con código {codigo} no existe.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
            print(f"Producto {codigo} eliminado exitosamente.")
        else:
            print(f"Error: El producto con código {codigo} no existe.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos.values():
                print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar Producto")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Mostrar Productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            codigo = input("Código del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(codigo, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            codigo = input("Código del producto a actualizar: ")
            nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(codigo, nombre, cantidad, precio)

        elif opcion == '3':
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)

        elif opcion == '4':
            inventario.mostrar_productos()

        elif opcion == '5':
            print("Saliendo del sistema de gestión de inventarios.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
