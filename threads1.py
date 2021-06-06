from threading import *
from time import *

class App1(Thread):
    def my_function(self, name):

        for i in range(5):
            print("thread "+ str(name))
            sleep(1)

app1 = App1()

t1 = Thread(target=app1.my_function, args=("alpha",))
t1.start()

t2 = Thread(target=app1.my_function, args=("beta",))
t2.start()


class App2(Thread):
    def run(self):
        for i in range(5):
            print("thread 2")
            sleep(1)

class App3(Thread):
    def run(self):
        for i in range(5):
            print("thread 3")
            sleep(1)

app1 = App1()
app2 = App2()
app3 = App3()


app1.start()
app2.start()
app3.start()

app1.join()
app2.join()
app3.join()

#this will be printed after the three child threads
print("\nhello")