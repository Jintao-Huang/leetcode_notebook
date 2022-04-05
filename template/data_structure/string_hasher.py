# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:


class StringHasher:
    def __init__(self, s: str, min_char='a', base=27, mod=int(1e9) + 7):
        self.base, self.mod = base, mod
        prev_s = [0] * (len(s) + 1)  # 长度
        b = [0] * (len(s) + 1)
        b[0] = 1  # prev_s[0] = 0
        offset = ord(min_char) - 1
        for i in range(len(s)):
            c = s[i]
            prev_s[i + 1] = (prev_s[i] * base + ord(c) - offset) % mod
            b[i + 1] = b[i] * base % mod
        self.prev_s = prev_s
        self.b = b

    def get_hash(self, lo: int, hi: int) -> int:
        # [lo, hi)
        b = self.b[hi - lo]
        str_hash = (self.prev_s[hi] - self.prev_s[lo] * b) % self.mod
        return str_hash


sh = StringHasher("aaa")
print(sh.get_hash(0, 1))
