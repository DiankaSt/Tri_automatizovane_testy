from playwright.sync_api import Page, expect

def test_hlavni_menu_je_viditelne(page: Page):
    page.goto("https://engeto.cz/")
    # Najde hlavní menu podle běžných selektorů
    hlavni_menu = page.locator("nav.main-menu, nav#menu, nav")
    # Ověří, že hlavní menu je viditelné
    expect(hlavni_menu).to_be_visible()
