Tento projekt obsahuje tři automatizované testy napsané v Pythonu s využitím frameworku Playwright a pytest-playwright. 

Testují základní funkčnost webové stránky engeto.cz.

Instalace:

pip install pytest pytest-playwright

playwright install

Spuštění testů
pytest (všechny najednou) 
pytest test_titulek_stranky.py (jednotlivě)

Popis testů
1. test_titulek_stranky.py
Ověřuje, že titulek hlavní stránky obsahuje slovo „ENGETO“ (bez ohledu na velikost písmen).

2. test_hlavni_menu.py
Ověřuje, že hlavní menu je na stránce viditelné.

3. test_odkazu.py
Ověřuje, že na stránce je viditelný odkaz s přesným názvem „Python Akademie“.
