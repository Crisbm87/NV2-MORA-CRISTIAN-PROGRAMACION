import tkinter as tk

class TaskManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Tareas Semana 15")
        self.geometry("400x400")

        # Crear los elementos de la interfaz
        self.task_entry = tk.Entry(self)
        self.task_entry.pack(pady=10)

        self.task_list = tk.Listbox(self)
        self.task_list.pack(pady=10)

        add_button = tk.Button(self, text="Añadir Tarea", command=self.add_task)
        add_button.pack()

        complete_button = tk.Button(self, text="Marcar como Completada", command=self.complete_task)
        complete_button.pack()

        delete_button = tk.Button(self, text="Eliminar Tarea", command=self.delete_task)
        delete_button.pack()

        # Lista para almacenar las tareas y su estado
        self.tasks = []

        # Asociar la pulsación de Enter con la función de agregar tarea
        self.task_entry.bind("<Return>", self.add_task)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]
            self.task_list.delete(selected_index)
            self.tasks.remove(selected_task)
            # Puedes agregar lógica aquí para marcar la tarea como completada en algún almacenamiento persistente

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index)
            del self.tasks[selected_index[0]]

if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()
