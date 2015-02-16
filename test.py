from PIL import Image, ImageDraw
im = Image.new('RGBA', (400, 400), (0, 0, 0, 0)) 
draw = ImageDraw.Draw(im) 
draw.ellipse((0,0, 150,300), fill=128)
im.show()
