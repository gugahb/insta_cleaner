import re
from datetime import datetime
from utils import verificar_status_perfil
from remover_depois import adicionar_para_remover

def analisar_seguidor(page, username):
    try:
        page.goto(f"https://www.instagram.com/{username}/", timeout=30000)
        if f"/{username.lower()}/" not in page.url:
            print(f"🚫 URL incorreta: {page.url}")
            adicionar_para_remover(username, "url_incorreta")
            return False

        status = verificar_status_perfil(page, username)
        if status != "ativo":
            print(f"📛 @{username} está {status}")
            adicionar_para_remover(username, f"status_{status}")
            return False

        page.wait_for_load_state('networkidle', timeout=20000)

        # 👇 Aqui é o novo trecho robusto
        try:
            page.wait_for_selector("header li", timeout=8000)

            posts_text = page.locator("header li").nth(0).locator("span").first.inner_text()
            seguidores_text = page.locator("header li").nth(1).locator("span").first.inner_text()
            seguindo_text = page.locator("header li").nth(2).locator("span").first.inner_text()
        except Exception as e:
            print(f"⚠️ Falha ao localizar estatísticas: {e}")
            adicionar_para_remover(username, "info_incompleta")
            return False

        def limpar(txt): return int(re.sub(r"[^\d]", "", txt))
        posts = limpar(posts_text)
        seguidores = limpar(seguidores_text)
        seguindo = limpar(seguindo_text)

        print(f"📊 @{username} → Posts: {posts}, Seguidores: {seguidores}, Seguindo: {seguindo}")

        if posts < 10:
            adicionar_para_remover(username, "menos_de_10_posts")
            return False

        if seguidores > 0:
            razao = seguindo / seguidores
            if razao > 4:
                print(f"📛 @{username} tem razão seguindo/seguidores = {razao:.2f}")
                adicionar_para_remover(username, "seguindo_mais_que_3x")
                return False
        else:
            print(f"⚠️ @{username} com 0 seguidores, ignorando cálculo da razão.")

        print(f"✅ @{username} não atende aos critérios de remoção.")
        return True

    except Exception as e:
        print(f"❌ Erro ao analisar @{username}: {e}")
        adicionar_para_remover(username, "erro_geral")
        return False


def remover_seguidor_por_busca(page, username, perfil="gugahb"):
    print(f"🔍 Buscando @{username} na sua lista de seguidores...")

    page.goto(f"https://www.instagram.com/{perfil}/followers/")
    page.wait_for_timeout(3000)

    try:
        search_input = page.wait_for_selector("input[placeholder='Search']", timeout=10000)
        search_input.fill(username)
        page.wait_for_timeout(10000)

        no_result = page.query_selector("text=No results found.")
        if no_result:
            print(f"⚠️ @{username} não encontrado na sua lista de seguidores.")
            return False

        link_usuario = page.query_selector(f"a[href='/{username.lower()}/']")
        if not link_usuario:
            print(f"⚠️ O usuário exibido não corresponde a @{username}.")
            return False

        botao = page.wait_for_selector("div[role='button']:has-text('Remove')", timeout=8000)
        page.wait_for_timeout(3000)
        botao.click()

        confirmar = page.query_selector("button:has-text('Remove')")
        if confirmar:
            confirmar.click()

        print(f"✅ @{username} removido com sucesso!")
        return True

    except Exception as e:
        print(f"⚠️ Erro ao tentar remover @{username}: {e}")
        return False


def log_remocao(username, motivo):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("remocoes_log.csv", "a") as f:
        f.write(f"{timestamp},@{username},{motivo}\n")
