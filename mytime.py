from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from time import sleep
now = datetime.now()
print now.hour
print now.minute

im = Image.new('RGBA', (320, 320), (0, 0, 0, 0)) 
draw = ImageDraw.Draw(im) 
font = ImageFont.load("arial.pil")
draw.text((20,200), "test", fill="rgb(255,0,0), font=font")
im.show()