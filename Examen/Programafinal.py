import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

def conectar_db():
    conexion = sqlite3.connect("almacen.db")
    conexion.execute("""
                create table if not exists medicamentos(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar NOT NULL, descripcion varchar NOT NULL,
                    precio integer NOT NULL, imagen blob NOT NULL)
    """)
    conexion.close()


def guardar_medicamento():
    conexion = sqlite3.connect("almacen.db")
    if nombre.get() == "" or descripcion.get() == "" or precio.get() == "":
        messagebox.showerror("Error", "Complete todos los datos por favor")
        return
    with open(imagen.get(), 'rb') as f:
        archivo_imagen = f.read()
    print(nombre.get())
    print(descripcion.get())
    int_precio = int(precio.get())
    print(int_precio)
    print(imagen.get())
    conexion.execute("insert into medicamentos(nombre, descripcion, precio, imagen) values (?,?,?,?)", (nombre.get(), descripcion.get(), int_precio, archivo_imagen))
    conexion.commit()
    conexion.close()
    ventana_nuevo.destroy()
    actualiza_listado()


def get_medicamentos():
    conexion = sqlite3.connect("almacen.db")
    cursor = conexion.cursor()
    registros_raw = cursor.execute("select * from medicamentos")
    registros_fetch = registros_raw.fetchall()
    print(registros_fetch)
    global registros
    registros = registros_fetch
    cursor.close()

def actualiza_listado():
    registros_lb.delete(0, tk.END)
    get_medicamentos()
    for registro in registros:
        registros_lb.insert(tk.END, registro)

def abrir_imagen():
    global imagen
    imagen.set(filedialog.askopenfilename(initialdir = "/", title="Select a File", filetypes=((".png","*.png*"),("all files","*.*"))))


def nuevo_medicamento():
    ventana_nuevo_medicamento = tk.Toplevel(ventana)
    ventana_nuevo_medicamento.title("Agregar medicamento")
    ventana_nuevo_medicamento.configure(bg="#FFF", padx=50, pady=50)

    #nombre
    nombre_label = tk.Label(ventana_nuevo_medicamento, text="Nombre:")
    nombre_label.grid(row=0, column=0, padx=(10, 0))
    nombre_label.configure(bg="#FFF")

    nombre_entry = tk.Entry(ventana_nuevo_medicamento)
    nombre_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

    #descripción
    descripcion_label = tk.Label(ventana_nuevo_medicamento, text="Descripción:")
    descripcion_label.grid(row=1, column=0, padx=(10,0))
    descripcion_label.configure(bg="#FFF")

    descripcion_entry = tk.Entry(ventana_nuevo_medicamento)
    descripcion_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 0))

    #precio
    precio_label = tk.Label(ventana_nuevo_medicamento, text="Precio:")
    precio_label.grid(row=2, column=0, padx=(10,0))
    precio_label.configure(bg="#FFF")

    precio_entry = tk.Entry(ventana_nuevo_medicamento)
    precio_entry.grid(row=2, column=1, padx=(0, 10), pady=(10, 0))

    #imagen
    imagen_entry = tk.Button(ventana_nuevo_medicamento, command=abrir_imagen, text="Buscar imagen")
    imagen_entry.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

    global nombre
    nombre = nombre_entry
    nombre.configure(width="50")
    global descripcion
    descripcion = descripcion_entry
    descripcion.configure(width="50")
    global precio
    precio = precio_entry
    precio.configure(width="50")
    global imagen
    imagen = StringVar()
    imagen_entry = tk.Button(ventana_nuevo_medicamento, command=abrir_imagen, text="Buscar imagen")
    imagen_entry.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

    global ventana_nuevo
    ventana_nuevo = ventana_nuevo_medicamento

    #button
    submit_button = tk.Button(ventana_nuevo_medicamento, command=guardar_medicamento, text="Añadir", bg="#002D4F", fg="#fff", width="30")
    submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

def verLista():
    registros_lb.pack(pady=20, padx=20)
    registros_lb.configure(font=('Arial', 11), width=300)

conectar_db()
get_medicamentos()
ventana = tk.Tk()
ventana.title("Examen 2")
ventana.configure(bg="#F0F0F0")
ventana.geometry("800x450") #ajustar tamaño
imagen = PhotoImage(file="PC.png") #llamar imagen en su ruta
fondo = Label(ventana, image=imagen).place(x=280, y=230) #posición
barra_menus = tk.Menu()

#menú.
menu = tk.Menu(barra_menus, tearoff=False)

#opciones del menú
barra_menus.add_cascade(menu=menu, label="Opciones")
menu.add_command(label="Agregar medicamento", accelerator="Ctrl+N", command=nuevo_medicamento)
menu.add_command(label="Ver medicamentos", accelerator="Ctrl+L", command=verLista)
ventana.config(menu=barra_menus)
registros_lb = tk.Listbox(ventana)
for registro in registros:
    registros_lb.insert(tk.END, registro)

mensaje = tk.Label(ventana, text="Los mejores productos para las enfermedades más comunes")
mensaje.pack(pady=20)
mensaje.configure(font=('Arial', 14))
    
ventana.mainloop()