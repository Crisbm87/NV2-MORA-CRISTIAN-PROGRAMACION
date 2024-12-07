import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_dato():
    dato = entry_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entry_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista de datos
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Datos")

# Etiqueta para el campo de texto
label_dato = tk.Label(ventana, text="Ingrese un dato:")
label_dato.pack(pady=5)

# Campo de texto para ingresar datos
entry_dato = tk.Entry(ventana)
entry_dato.pack(pady=5)

# Botón para agregar datos a la lista
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos ingresados
lista_datos = tk.Listbox(ventana, height=10)
lista_datos.pack(pady=5)

# Botón para limpiar la lista de datos
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
