from browser import Browser
from datetime import datetime


# executa os comandos antes de todos os testes iniciarem
def before_all(context):
    context.browser = Browser()


def after_feature(context, feature):
    context.browser.browser_clear()


def after_all(context):
    context.browser.browser_quit()
