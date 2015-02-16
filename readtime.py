from datetime import datetime
from time import sleep
tod=0
hr1=0

mindic ={0:"o'clock", 1:'oh-one', 2:'oh-two', 3:'oh-three', 4:'oh-four', 5:'oh-five', 6:'oh-six', 7:'oh-seven', 8:'oh-eight', 9:'oh-nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 21:'twenty-one', 22:'twenty-two', 23:'twenty-three', 24:'twenty-four', 25:'twenty-five', 26:'twenty-six', 27:'twenty-seven', 28:'twenty-eight', 29:'twenty-nine', 30:'thirty', 31:'thirty-one', 32:'thirty-two', 33:'thirty-three', 34:'thirty-four', 35:'thirty-five', 36:'thirty-six', 37:'thirty-seven', 38:'thirty-eight', 39:'thirty-nine', 40:'fourty', 41:'fourty-one', 42:'fourty-two', 43:'fourty-three', 44:'fourty-four', 45:'fourty-five', 46:'fourty-six', 47:'fourty-seven', 48:'fourty-eight', 49:'fourty-nine', 50:'fifty', 51:'fifty-one', 52:'fifty-two', 53:'fifty-three', 54:'fifty-four', 55:'fifty-five', 56:'fifty-six', 57:'fifty-seven', 58:'fifty-eight', 59:'fifty-nine'}

hrdic ={1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve'}

now=datetime.now()

hr0=now.hour
min0=now.minute

if hr0 >12:
	hr1=hr0-12
else:
	hr1=hr0

if hr0<1:
	hr1=12

if hr0 > 11 and hr0<18:
	tod='in the afternoon'
elif hr0>18:
	tod='in the evening'
elif hr0<12:
	tod='in the morning'


print "It is %s %s %s" % (hrdic[hr1],mindic[min0],tod)


