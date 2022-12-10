import threading

from time import sleep

from datetime import datetime


def get_date(date: datetime, value: int):

    for _ in range(value):
        thr_name = threading.current_thread().name
        print(f"{thr_name} -- {date}")
        sleep(1)

thread_list: list = []

for i in range(3):
    thr = threading.Thread(target=get_date, args=(str(datetime.now()), i), name=f"thr-{i}")
    thread_list.append(thr)
    thr.start()


for i in thread_list:
    i.join()


