from PIL import Image, ImageDraw
from math import sin, cos,tan, radians
from time import sleep
from datetime import datetime
#im = Image.new('RGBA', (320, 320), (0, 0, 0, 0)) 
#draw = ImageDraw.Draw(im) 
r0=100
origin=[160,160]
minlist=[]
hourlist=[]
count=0
def calcpoint(radius,angle):
	angle=radians(angle)	
	point=[radius*cos(angle)+160,radius*sin(angle)+160]
	return point
def calchour(chour):
	if chour>12:
		chour=chour-12
	return chour
while count<2:
	im = Image.new('RGBA', (320, 320), (0, 0, 0, 0)) 
	draw = ImageDraw.Draw(im) 
	a0=0
	while a0<361:
		#print "Angle is %d" % (a0)	
		minlist.append(calcpoint(r0,a0))
		a0=a0+6
	a0=0
	while a0<361:
	        #print "Angle is %d" % (a0)
	        hourlist.append(calcpoint(r0,a0))
	        a0=a0+30

	for p1 in minlist:
		print "x=%d, y=%d" % (p1[0], p1[1])
		#draw.point((p1['x'],p1['y']),fill="rgb(255,0,0)")
		draw.point((p1[0],p1[1]),fill="rgb(255,0,0)")
		#draw.line((origin[0],origin[1],p1[0],p1[1]),fill="rgb(255,0,0)")

	for p1 in hourlist:
	        print "x=%d, y=%d" % (p1[0], p1[1])
	        draw.point((p1[0],p1[1]),fill="rgb(0,255,0)")

	now=datetime.now()

	hr0=calcpoint(70,30*calchour(now.hour)-90)
	draw.line((origin[0],origin[1],hr0[0],hr0[1]),fill="rgb(255,0,0)")
	min0=calcpoint(90,6*now.minute-90)
	draw.line((origin[0],origin[1],min0[0],min0[1]),fill="rgb(255,0,0)")
	#print "x=%d, y=%d" % (p1['x'], p1['y'])
	#draw.point((p1['x']+200,p1['y']+200),fill="rgb(255,0,0)")
	draw.point((origin),fill="rgb(0,0,255)")
	im.show()
	break	
	#sleep(60)
	count=count+1

