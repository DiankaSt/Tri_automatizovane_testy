from playwright.sync_api import Page, expect

def test_odkaz_python_akademie_je_viditelny(page: Page):
    # Otevře hlavní stránku Engeto.cz
    page.goto("https://engeto.cz/")
    # Najde odkaz s názvem "Python Akademie"
    odkaz = page.get_by_role("link", name="Python Akademie", exact=True)
    # Ověří, že tento odkaz je na stránce viditelný
    expect(odkaz).to_be_visible()
