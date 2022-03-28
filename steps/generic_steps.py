from behave import *
from pages.generic_page import GenericPage

genericPage = GenericPage()


@when(u'preenche o campo "Email" com "{email}"')
def step_impl(context, email):
    genericPage.send_keys_input_email(email)


@when(u'preenche o campo "Senha" com "{senha}"')
def step_impl(context, senha):
    genericPage.send_keys_input_password(senha)
