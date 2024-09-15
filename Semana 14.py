import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

# Función para agregar un nuevo evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        try:
            # Comprobar si la fecha y la hora tienen el formato correcto
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
            datetime.datetime.strptime(hora, '%H:%M')
            treeview.insert('', 'end', values=(fecha, hora, descripcion))
            entry_fecha.delete(0, tk.END)
            entry_hora.delete(0, tk.END)
            entry_descripcion.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error de formato", "La fecha debe ser Año-Mes-Día y la hora HH:MM")
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")

# Función para eliminar el evento seleccionado
def eliminar_evento():
    seleccionado = treeview.selection()
    if seleccionado:
        treeview.delete(seleccionado)
    else:
        messagebox.showwarning("Selección", "Por favor, selecciona un evento para eliminar.")

# Función para cerrar la aplicación
def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Eventos Semana 14")
ventana.geometry("650x500")

# Crear los widgets para los campos de entrada
label_fecha = tk.Label(ventana, text="Fecha (Año-Mes-Día):")
label_fecha.pack(pady=5)
entry_fecha = tk.Entry(ventana)
entry_fecha.pack(pady=5)

label_hora = tk.Label(ventana, text="Hora (HH:MM):")
label_hora.pack(pady=5)
entry_hora = tk.Entry(ventana)
entry_hora.pack(pady=5)

label_descripcion = tk.Label(ventana, text="Descripción:")
label_descripcion.pack(pady=5)
entry_descripcion = tk.Entry(ventana)
entry_descripcion.pack(pady=5)

# Crear el TreeView para mostrar la lista de eventos
treeview = ttk.Treeview(ventana, columns=("Fecha", "Hora", "Descripción"), show="headings")
treeview.heading("Fecha", text="Fecha")
treeview.heading("Hora", text="Hora")
treeview.heading("Descripción", text="Descripción")
treeview.pack(pady=20, fill=tk.BOTH, expand=True)

# Crear los botones para las acciones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=0, column=0, padx=10)

boton_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.grid(row=0, column=1, padx=10)

boton_salir = tk.Button(frame_botones, text="Salir", command=salir)
boton_salir.grid(row=0, column=2, padx=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
