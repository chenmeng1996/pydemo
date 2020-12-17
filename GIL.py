import datetime

def calc():
    sum = 0
    import time
    # 加入IO操作，多线程就发挥出优势
    # time.sleep(0.5)
    for _ in range(10000000):
        sum = sum + 1

def single_thread():
    start = datetime.datetime.now()
    for _ in range(4):
        calc()
    duration = (datetime.datetime.now() - start).total_seconds()
    print(duration)

def multi_thread():
    import threading
    start = datetime.datetime.now()
    for _ in range(4):
        threading.Thread(target=calc).start()
    # 确保主线程最后执行
    for thread in threading.enumerate():
        if thread.name != "MainThread":
            thread.join()
    duration = (datetime.datetime.now() - start).total_seconds()
    print(duration)

def single_process():
    single_thread()

def multi_process():
    start = datetime.datetime.now()
    from multiprocessing import Process
    for _ in range(4):
        Process(target=calc).start()
    duration = (datetime.datetime.now() - start).total_seconds()
    print(duration)


if __name__ == '__main__':
    single_process()