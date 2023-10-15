import json

dados_plantas = [
    {"nome": "Planta 1", "tamanho": "Pequeno", "cor": "Verde", "ambiente": "Sala"},
    {"nome": "Planta 2", "tamanho": "Médio", "cor": "Vermelho", "ambiente": "Quarto"},
    {"nome": "Planta 3", "tamanho": "Grande", "cor": "Azul", "ambiente": "Cozinha"}
]

# Salvar os dados no arquivo JSON
with open("dados_plantas.json", "w") as arquivo_json:
    json.dump(dados_plantas, arquivo_json)
