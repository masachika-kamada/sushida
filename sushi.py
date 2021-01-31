import chromedriver_binary  # Adds chromedriver binary to path
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

# OpenGL版の寿司打を開く
target_url = 'http://typingx0.net/sushida/play.html?soundless'
driver.get(target_url)

target_xpath = '//*[@id="game"]/div'
webgl_element = driver.find_element_by_xpath(target_xpath)

# クリックする前にロード時間待機
sleep(5)

# スタートボタンの座標
center_x = 250
start_y = 250
mode_y = 300

# スタートボタンをクリックする
actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, start_y).click().perform()

print("スタートボタンをクリックしました。")

# ボタンが表示されるまで待つ
sleep(1)

# お勧めコースをクリックする
actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, mode_y).click().perform()

print("お勧めコースのボタンをクリックしました。")

# <body>に向かってキーを入力させる
target_xpath = '/html/body'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

sleep(2)

text_temp = ""
mis_no = 1
cycle_time = 5.3
ans_no = 0

start = time()

sleep(30)
# while time() - start < 445.0:
while ans_no < 335:
    fname = "sample_image.png"
    # スクショをする
    driver.save_screenshot(fname)

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
    text = tool.image_to_string(im, lang='eng', builder=pyocr.builders.TextBuilder())

    # text を確認
    print(text)

    if text.islower():
        if text.find(")") == -1:
            if text_temp != text:
                # 空白なくす
                text = text.replace(" ", "")
                if text == 'initouroku':
                    text = 'okiniirinitouroku'
                    Image.open(fname).crop((200, 228 + 128, 550, 256 + 128)).save('iniM.png')

                if ans_no % 20 == 0:
                    print(ans_no)

                # 文字を入力させる
                element.send_keys(text)
                ans_no = ans_no + 1
                sleep(0.7)

            else:
                print("M")
                im.save('mistakes/pic_%02d.png' % mis_no)
                mis_no = mis_no + 1
                sleep(cycle_time)

        else:
            print("S")
            im.save('mistakes/pic_%02d.png' % mis_no)
            mis_no = mis_no + 1
            sleep(cycle_time)

        text_temp = text

    else:
        print("X")
        im.save('mistakes/pic_%02d.png' % mis_no)
        mis_no = mis_no + 1
        sleep(cycle_time)

    # element.send_keys('bfgjklmnprdtshuvwyzaiueo?!-,')

input("何か入力してください")
print(time() - start)
# ドライバーを閉じる
driver.quit()

'''
正解数が340を超えるとバグる
時間がたちすぎてもバグるっぽい
440秒当たりが怪しい
420秒でもエラーが出た
エラー文が発見されたときに時間を止めてくれるやつを作ったほうがいい
プラス３秒が来ないように意図的に間違うようにプログラムを改変したらいいかも
'''
