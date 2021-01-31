from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
# import pyocr
import pyocr.builders
import chromedriver_binary  # Adds chromedriver binary to path

driver = webdriver.Chrome()

# ウィンドウサイズを固定
# +123としているのは
# 「Chromeは自動テストソフトウェアによって制御されています。」
# という部分を考慮している
window = (500, 420+123)
driver.set_window_size(*window)

# OpenGL版の寿司打を開く
target_url = 'http://typingx0.net/sushida/play.html?soundless'
driver.get(target_url)

# 寿司打のゲーム画面をずらすために書く
target_xpath = '//*[@id="game"]/div'
webgl_element = driver.find_element_by_xpath(target_xpath)

# クリックする前にロード時間待機
sleep(10)

# スタートボタンの座標
center_x = 250
center_y = 256

# スタートボタンをクリックする
actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, center_y).click().perform()

print("スタートボタンをクリックしました。")

# ボタンが表示されるまで待つ
sleep(2)

# お勧めコースをクリックする
actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, center_y).click().perform()

print("お勧めコースのボタンをクリックしました。")

# <body>に向かってキーを入力させる
target_xpath = '/html/body'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

# PyOCRのツール
tool = pyocr.get_available_tools()[0]

from time import time
start = time()
while time() - start < 90.0:

    # 移動した
    # ファイル名
    fname = "sample_image.png"
    # スクショをする
    driver.save_screenshot(fname)

    # 画像をPILのImageを使って読み込む
    # ローマ字の部分を取り出す
    im = Image.open(fname).crop((0,230,500,254))

    # tool で文字を認識させる
    text = tool.image_to_string(im, lang='eng', builder=pyocr.builders.TextBuilder())

    # text を確認
    print(text)

    # 文字を入力させる
    element.send_keys(text)

input("何か入力してください")

# ドライバーを閉じる
driver.close()
driver.quit()
