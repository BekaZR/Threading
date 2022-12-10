import threading

from time import sleep

from datetime import datetime


def get_date(date: datetime):

    for _ in range(5):
        thr_name = threading.current_thread().name
        print(f"{thr_name} -- {date}")
        sleep(1)


thr = threading.Thread(target=get_date, args=(str(datetime.now()), ), name=f"thr-1", daemon=True)
thr.start()

print("finish")

