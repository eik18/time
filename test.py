from time import sleep
from PIL import Image, ImageDraw
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(16, 1)
image = Image.new('RGB', (32, 16))
draw = ImageDraw.Draw(image)
 
draw.ellipse((5,5, 16,16), outline=128)



matrix.Clear()
matrix.SetImage(image.im.id,0,0)
sleep(10)
matrix.Clear()
