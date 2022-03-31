# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        cnt = 0  # pattern
        n_a, n_b = 0, 0
        for i in range(len(text)):
            if text[i] == pattern[1]:
                cnt += n_a
                n_b += 1
            if text[i] == pattern[0]:
                n_a += 1

        return max(n_a, n_b) + cnt

text = "fwymvreuftzgrcrxczjacqovduqaiig"
pattern = "yy"
print(Solution().maximumSubsequenceCount(text, pattern))