import threading

from time import sleep

from datetime import datetime

locker = threading.Lock()


value = 0

def inc_value():
    global value
    while True:
        locker.acquire()
        value += 1
        print(value)
        sleep(1)
        locker.release()
        


for _ in range(5):
    threading.Thread(target=inc_value).start()
