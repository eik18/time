from PIL import Image, ImageDraw
from math import sin, cos,tan, radians
from time import sleep
from datetime import datetime
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(16, 1)
image = Image.new('1', (32, 16))
draw = ImageDraw.Draw(image)

r0=7
originx=16
originy=8
origin=[originx,originy]
minlist=[]
hourlist=[]
count=0
hrradius=4
minradius=6
def calcpoint(radius,angle):
	angle=radians(angle)	
	point=[radius*cos(angle),radius*sin(angle)]
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


matrix.Clear()
matrix.SetImage(image.im.id,0,0)


