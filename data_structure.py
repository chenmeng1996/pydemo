# 队列
def queue():
    from queue import Queue
    q = Queue()
    q.put(1)
    q.put(2)
    print(q.queue)
    first = q.get(False)
    print(first)
    print(q.queue)

if __name__ == "__main__":
    queue()