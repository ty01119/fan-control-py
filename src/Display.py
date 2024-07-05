import board
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

class Display:
  # init display
  def __init__(self):
    self.WIDTH = 128
    self.HEIGHT = 64  
    self.BORDER = 5
    i2c = board.I2C()
    self.oled = adafruit_ssd1306.SSD1306_I2C(self.WIDTH, self.HEIGHT, i2c, addr=0x3C)

  def clear(self, keepBorder=False):
    self.oled.fill(0)

    if keepBorder:
      self.drawBasic()

    self.oled.show()

  def drawBasic(self):
    self.image = Image.new("1", (self.oled.width, self.oled.height))
    # Get drawing object to draw on image.
    self.draw = ImageDraw.Draw(self.image)

    # Draw a white background
    self.draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=255)

    # Draw a smaller inner rectangle
    self.draw.rectangle(
        (self.BORDER, self.BORDER, self.oled.width - self.BORDER - 1, self.oled.height - self.BORDER - 1),
        outline=0,
        fill=0,
    )


  
  def drawText(self, line1 = '', line2 = '', line3 = ''):
    self.clear(keepBorder=True)
    # Load default font.
    font = ImageFont.load_default()
    # Draw Some Text
    bbox = font.getbbox(line1)
    (font_width_line_1, font_height_line_1) = bbox[2] - bbox[0], bbox[3] - bbox[1]
    bbox = font.getbbox(line2)
    (font_width_line_2, font_height_line_2) = bbox[2] - bbox[0], bbox[3] - bbox[1]
    bbox = font.getbbox(line3)
    (font_width_line_3, font_height_line_3) = bbox[2] - bbox[0], bbox[3] - bbox[1]
    # draw line 1
    self.draw.text(
      (self.oled.width // 2 - font_width_line_1 // 2, self.oled.height // 4 - font_height_line_1 // 2),
      line1,
      font=font,
      fill=255,
    )
    self.draw.text(
      (self.oled.width // 2 - font_width_line_2 // 2, self.oled.height // 2 - font_height_line_2 // 2),
      line2,
      font=font,
      fill=255,
    )
    self.draw.text(
      (self.oled.width // 2 - font_width_line_3 // 2, self.oled.height - self.oled.height // 4 - font_height_line_3 // 2),
      line3,
      font=font,
      fill=255,
    )

  def show(self):
    self.oled.image(self.image)
    self.oled.show()
