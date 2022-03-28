from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser(object):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path=r'D:\pythonProject\drivers\chromedriver.exe', chrome_options=options)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def browser_quit(self):
        self.driver.quit()

    def browser_clear(self):
        self.driver.delete_all_cookies()
    #    self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.get('https://www.meubilhete.com/')
