# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

def paren_match(s: str) -> bool:
    """Ot(N)"""
    stack = []
    for c in s:
        if c in ('(', '[', '{'):
            stack.append(c)
        elif len(stack) == 0:
            return False
        elif c == ')' and stack[-1] == '(':
            stack.pop()
        elif c == ']' and stack[-1] == '[':
            stack.pop()
        elif c == '}' and stack[-1] == '{':
            stack.pop()
        else:
            return False
    return len(stack) == 0
