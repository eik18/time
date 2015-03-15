from time import sleep
from PIL import Image, ImageDraw
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(16, 1)
image = Image.new('RGB', (32, 16))
draw = ImageDraw.Draw(image)
 
draw.rectangle((7,0, 23,14), outline=128)
draw.point((15,7),fill='rgb(0,0,255)')


matrix.Clear()
matrix.SetImage(image.im.id,0,0)
sleep(10)
matrix.Clear()
