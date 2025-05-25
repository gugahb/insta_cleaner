import csv
import re
import sys
from analisados import carregar_analisados, salvar_analisado
from remover_depois import carregar_remover_depois, remover_usuario_da_lista
from remover import remover_seguidor_por_busca, log_remocao, analisar_seguidor

csv.field_size_limit(sys.maxsize)
REMOVER_LIMITE = 50

def remover_da_lista_json(page):
    lista = carregar_remover_depois()
    if not lista:
        print("📭 Nenhum usuário na fila de remoção.")
        return

    print("🗂️ Usuários para remover:")
    for u, motivo in lista.items():
        print(f" - @{u} → {motivo}")

    confirm = input("\nDeseja remover esses usuários agora? [s/N]: ").strip().lower()
    if confirm != "s":
        print("❌ Remoção cancelada.")
        return

    for username, motivo in list(lista.items()):
        print(f"🚨 Removendo @{username}... ({motivo})")
        sucesso = remover_seguidor_por_busca(page, username)
        if sucesso:
            log_remocao(username, motivo)
            remover_usuario_da_lista(username)
            page.wait_for_timeout(3000)

def carregar_seguidores_csv(caminho):
    seguidores = []
    with open(caminho, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            username = row.get("Username")
            followed_by_you = row.get("Followed By You")
            if username and (not followed_by_you or followed_by_you.strip().lower() != "yes"):
                seguidores.append(username.strip())
    return seguidores

def filtrar_por_padrao(seguidores, padrao):
    regex = re.compile(padrao, re.IGNORECASE)
    return [s for s in seguidores if regex.search(s)]

def processar_seguidores(page, seguidores):
    ja_analisados = carregar_analisados()
    removidos = []

    for username in seguidores:
        if username in ja_analisados:
            print(f"⏭️  @{username} já analisado, pulando...")
            continue

        print(f"🔍 Verificando @{username}")
        resultado = analisar_seguidor(page, username)
        salvar_analisado(username, "removido" if not resultado else "manter")

        if not resultado:
            removidos.append(username)
            if len(removidos) >= REMOVER_LIMITE:
                print(f"⚠️ Limite de {REMOVER_LIMITE} remoções atingido.")
                break

    if not removidos:
        print("✅ Nenhum perfil removido nesta execução.")

def remover_por_nome(page, seguidores, padrao="sorte"):
    ja_removidos = set()
    try:
        with open("remocoes_log.csv") as f:
            ja_removidos = {line.split(",")[1].strip("@") for line in f.readlines()}
    except FileNotFoundError:
        pass

    candidatos = [
        s for s in filtrar_por_padrao(seguidores, padrao)
        if s not in ja_removidos
    ]

    if not candidatos:
        print(f"🔍 Nenhum seguidor encontrado com o padrão '{padrao}'.")
        return

    print("\n🎯 Seguidores encontrados com base no padrão:")
    for s in candidatos:
        print(f" - @{s}")

    confirm = input("\nDeseja remover esses usuários? [s/N]: ").lower().strip()
    if confirm == 's':
        for username in candidatos[:REMOVER_LIMITE]:
            print(f"❌ Removendo @{username}... (por padrão '{padrao}')")
            remover_seguidor_por_busca(page, username)
            log_remocao(username, f"remocao_padrao_{padrao}")
            page.wait_for_timeout(3000)
    else:
        print("Nenhum usuário foi removido.")
