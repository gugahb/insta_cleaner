def abrir_lista_de_seguidores(page, perfil="gugahb"):
    page.goto(f"https://www.instagram.com/{perfil}/")
    page.wait_for_selector("a[href$='/followers/']", timeout=15000)
    page.click("a[href$='/followers/']")

    input("🕵️ Cliquei em 'seguidores'. Aguarde o modal abrir e aperte ENTER quando estiver visível...")

    page.wait_for_selector("div[role='dialog']", timeout=15000)
    page.wait_for_timeout(2000)

    # Faz scroll no modal para carregar mais seguidores
    try:
        scroll_box = page.wait_for_selector("div[role='dialog'] div._aano", timeout=10000)
    except:
        print("❌ Não foi possível localizar o container de rolagem (._aano).")
        return []

    for _ in range(100):
        try:
            scroll_box.evaluate("el => el.scrollBy(0, el.scrollHeight)")
            page.wait_for_timeout(1000)
        except Exception as e:
            print(f"⚠️ Erro ao rolar: {e}")
            break

    seguidores = set()
    lista_items = page.query_selector_all("div[role='dialog'] li")
    print(f"📋 Total de <li> encontrados no modal: {len(lista_items)}")

    for item in lista_items:
        link = item.query_selector("a[href^='/']")
        if link:
            href = link.get_attribute("href")
            if href and href.startswith("/") and href.count("/") == 2:
                username = href.strip("/").split("/")[0]
                seguidores.add(username)

    print(f"🔎 Total de seguidores extraídos: {len(seguidores)}")

    # Armazena a lista para uso posterior
    with open("seguidores_extraidos.txt", "w") as f:
        for nome in sorted(seguidores):
            f.write(f"{nome}\n")

    return list(seguidores)
