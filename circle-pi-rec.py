from PIL import Image, ImageDraw
from math import sin, cos,tan, radians
from time import sleep
from rgbmatrix import Adafruit_RGBmatrix
from datetime import datetime

matrix = Adafruit_RGBmatrix(16, 1)
image = Image.new('RGB', (32, 16))
draw = ImageDraw.Draw(image)

r0=8
originx=15
originy=7
origin=[originx,originy]
hourlist=[]
minradius=6
minlist=[]
matrix.Clear()
def calcpoint(radius,angle):
	angle=radians(angle)	
	point=[radius*cos(angle)+16,radius*sin(angle)+8]
	return point
def calchour(chour):
	if chour>12:
		chour=chour-12
	return chour
a0=6
while a0<359:
	print "Angle is %d" % (a0)	
	minlist.append(calcpoint(r0,a0))
	a0=a0+6
a0=30
while a0<359:
	        #print "Angle is %d" % (a0)
	        hourlist.append(calcpoint(r0,a0))
	        a0=a0+30

#for p1 in minlist:
#	print "x=%d, y=%d" % (p1[0], p1[1])
	#draw.point((p1['x'],p1['y']),fill="rgb(255,0,0)")
#	draw.point((p1[0],p1[1]),fill="rgb(255,0,0)")
	#draw.line((origin[0],origin[1],p1[0],p1[1]),fill="rgb(255,0,0)"

#for p1 in hourlist:
#	print "x=%d, y=%d" % (p1[0], p1[1])
	#draw.point((p1['x'],p1['y']),fill="rgb(255,0,0)")
#	draw.point((p1[0],p1[1]),fill="rgb(0,0,255)")
	#draw.line((origin[0],origin[1],p1[0],p1[1]),fill="rgb(255,0,0)"

now=datetime.now()

min0=calcpoint(minradius,6*now.minute-90)
draw.line((originx,originy,min0[0],min0[1]),fill="rgb(255,0,0)")

draw.point((origin),fill="rgb(0,0,255)")
draw.rectangle((7,0, 23,14), outline=128)
#draw.point((15,7),fill='rgb(0,0,255)')



matrix.SetImage(image.im.id,0,0)
sleep (10)
matrix.Clear()

