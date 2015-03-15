from PIL import Image, ImageDraw
from math import sin, cos,tan, radians
from time import sleep
from rgbmatrix import Adafruit_RGBmatrix
#from datetime import datetime

matrix = Adafruit_RGBmatrix(16, 1)
image = Image.new('RGB', (32, 16))
draw = ImageDraw.Draw(image)

originx=15
originy=7
origin=[originx,originy]
minradius=6
matrix.Clear()
def calcpoint(radius,angle):
	angle=radians(angle)	
	point=[radius*cos(angle)+16,radius*sin(angle)+8]
	return point


#now=datetime.now()
#nowmin=now.minute

for nowmin in range(0,59):
	matrix.Clear()
	draw.rectangle((7,0, 23,14), outline=128)
	min0=calcpoint(minradius,6*nowmin-90)
	draw.line((originx,originy,min0[0],min0[1]),fill="rgb(255,0,0)")
	draw.point((origin),fill="rgb(0,0,255)")	
	matrix.SetImage(image.im.id,0,0)
	sleep (1)

sleep (5)
matrix.Clear()

