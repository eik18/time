
from PIL import Image, ImageDraw
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(16, 1)
image = Image.new('1', (32, 16))
draw = ImageDraw.Draw(image)
 
draw.ellipse((0,0, 8,8), fill=128)

matrix.Clear()
matrix.SetImage(image.im.id,0,0)