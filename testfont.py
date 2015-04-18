from PIL import Image, ImageDraw, ImageFont
from time import sleep
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(16, 1)
image = Image.new('RGB', (32, 16))
draw = ImageDraw.Draw(image)
font=ImageFont.truetype("Ubuntu-R.ttf",14)
draw.text((0,0),"Test", font=font)
matrix.SetImage(image.im.id,0,0)
sleep (2)
matrix.Clear()
image = Image.new('RGB', (32, 16))
draw.text((0,0),"Eric", font=font)
matrix.SetImage(image.im.id,0,0)



sleep (22)
matrix.Clear()
