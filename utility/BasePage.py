from datetime import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class BasePage:
    def __init__(self, driver):
        self.locator = None
        self.driver = driver

    def get_element(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, self.get_locator())))
        return self.driver.find_element(By.CSS_SELECTOR, self.get_locator())

    def click(self):
        self.get_element().click()
        return self

    def navigate(self, url):
        self.driver.get(url)

    def compare_url(self, url):
        self.wait_seconds(3)
        print(self.driver.current_url)
        print(url)
        return self.driver.current_url == url

    def set_locator(self, locator):
        self.locator = locator
        return self

    def get_locator(self):
        return self.locator

    def send_keys(self, keys):
        self.get_element().send_keys(keys)
        return self

    def press_enter(self):
        self.wait_seconds(0.50)
        self.get_element().send_keys(Keys.ENTER)
        self.wait_seconds(0.50)
        return self

    def scroll_to(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_element())
        return self

    def wait_seconds(self, seconds):
        time.sleep(seconds)
        return self

    def check_url(self, url):
        return self.compare_url(url)

    def screen_shot(self, name):
        self.driver.get_screenshot_as_file('D:/pythonProject/reports/' +
                                           datetime.today().strftime('%Y-%m-%d') + '_' + name + '.png')
