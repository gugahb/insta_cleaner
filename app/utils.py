def verificar_status_perfil(page, username):
    try:
        # Remove timeouts fixos
        if page.title() == "Página não encontrada • Instagram":
            print(f"⚠️ Conta @{username} parece desativada ou inexistente.")
            return "conta desativada"

        # Verifica elementos que indicam perfil sem conteúdo
        sem_postagens = page.query_selector("h2:has-text('Ainda não há publicações')")
        if sem_postagens:
            return "sem postagens"

        return "ativo"
    except Exception as e:
        print(f"⚠️ Erro ao verificar status de @{username}: {e}")
        return "erro_verificacao"