import tkinter as tk
from tkinter import ttk
import json

def salvar_planta():
    nome = nome_planta.get()
    tamanho = tamanho_planta.get()
    cor = cor_planta.get()
    ambiente = ambiente_planta.get()

    planta = {"nome": nome, "tamanho": tamanho, "cor": cor, "ambiente": ambiente}

    with open("dados_plantas.json", "r") as arquivo_json:
        dados_plantas = json.load(arquivo_json)

    dados_plantas.append(planta)

    with open("dados_plantas.json", "w") as arquivo_json:
        json.dump(dados_plantas, arquivo_json, indent=4)

    limpar_campos()

def limpar_campos():
    nome_planta.set("")
    tamanho_planta.set("")
    cor_planta.set("")
    ambiente_planta.set("")

app = tk.Tk()
app.title("Adicionar Planta")

frame = tk.Frame(app)
frame.pack()

label = tk.Label(frame, text="Adicionar Planta")
label.pack(pady=10)

label_nome = tk.Label(frame, text="Nome:")
label_nome.pack()
nome_planta = tk.StringVar()
entrada_nome = tk.Entry(frame, textvariable=nome_planta)
entrada_nome.pack()

label_tamanho = tk.Label(frame, text="Tamanho:")
label_tamanho.pack()
tamanho_planta = tk.StringVar()
entrada_tamanho = tk.Entry(frame, textvariable=tamanho_planta)
entrada_tamanho.pack()

label_cor = tk.Label(frame, text="Cor:")
label_cor.pack()
cor_planta = tk.StringVar()
entrada_cor = tk.Entry(frame, textvariable=cor_planta)
entrada_cor.pack()

label_ambiente = tk.Label(frame, text="Ambiente:")
label_ambiente.pack()
ambiente_planta = tk.StringVar()
entrada_ambiente = tk.Entry(frame, textvariable=ambiente_planta)
entrada_ambiente.pack()

botao_salvar = tk.Button(frame, text="Salvar Planta", command=salvar_planta)
botao_salvar.pack()

app.mainloop()
