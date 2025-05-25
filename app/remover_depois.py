import json
import os

CAMINHO = "remover_depois.json"

def carregar_remover_depois():
    if not os.path.exists(CAMINHO):
        return {}
    with open(CAMINHO, "r") as f:
        return json.load(f)

def salvar_remover_depois(data):
    with open(CAMINHO, "w") as f:
        json.dump(data, f, indent=2)

def adicionar_para_remover(username, motivo):
    dados = carregar_remover_depois()
    dados[username] = motivo
    salvar_remover_depois(dados)

def remover_usuario_da_lista(username):
    dados = carregar_remover_depois()
    if username in dados:
        del dados[username]
        salvar_remover_depois(dados)
