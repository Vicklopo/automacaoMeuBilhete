from browser import Browser
from utility.BasePage import BasePage


class HomePageLocator(object):
    # Seletores dos elementos utilizados na página
    BUTTON_LOGIN = '[class="btn orangeBtn"]'


class HomePage(Browser):

    def __init__(self):
        self.b = BasePage(self.driver)

    def access_page(self, url):
        self.b.navigate(url)

    def click_button_login(self):
        self.b.set_locator(HomePageLocator.BUTTON_LOGIN).click()

    def check_url(self, url):
        return self.b.check_url(url)

    def capture_home_page(self):
        self.b.screen_shot('home_page')


