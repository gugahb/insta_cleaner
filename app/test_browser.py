import os
os.environ["DISPLAY"] = ":0"

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    input("Pressione ENTER para fechar...")
    browser.close()
