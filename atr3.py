import chromedriver_binary
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pyocr
import pyocr.builders
from time import time

tool = pyocr.get_available_tools()[0]

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

print("Start")

sleep(1)

actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, mode_y).click().perform()

print("Choose the course")

target_xpath = '/html/body'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

sleep(2)

start = time()

text_temp = ""

while time() - start < 400.0:
    fname = "sample_image.png"
    driver.save_screenshot(fname)
    im = Image.open(fname).crop((200, 228 + 128, 550, 256 + 128))
    text = tool.image_to_string(im, lang='eng', builder=pyocr.builders.TextBuilder())

    if text.islower():
        if text.find(")") == -1 or text.find("]") == -1:
            if text_temp != text:
                text = text.replace(" ", "")

                element.send_keys(text)
                print(text)

input("input something")
driver.quit()
