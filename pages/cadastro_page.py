from browser import Browser
from utility.BasePage import BasePage


class CadastroPageLocator(object):
    BUTTON_CRIAR_CONTA = '[class="text-info m-l-5"]'
    INPUT_NOME = '[formcontrolname="name"]'
    INPUT_CPF = '[formcontrolname="doc"]'
    INPUT_WHATSAPP = '[formcontrolname="phone"]'
    BUTTON_PROSSEGUIR = '[class="btn lgYellowBtn mt-n2"]'
    INPUT_REPETIR_SENHA = '[formcontrolname="confirmPassword"]'
    SELECT_SEXO = '[formcontrolname="genre"]'
    PESQUISAR_SEXO = '[class="roundedControl"]'
    INPUT_DATA_NASCIMENTO = '[formcontrolname="birthDate"]'
    INPUT_CEP = '[formcontrolname="addressPostalCode"]'
    INPUT_NUMERO = '[formcontrolname="addressNumber"]'
    BUTTON_CHECKBOX = '[class="form-control chkbox ng-untouched ng-pristine ng-valid"]'
    BUTTON_CADASTRAR = '[class="btn lgYellowBtn mt-n2"]'


class CadastroPage(Browser):

    def __init__(self):
        self.b = BasePage(self.driver)

    def access_page(self, url):
        self.b.navigate(url)

    def click_button_create_account(self):
        self.b.set_locator(CadastroPageLocator.BUTTON_CRIAR_CONTA).click()

    def check_url(self, url):
        return self.b.check_url(url)

    def send_keys_input_name(self, nome_completo):
        self.b.set_locator(CadastroPageLocator.INPUT_NOME).send_keys(nome_completo)

    def send_keys_input_cpf(self, cpf):
        self.b.set_locator(CadastroPageLocator.INPUT_CPF).send_keys(cpf)

    def send_keys_input_whatsapp(self, whatsapp):
        self.b.set_locator(CadastroPageLocator.INPUT_WHATSAPP).send_keys(whatsapp)

    def click_button_proceed(self):
        self.b.set_locator(CadastroPageLocator.BUTTON_PROSSEGUIR).click()

    def send_keys_input_repeat_password(self, confirmar_senha):
        self.b.set_locator(CadastroPageLocator.INPUT_REPETIR_SENHA).send_keys(confirmar_senha)

    def click_select_sexo(self, sexo):
        self.b.set_locator(CadastroPageLocator.SELECT_SEXO).click()
        self.b.set_locator(CadastroPageLocator.PESQUISAR_SEXO).send_keys(sexo).press_enter()

    def send_keys_input_data_nascimento(self, data_nascimento):
        self.b.set_locator(CadastroPageLocator.INPUT_DATA_NASCIMENTO).send_keys(data_nascimento)

    def send_keys_input_cep(self, cep):
        self.b.set_locator(CadastroPageLocator.INPUT_CEP).scroll_to().send_keys(cep).press_enter()
        # preciso esperar mais tempo, pois a API de CEP pode demorar
        # ToDo: Poderia validar o valor de algum elemento para ter certeza que foi preenchido
        self.b.wait_seconds(10)

    def send_keys_input_numero(self, numero):
        self.b.set_locator(CadastroPageLocator.INPUT_NUMERO).send_keys(numero)

    def click_button_checkbox(self):
        self.b.set_locator(CadastroPageLocator.BUTTON_CHECKBOX).click()

    def click_button_cadastrar(self):
        self.b.wait_seconds(2)
        self.b.set_locator(CadastroPageLocator.BUTTON_CADASTRAR).click()

    def capture_register_third(self):
        self.b.screen_shot('register_third')

    def capture_register_second(self):
        self.b.screen_shot('register_second')

    def capture_register_first(self):
        self.b.screen_shot('register_first')

    def capture_register_success(self):
        self.b.screen_shot('register_success')
