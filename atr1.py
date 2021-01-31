import chromedriver_binary
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import time

driver = webdriver.Chrome()

window = (744, 744)
driver.set_window_size(*window)

target_url = 'http://typingx0.net/sushida/play.html?soundless'
driver.get(target_url)

target_xpath = '//*[@id="game"]/div'
webgl_element = driver.find_element_by_xpath(target_xpath)

sleep(5)

center_x = 250
start_y = 250
mode_y = 300

actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, start_y).click().perform()

sleep(1)

actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, mode_y).click().perform()

target_xpath = '/html/body'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

sleep(2)

start = time()

while time() - start < 123.0:

    element.send_keys('bfgjklmnprdtshuvwyzaiueo?!-,')

input("input any keys")
driver.quit()
