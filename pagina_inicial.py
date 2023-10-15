import tkinter as tk
import os

def abrir_adicionar_planta():
    os.system('python adicionar_planta.py')

def abrir_lista_de_plantas():
    os.system('python lista_de_plantas.py')

app = tk.Tk()
app.title("Gerenciador de Plantas")

frame = tk.Frame(app)
frame.pack()

label = tk.Label(frame, text="Página Inicial")
label.pack(pady=10)

botao_adicionar = tk.Button(frame, text="Adicionar Planta", command=abrir_adicionar_planta)
botao_adicionar.pack()

botao_lista = tk.Button(frame, text="Lista de Plantas", command=abrir_lista_de_plantas)
botao_lista.pack()

app.mainloop()
