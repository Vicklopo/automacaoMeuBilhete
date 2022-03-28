from behave import *
from pages.cadastro_page import CadastroPage
from pages.home_page import HomePage

homePage = HomePage()
cadastroPage = CadastroPage()


@when(u'seleciona botao "Criar conta"')
def step_impl(context):
    cadastroPage.click_button_create_account()


@when(u'o site redireciona para pagina de cadastro')
def step_impl(context):
    if not cadastroPage.check_url('https://www.meubilhete.com/signup'):
        raise Exception("url incorreta")


@when(u'preenche o campo "nome completo" com "{nome_completo}"')
def step_impl(context, nome_completo):
    cadastroPage.send_keys_input_name(nome_completo)


@when(u'preenche o campo "cpf" com "{cpf}"')
def step_impl(context, cpf):
    cadastroPage.send_keys_input_cpf(cpf)


@when(u'preenche o campo "whatsapp" com "{whatsapp}"')
def step_impl(context, whatsapp):
    cadastroPage.send_keys_input_whatsapp(whatsapp)


@when(u'seleciona botao "PROSSEGUIR"')
def step_impl(context):
    cadastroPage.capture_register_first()
    cadastroPage.click_button_proceed()


@when(u'preenche o campo "confirmar senha" com "{confirmar_senha}"')
def step_impl(context, confirmar_senha):
    cadastroPage.send_keys_input_repeat_password(confirmar_senha)


@when(u'seleciona "{sexo}" no select "sexo"')
def step_impl(context, sexo):
    cadastroPage.click_select_sexo(sexo)


@when(u'preenche o campo "data de nascimento" com "{data_nascimento}"')
def step_impl(context, data_nascimento):
    cadastroPage.send_keys_input_data_nascimento(data_nascimento)
    cadastroPage.capture_register_second()


@when(u'preenche o campo "cep" com "{cep}"')
def step_impl(context, cep):
    cadastroPage.send_keys_input_cep(cep)


@when(u'preenche o campo "numero" com "{numero}"')
def step_impl(context, numero):
    cadastroPage.send_keys_input_numero(numero)


@when(u'aceita os termos de uso selecionando o botao "checkbox"')
def step_impl(context):
    cadastroPage.click_button_checkbox()


@when(u'seleciona botao "CADASTRAR"')
def step_impl(context):
    cadastroPage.capture_register_third()
    cadastroPage.click_button_cadastrar()


@then(u'o cadastro e realizado com sucesso')
def step_impl(context):
    if not cadastroPage.check_url('https://www.meubilhete.com/'):
        raise Exception("url incorreta")
    cadastroPage.capture_register_success()
