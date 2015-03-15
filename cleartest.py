from PIL import Image, ImageDraw
from time import sleep
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(16, 1)
image = Image.new('RGB', (32, 16))
draw = ImageDraw.Draw(image)
draw.line((0,0,0,15),fill="rgb(255,0,0)")


x=0
while x<32:
	matrix.Clear()
	#draw.line((x,0,x,15),fill="rgb(255,0,0)")
	matrix.SetImage(image.im.id,x,0)
	sleep (1)
	x=x+1

sleep (5)
matrix.Clear()

