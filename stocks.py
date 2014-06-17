import urllib.request, sched, time, datetime, re
from pylab import *
s=sched.scheduler(time.time,time.sleep)
count=0
x=[]
y=[]
def timestock(sc):
    global count
    global x
    global y
    i=0
    symbolfile=open("symbols.txt")
    symbolslist=symbolfile.read()
    newsymbolslist=symbolslist.split("\n")
    while i<len(newsymbolslist):
        n=0
        url="http://finance.yahoo.com/q?s=" +newsymbolslist[i] +"&ql=1"
        htmlfile=urllib.request.urlopen(url)
        htmltext=htmlfile.read().decode("utf-8")
        regex=r"[-+]?\d*\.\d+|\d+"
        pattern=re.compile(regex)
        price=re.findall(regex,htmltext)
        if newsymbolslist[i]=='SPY':
            x.append(count)
            y.append(float(price[500]))
            count+=1
            print(x,y)
            plt.plot(x,y)
        i+=1
    sc.enter(1,1,timestock, (sc,))

s.enter(1,1,timestock,(s,))
s.run()
