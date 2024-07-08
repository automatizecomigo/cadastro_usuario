from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_bdd.parsers import parse
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


@then(parse("valido se a busca foi realizada com sucesso"), converters=dict(texto=str))
def validar_se_os_filmes_existem(browser: Page):
    expect(browser.get_by_text('The Matrix')).to_be_visible()
    expect(browser.get_by_text('Inception')).to_be_visible()
    expect(browser.get_by_text('The Godfather Part II', exact=True)).not_to_be_visible()
    expect(browser.get_by_text('Jurassic Park III', exact=True)).not_to_be_visible()
