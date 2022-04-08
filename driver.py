import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv



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
        mis_no = 1
        cycle_time = 5.3
        ans_no = 0

        time.sleep(32)
        while ans_no < 320:
            fname = "sample_image.png"
            # スクショをする
            self.driver.save_screenshot(fname)

            # 画像をPILのImageを使って読み込む
            # ローマ字の部分を取り出す
            im = Image.open(fname).crop((200, 228 + 128, 550, 256 + 128))

            # モノクロへ変換
            im = im.convert("L")
            for i in range(im.size[0]):
                for j in range(im.size[1]):
                    if im.getpixel((i, j)) >= 128:
                        im.putpixel((i, j), 0)
                    else:
                        im.putpixel((i, j), 255)

            # tool で文字を認識させる
            text = self.tool.image_to_string(
                im, lang='eng', builder=pyocr.builders.TextBuilder())

            # text を確認
            print(text)

            if text.islower():
                if text.find(")") == -1:
                    if text_temp != text:
                        # 空白なくす
                        text = text.replace(" ", "")
                        if text == 'initouroku':
                            text = 'okiniirinitouroku'
                            Image.open(fname).crop(
                                (200, 228 + 128, 550, 256 + 128)).save('iniM.png')

                        if ans_no % 20 == 0:
                            print(ans_no)

                        # 文字を入力させる
                        element.send_keys(text)
                        ans_no = ans_no + 1
                        time.sleep(0.7)

                    else:
                        print("M")
                        im.save('mistakes/pic_%02d.png' % mis_no)
                        mis_no = mis_no + 1
                        time.sleep(cycle_time)

                else:
                    print("S")
                    im.save('mistakes/pic_%02d.png' % mis_no)
                    mis_no = mis_no + 1
                    time.sleep(cycle_time)

                text_temp = text

            else:
                print("X")
                im.save('mistakes/pic_%02d.png' % mis_no)
                mis_no = mis_no + 1
                time.sleep(cycle_time)

        input("何か入力してください")
        self.driver.quit()

    def send_key(self, xpath, key):
        self.driver.find_element_by_xpath(xpath).send_keys(key)
