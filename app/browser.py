import os

def login_instagram(p):
    iphone_12 = p.devices["iPhone 12"]  # ou outro modelo, como "Pixel 5"

    browser = p.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
        **iphone_12,
        storage_state="cookies/ig.json" if os.path.exists("cookies/ig.json") else None
    )

    page = context.new_page()

    if not os.path.exists("cookies/ig.json"):
        page.goto("https://www.instagram.com/accounts/login/")
        input("⚠️ Faça login manualmente (inclusive 2FA) e aperte ENTER aqui quando estiver na home.")
        context.storage_state(path="cookies/ig.json")
    else:
        page.goto("https://www.instagram.com/")

    return page, browser
