import tkinter as tk
from tkinter import ttk
import json

# Carregando dados do arquivo JSON
with open("dados_plantas.json", "r") as arquivo_json:
    dados_plantas = json.load(arquivo_json)

def preencher_tabela():
    for planta in dados_plantas:
        tree.insert("", "end", values=(planta["nome"], planta["tamanho"], planta["cor"], planta["ambiente"]))

app = tk.Tk()
app.title("Lista de Plantas")

frame = tk.Frame(app)
frame.pack()

label = tk.Label(frame, text="Lista de Plantas")
label.pack(pady=10)

tree = ttk.Treeview(frame, columns=("Nome", "Tamanho", "Cor", "Ambiente"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Tamanho", text="Tamanho")
tree.heading("Cor", text="Cor")
tree.heading("Ambiente", text="Ambiente")
tree.pack()

preencher_tabela()

app.mainloop()
