from browser import Browser
from utility.BasePage import BasePage


class LoginPageLocator(object):
    # Seletores dos elementos utilizados na página
    INPUT_EMAIL = '[formcontrolname="email"]'
    INPUT_SENHA = '[formcontrolname="password"]'
    BUTTON_ENTRAR = '[class="btn lgYellowBtn mt-n2"]'


class LoginPage(Browser):

    def __init__(self):
        self.b = BasePage(self.driver)

    def send_keys_input_email(self, email):
        self.b.set_locator(LoginPageLocator.INPUT_EMAIL).send_keys(email)

    def send_keys_input_password(self, senha):
        self.b.set_locator(LoginPageLocator.INPUT_SENHA).send_keys(senha)

    def click_button_entrar(self):
        self.b.wait_seconds(2)
        self.b.screen_shot('login')
        self.b.set_locator(LoginPageLocator.BUTTON_ENTRAR).click()

    def check_url(self, url):
        return self.b.check_url(url)

    def capture_logged(self):
        self.b.screen_shot('logged')
