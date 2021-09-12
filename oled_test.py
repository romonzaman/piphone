import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

def oled_white():
    oled.fill(250)
    oled.show()

def oled_black():
    oled.fill(0)
    oled.show()

oled_black()
oled_white()
time.sleep(2)
oled_black()
time.sleep(1)

oled_white()
time.sleep(2)
oled_black()
time.sleep(1)

oled_white()
time.sleep(2)
oled_black()
time.sleep(1)

oled_white()
time.sleep(2)
oled_black()
time.sleep(1)

oled_white()
