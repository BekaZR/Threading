import threading

data = threading.local()


def get_data():
    thread_name = threading.current_thread().name
    print(thread_name, data.value)
    


def set_value_data_in_thread_1():
    data.value = 111
    get_data()


def set_value_data_in_thread_2():
    data.value = 222
    get_data()


threading.Thread(target=set_value_data_in_thread_1).start()
threading.Thread(target=set_value_data_in_thread_2).start()
