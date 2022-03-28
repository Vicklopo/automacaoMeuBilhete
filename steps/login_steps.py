from behave import *
from pages.login_page import LoginPage

loginPage = LoginPage()


@when(u'seleciona o botao "ENTRAR"')
def step_impl(context):
    loginPage.click_button_entrar()


@then(u'o site redireciona para o dashboard')
def step_impl(context):
    if not loginPage.check_url('https://www.meubilhete.com/'):
        raise Exception("url incorreta")
    loginPage.capture_logged()
