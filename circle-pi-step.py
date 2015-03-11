from PIL import Image, ImageDraw
from math import sin, cos,tan, radians
from time import sleep
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(16, 1)
image = Image.new('1', (32, 16))
draw = ImageDraw.Draw(image)

r0=8

minlist=[]
matrix.Clear()
def calcpoint(radius,angle):
	angle=radians(angle)	
	point=[radius*cos(angle)+16,radius*sin(angle)+8]
	return point

a0=0
while a0<361:
	print "Angle is %d" % (a0)	
	minlist.append(calcpoint(r0,a0))
	a0=a0+6


for p1 in minlist:
	print "x=%d, y=%d" % (p1[0], p1[1])
	#draw.point((p1['x'],p1['y']),fill="rgb(255,0,0)")
	draw.point((p1[0],p1[1]),fill="rgb(255,0,0)")
	#draw.line((origin[0],origin[1],p1[0],p1[1]),fill="rgb(255,0,0)")
	matrix.SetImage(image.im.id,0,0)
	sleep(1)

sleep (10)


matrix.Clear()

