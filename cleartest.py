from PIL import Image, ImageDraw
from time import sleep
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(16, 1)
image = Image.new('RGB', (32, 16))
draw = ImageDraw.Draw(image)
draw.line((0,0,0,15),fill="rgb(255,0,0)")


for x in range(0,31):
	matrix.Clear()
	image = Image.new('RGB', (32, 16))
	draw = ImageDraw.Draw(image)
	draw.line((x,0,x,15),fill="rgb(255,0,0)")
	#matrix.SetImage(image.im.id,x,0)
	sleep (1)

sleep (5)
matrix.Clear()

