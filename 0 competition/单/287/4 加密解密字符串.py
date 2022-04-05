# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from template.build.call_func import call_func
from collections import defaultdict

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys = keys
        self.values = values
        self.k_to_val = {}
        for i in range(len(keys)):
            k = keys[i]
            val = values[i]
            self.k_to_val[k] = val

        start = defaultdict(int)
        for i in range(len(dictionary)):
            w = dictionary[i]
            start[self.encrypt(w)] += 1
        self.start = start


    def encrypt(self, word1: str) -> str:
        ans = []
        for w in word1:
            ans.append(self.k_to_val[w])
        return "".join(ans)

    def decrypt(self, word2: str) -> int:
        return self.start[word2]

print(call_func(["Encrypter", "encrypt", "decrypt"],
[[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]
, globals()))
