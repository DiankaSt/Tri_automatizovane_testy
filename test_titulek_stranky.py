import re
from playwright.sync_api import Page, expect

def test_titulek_stranky_obsahuje_engeto(page: Page):
    page.goto("https://engeto.cz/")
    expect(page).to_have_title(re.compile("ENGETO", re.IGNORECASE))
