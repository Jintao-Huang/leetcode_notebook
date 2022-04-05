# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class MyHashMap:
    def hash_func(self, k: int):
        return k % self.p

    def __init__(self):
        self.p = 10007
        self.T = [[]] * self.p

    def put(self, key: int, value: int) -> None:
        ll = self.T[self.hash_func(key)]
        for i in range(len(ll)):
            k = ll[i][0]
            if k == key:
                ll[i] = key, value
                return
        ll.append((key, value))

    def get(self, key: int) -> int:
        ll = self.T[self.hash_func(key)]
        for i in range(len(ll)):
            k, v = ll[i]
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        ll = self.T[self.hash_func(key)]
        for i in range(len(ll)):
            k = ll[i][0]
            if k == key:
                ll.pop(i)
                return


from template.build.call_func import call_func

print(call_func(["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
                [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]], globals()))
