import tkinter as tk
import mysql.connector
from tkinter import ttk

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escuela"
)

mi_cursor = bd.cursor()
mi_cursor.execute("SELECT * from alumnos")
resultado = mi_cursor.fetchall()

# crear ventana de Tkinter
ventana = tk.Tk()
ventana.title("Lista de alumnos")

# crear Table
tabla = ttk.Treeview(ventana)
tabla['columns'] = ('ID', 'Nombre')

# ajustar las columnas
tabla.column('#0', width=0, stretch=tk.NO)
tabla.column('ID', anchor=tk.CENTER, width=200)
tabla.column('Nombre', anchor=tk.CENTER, width=100)

# heading
tabla.heading('#0', text='', anchor=tk.CENTER)
tabla.heading('ID', text='Nombre', anchor=tk.CENTER)
tabla.heading('Nombre', text='Edad', anchor=tk.CENTER)

# agregar datos
for alumno in resultado:
  tabla.insert(parent='', index='end', iid=alumno[0], values=(alumno[1], alumno[2]))

# mostrar tabla en ventana
tabla.pack()

ventana.mainloop()