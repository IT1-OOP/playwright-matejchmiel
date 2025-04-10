from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("file://" + "index.html")  # Načte lokální HTML soubor
    print(page.title())  # Vypíše titulek stránky
    browser.close()