from behave import *
from pages.home_page import HomePage

homePage = HomePage()


@given(u'esta na pagina home do site')
def step_impl(context):
    homePage.access_page('https://www.meubilhete.com/')
    homePage.capture_home_page()


@when(u'seleciona botao Login')
def step_impl(context):
    homePage.click_button_login()


@then(u'o site redireciona para pagina de login')
def step_impl(context):
    if not homePage.check_url('https://www.meubilhete.com/login'):
        raise Exception("url incorreta")
