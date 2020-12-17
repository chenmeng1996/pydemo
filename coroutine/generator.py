import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            print('没有传数据')
            r = '500 ERROR'
        else:
            print('消费 %s' % n)
            time.sleep(1)
            r = '200 OK'

def producer(c):
    # 第一次执行，返回的r是''
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('生产 %s' % n)
        r = c.send(n)
        print('消费者返回 %s' % r)
    r = c.send(None)
    print('消费者返回 %s' % r)
    r = c.send(10)
    print('消费者返回 %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    producer(c)
