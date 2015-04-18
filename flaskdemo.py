from flask import Flask
import multiprocessing
from time import sleep
from sys import exit

def runtext(queue):
    for x in range (10):
        print "Counting %d" %(x)
        try:
            obj=queue.get(True,1)
        except Exception as e:
            obj=None  
            pass
        if obj is not None:
            print "got exit!"
            exit()

def runled(queue):
    while True:
        print "start while"
        runtext(queue)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test/<user>")
def reply(user):
    return "Hello %s!" % user
    image = Image.new('RGB', (32, 16))
    draw = ImageDraw.Draw(image) 
    font=ImageFont.truetype("Ubuntu-R.ttf",14)
    draw.text((0,0),user, font=font)
    image.save("%s.jpg" % (user))

@app.route("/start/")
def reply():
	queue=multiprocessing.Queue()
    p = multiprocessing.Process(target=runled, args=(queue,))
    p.start()
    
@app.route("/stop/")
def reply():
    queue.put('something')
    queue.close()
    queue.join_thread()
    p.join

if __name__ == "__main__":
    app.run(host='0.0.0.0')
