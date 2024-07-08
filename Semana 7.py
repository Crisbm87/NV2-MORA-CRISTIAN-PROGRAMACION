class Resource:
    def __init__(self, name):
        """
        Constructor de la clase Resource.
        Se llama automáticamente cuando se crea una instancia de la clase.

        Args:
            name (str): El nombre del recurso.
        """
        self.name = name
        self.resource_file = None
        self.open_resource()
        print(f"Recurso {self.name} creado.")

    def open_resource(self):
        """
        Método para abrir (inicializar) el recurso.
        """
        self.resource_file = open(f"{self.name}.txt", "w")
        self.resource_file.write("Este es un recurso de ejemplo.\n")
        print(f"Recurso {self.name} abierto y escrito.")

    def close_resource(self):
        """
        Método para cerrar (limpiar) el recurso.
        """
        if self.resource_file:
            self.resource_file.close()
            self.resource_file = None
            print(f"Recurso {self.name} cerrado.")

    def __del__(self):
        """
        Destructor de la clase Resource.
        Se llama automáticamente cuando se elimina una instancia de la clase.
        """
        self.close_resource()
        print(f"Recurso {self.name} destruido.")


# Demostración de uso de la clase Resource
if __name__ == "__main__":
    # Crear un recurso
    resource1 = Resource("mi_recurso")

    # Realizar algunas operaciones con el recurso
    resource1.resource_file.write("Añadiendo más contenido al recurso.\n")

    # Cerrar el recurso manualmente
    resource1.close_resource()

    # Crear otro recurso para ver el destructor en acción
    resource2 = Resource("otro_recurso")

    # Al final del script, el destructor se llamará automáticamente
    # para cualquier instancia que no haya sido eliminada explícitamente.
