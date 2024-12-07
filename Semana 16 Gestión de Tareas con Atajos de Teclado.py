import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas Semana 16")
        self.root.geometry("600x600")

        # Crear la entrada de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=40)
        self.entry.bind("<Return>", self.add_task)  # Atajo para agregar tarea con Enter

        # Botones para gestionar las tareas
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(root, text="Marcar Completada", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=10)
        self.task_listbox.pack(pady=10)

        # Atajos de teclado
        root.bind("<Escape>", lambda event: root.quit())  # Cerrar con Escape
        root.bind("<Delete>", lambda event: self.delete_task())  # Eliminar con Delete
        root.bind("<d>", lambda event: self.delete_task())  # Eliminar con 'D'
        root.bind("<c>", lambda event: self.complete_task())  # Completar con 'C'

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, f"{task} - COMPLETADA")
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para completar")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
