import threading

from time import sleep

from datetime import datetime


def get_date(date):
    while True:
        thr_name = threading.current_thread().name
        print(f"{thr_name} -- {date}")
        sleep(2)

thr = threading.Thread(target=get_date, args=(str(datetime.now()),), name="thr-1").start()


for i in range(10):
    print(i)
    sleep(2)
