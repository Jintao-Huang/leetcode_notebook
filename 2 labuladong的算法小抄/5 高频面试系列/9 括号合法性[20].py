# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        left = {'(', '[', '{'}
        for c in s:
            if c in left:
                st.append(c)
            else:
                if len(st) <= 0:
                    return False
                t = st.pop()
                if c == ')' and t == '(' or \
                    c == ']' and t == '[' or \
                    c == '}' and t == '{':
                    pass
                else:
                    return False
        return len(st) == 0  # !


print(Solution().isValid(")"))