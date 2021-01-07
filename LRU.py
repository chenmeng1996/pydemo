
class LRU:
    def __init__(self):
        self.l: list = []
        self.m: dict = dict()
        self.n = 5

    def set(self, k, v):
        if k in self.l:
            self.l.remove(k)
            self.l.append(k)
        else:
            if self.n == len(self.l):
                _k = self.l.pop(0)
                del self.m[_k]
            self.l.append(k)
        self.m[k] = v

    def get(self, k):
        return self.m[k]