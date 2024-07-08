from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/busco_filmes.feature')


@given('que estou na página Goden Movie Studio')
def pagina_golden_movie_studio(browser: Page):
    browser.goto('http://127.0.0.1:8080/')


@when("Busco por filmes")
def busco_pelo_filme(browser: Page):
    browser.locator('[placeholder="Digite o nome do filme..."]').fill('The Matrix')
    browser.get_by_text('Buscar', exact=True).click()
    browser.locator('[placeholder="Digite o nome do filme..."]').fill('Inception')
    browser.get_by_text('Buscar', exact=True).click()
    browser.locator('[placeholder="Digite o nome do filme..."]').fill('The Godfather')
    browser.get_by_text('Buscar', exact=True).click()
    browser.locator('[placeholder="Digite o nome do filme..."]').fill('Interstellar')
    browser.get_by_text('Buscar', exact=True).click()


@then("valido se a busca foi realizada com sucesso")
def validar_se_os_filmes_existem(browser: Page):
    browser.wait_for_selector("text=Interstellar", timeout=10000)
    browser.wait_for_selector("text=The Matrix", timeout=10000)
    browser.wait_for_selector("text=Inception", timeout=10000)
    browser.wait_for_selector("text=The Godfather", timeout=10000)
