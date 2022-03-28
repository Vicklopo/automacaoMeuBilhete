from browser import Browser
from utility.BasePage import BasePage


class GenericPageLocator(object):
    INPUT_EMAIL = '[formcontrolname="email"]'
    INPUT_SENHA = '[formcontrolname="password"]'


class GenericPage(Browser):

    def __init__(self):
        self.b = BasePage(self.driver)

    def send_keys_input_email(self, email):
        self.b.set_locator(GenericPageLocator.INPUT_EMAIL).send_keys(email)

    def send_keys_input_password(self, senha):
        self.b.set_locator(GenericPageLocator.INPUT_SENHA).send_keys(senha)

