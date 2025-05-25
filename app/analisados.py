import json
import os

CAMINHO_CACHE = "seguidores_analisados.json"

def carregar_analisados():
    if not os.path.exists(CAMINHO_CACHE):
        return set()
    with open(CAMINHO_CACHE, "r") as f:
        data = json.load(f)
        return set(data.get("analisados", {}).keys())

def salvar_analisado(username, status):
    data = {"analisados": {}}
    if os.path.exists(CAMINHO_CACHE):
        with open(CAMINHO_CACHE, "r") as f:
            data = json.load(f)
    data["analisados"][username] = status
    with open(CAMINHO_CACHE, "w") as f:
        json.dump(data, f, indent=2)
