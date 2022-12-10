import threading

from time import sleep


def test():
    while True:
        print("test")
        sleep(1)


threading.Timer(10, test).start()


while True:
    print(1)
    sleep(2)