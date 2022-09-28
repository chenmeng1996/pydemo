def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print("[CONSUMER] Consuming {0}...".format(n))
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("[PRODUCER] Producing {0}...".format(n))
        r = c.send(n)
        print("[PRODUCER] Consumer return: {0}".format(r))
    c.close()

c = consumer()
produce(c)