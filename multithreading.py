from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)


class hi(Thread):
    def run(self):
        for i in range(5):
         print("hi")
         sleep(1)

h1=hello()
h2=hi()

h1.start()
sleep(0.2)
h2.start()
h1.join()
h2.join()
print("bye")