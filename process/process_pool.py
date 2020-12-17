"""
进程池
"""
from multiprocessing import Pool
import time

def func(msg):
    print('开始执行工作%s' % msg)
    time.sleep(1)
    return msg


def apply_async():
    """
    异步使用
    :return:
    """
    pool = Pool(processes=4)
    results = []
    for i in range(10):
        result = pool.apply_async(func=func, args=(i,))
        results.append(result)
    print('不阻塞')
    '''
    在这里干点其他事情
    '''

    for result in results:
        result.wait() # 让result所在进程先执行
    for result in results:
        if result.ready(): # 进程执行完毕
            if result.successful(): # 进程执行成功
                print(result.get())
    print('全部执行完毕')

def map_async():
    """
    异步使用
    :return:
    """
    pool = Pool(processes=4)
    args = list(range(10))
    results = pool.map_async(func=func, iterable=args)
    print('不阻塞')
    '''
    在这里干点其他事情
    '''
    results.wait() # 阻塞等待进程池执行完毕
    if results.ready(): # 进程执行完毕
        if results.successful(): # 进程执行成功
            print(results.get())
    print('全部执行完毕')

def apply_sync():
    """
    同步使用
    :return:
    """
    pool = Pool(processes=4)
    results = []
    for i in range(10):
        # 在这里已经阻塞了，前一句进程执行完后才能进入for循环，所以速度和单进程没有区别
        result = pool.apply(func=func, args=(i,))
        results.append(result)
    print('阻塞')
    pool.close()
    # 进程池里的进程
    # pool.join() # join()语句要放在close()语句后面。
    print(results)
    print('全部执行完毕')

def map_sync():
    """
    异步使用
    :return:
    """
    pool = Pool(processes=4)
    args = list(range(10))
    results = pool.map(func=func, iterable=args)
    print('阻塞')
    print(results)
    print('全部执行完毕')


# apply_async()
# apply_sync()
# map_async()
map_sync()
