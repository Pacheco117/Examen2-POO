import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Medicamentos")
medicamentos = [    ("Ibuprofeno", "El ibuprofeno es un antiinflamatorio no esteroideo (AINE) que se utiliza para aliviar el dolor y reducir la fiebre.", "ruta/a/imagen1.jpg"),    ("Acetaminofén", "El acetaminofén es un analgésico que se utiliza para aliviar el dolor y reducir la fiebre.", "ruta/a/imagen2.jpg"),    ("Aspirina", "La aspirina es un analgésico y antiinflamatorio que se utiliza para aliviar el dolor y reducir la fiebre.", "C:\Users\Sergio\Documents\pythonscripts\Proyect2-POO\Aspirina.jpg")]


tree = ttk.Treeview(root, columns=("nombre", "descripcion", "imagen"), show="headings")

tree.heading("nombre", text="Nombre")
tree.heading("descripcion", text="Descripción")
tree.heading("imagen", text="Imagen")

def cargar_imagen(ruta):
    imagen = Image.open(ruta)
    imagen = imagen.resize((100, 100), Image.ANTIALIAS)
    return ImageTk.PhotoImage(imagen)

for medicamento in medicamentos:
    imagen = cargar_imagen(medicamento[2])
    tree.insert("", tk.END, values=(medicamento[0], medicamento[1], imagen))