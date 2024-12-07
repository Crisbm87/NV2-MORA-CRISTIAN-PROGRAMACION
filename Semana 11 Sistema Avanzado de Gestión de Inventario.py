class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio
import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print(f"Error: El producto con ID {producto.id} ya existe.")
        else:
            self.productos[producto.id] = producto
            print(f"Producto {producto.nombre} agregado exitosamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado exitosamente.")
        else:
            print(f"Error: Producto con ID {id} no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id].actualizar_precio(precio)
            print(f"Producto con ID {id} actualizado exitosamente.")
        else:
            print(f"Error: Producto con ID {id} no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'w') as archivo:
                json.dump({id: vars(producto) for id, producto in self.productos.items()}, archivo)
            print(f"Inventario guardado en {nombre_archivo}.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                productos_cargados = json.load(archivo)
                for id, datos in productos_cargados.items():
                    self.productos[int(id)] = Producto(**datos)
            print(f"Inventario cargado desde {nombre_archivo}.")
        except FileNotFoundError:
            print(f"Archivo {nombre_archivo} no encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Cargar inventario desde archivo")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            nombre_archivo = input("Ingrese el nombre del archivo para guardar: ")
            inventario.guardar_en_archivo(nombre_archivo)

        elif opcion == '7':
            nombre_archivo = input("Ingrese el nombre del archivo para cargar: ")
            inventario.cargar_desde_archivo(nombre_archivo)

        elif opcion == '8':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    menu()
