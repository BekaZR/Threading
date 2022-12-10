import threading

from time import sleep

from datetime import datetime


def get_date(date):
    thr_name = threading.current_thread().name
    print(f"{thr_name} -- {date}")
    sleep(5)

thr = threading.Thread(target=get_date, args=(str(datetime.now()),), name="thr-1").start()

