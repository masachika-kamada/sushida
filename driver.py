import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
from ocr import ocr


class ChromeDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(744, 744)
        self.actions = ActionChains(self.driver)
        data = {}
        file = open("./data.csv", 'r', encoding="UTF-8")
        for row in csv.reader(file):
            if " " in row[1]:  # 座標データ
                data[row[0]] = list(map(int, row[1].split()))
            else:
                data[row[0]] = row[1]
        file.close()
        self.data = data

    def access_sushida(self):
        self.driver.get(self.data["url"])
        time.sleep(5)
        element = self.driver.find_element_by_xpath(self.data["menu_xpath"])
        self.actions.move_to_element_with_offset(
            element, self.data["start"][0], self.data["start"][1]).click().perform()
        print("スタートボタンをクリックしました。")
        time.sleep(1)
        self.actions.move_to_element_with_offset(
            element, self.data["mode_choice"][0], self.data["mode_choice"][1]).click().perform()
        print("お勧めコースのボタンをクリックしました。")

    def play_game(self):
        element = self.driver.find_element_by_xpath(self.data["play_xpath"])
        element.send_keys(" ")

        text_temp = ""
        n_failure = 0
        n_ans = 0

        time.sleep(32)
        while n_ans < 320:
            fname = "suhida.jpg"
            self.driver.save_screenshot(fname)
            res, text = ocr(fname, text_temp, n_failure, self.data["bbox"])

            if not res:
                time.sleep(self.data["cycle_time"])
                continue

            element.send_keys(text)
            n_ans += 1
            time.sleep(0.7)
            text_temp = text

            if n_ans % 20 == 0:
                print(n_ans)

        input("何か入力してください")
        self.driver.quit()
