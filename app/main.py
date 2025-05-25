from playwright.sync_api import sync_playwright
from browser import login_instagram
from processar_csv_seguidores import (
    carregar_seguidores_csv,
    processar_seguidores,
    remover_por_nome,
    remover_da_lista_json,
)

CAMINHO_CSV = "seguidores.csv"

def menu():
    print("\n📋 MENU")
    print("1 - Verificar perfis inativos e autorizar remoção")
    print("2 - Remover seguidores com nome contendo 'sorte'")
    print("3 - Remover seguidores listados em remover_depois.json")
    print("4 - Sair")
    return input("Escolha uma opção: ").strip()

def main():
    with sync_playwright() as p:
        page, browser = login_instagram(p)

        seguidores = carregar_seguidores_csv(CAMINHO_CSV)
        if not seguidores:
            print("⚠️ Nenhum seguidor carregado do CSV.")
            return

        print(f"🔍 Total de seguidores carregados do CSV: {len(seguidores)}")

        while True:
            opcao = menu()
            if opcao == "1":
                processar_seguidores(page, seguidores)
            elif opcao == "2":
                remover_por_nome(page, seguidores, padrao="sorte")
            elif opcao == "3":
                remover_da_lista_json(page)
            elif opcao == "4":
                break
            else:
                print("❌ Opção inválida. Tente novamente.")

        browser.close()

if __name__ == "__main__":
    main()