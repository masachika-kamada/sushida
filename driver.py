import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


class chrome_driver:

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(744, 744)
        self.driver.get(self.urls['mypage'])

    def login(self, reverse=False):
        self.click(self.x_paths['login'])
        if reverse:
            self.send_key(self.x_paths['id'], self.idpass['id2'])
            self.send_key(self.x_paths['pass'], self.idpass['pass2'])
        else:
            self.send_key(self.x_paths['id'], self.idpass['id1'])
            self.send_key(self.x_paths['pass'], self.idpass['pass1'])

    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def send_key(self, xpath, key):
        self.driver.find_element_by_xpath(xpath).send_keys(key)
