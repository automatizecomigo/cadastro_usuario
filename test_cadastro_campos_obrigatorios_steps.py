import random
import string
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/cadastro_campos_obrigatorios.feature')


def gerar_email_aleatorio():
    # Gerar a parte local do email
    nome = ''.join(random.choices(string.ascii_lowercase, k=5))
    sobrenome = ''.join(random.choices(string.ascii_lowercase, k=5))

    # Gerar o domínio
    dominio = ''.join(random.choices(string.ascii_lowercase, k=5)) + ".com"

    # Combinar partes do email
    email = f"{nome}.{sobrenome}@{dominio}"
    return email


@given('que estou na página Goden Movie Studio')
def pagina_golden_movie_studio(browser: Page):
    browser.goto('http://127.0.0.1:8080/')


@when("faco o preechimento dos campos obrigatórios")
def preencher_campos_obrigatorios(browser: Page):
    email_aleatorio = gerar_email_aleatorio()
    browser.locator('[placeholder="Nome...*"]').fill('Rafael')
    browser.locator('[placeholder="Sobrenome...*"]').fill('Pantoja')
    browser.locator('[placeholder="Email...*"]').fill(email_aleatorio)
    browser.locator('[placeholder="Telefone..."]').fill('91983074577')
    browser.locator('[placeholder="Senha...*"]').fill('@Panquecaria20246')
    browser.get_by_text('Cadastrar', exact=True).click()


@then("valido se o usuario foi cadastra com sucesso")
def validacao_de_cadastro_de_usuario(browser: Page):
    expect(browser.get_by_text('Cadastro realizado com sucesso!')).to_be_visible()


@when("faco o preechimento dos campos obrigatórios com nome invalido")
def preencho_com_dados_invalidos(browser: Page):
    email_aleatorio = gerar_email_aleatorio()
    browser.locator('[placeholder="Nome...*"]').fill('Rafael22')
    browser.locator('[placeholder="Sobrenome...*"]').fill('Pantoja')
    browser.locator('[placeholder="Email...*"]').fill(email_aleatorio)
    browser.locator('[placeholder="Telefone..."]').fill('91983074577')
    browser.locator('[placeholder="Senha...*"]').fill('@Panquecaria20246')
    browser.get_by_text('Cadastrar', exact=True).click()


@then("valido que o nome nao e aceito")
def valid_que_nome_nao_vai_ser_aceito(browser: Page):
    expect(browser.locator('text=Nome deve conter apenas caracteres alfabéticos')).to_be_visible()



