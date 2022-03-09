# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from collections import deque


class Solution:
    """bfs"""

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = set(wordList)
        ans = 1
        q = deque([beginWord])
        while len(q) > 0:
            for _ in range(len(q)):
                s = q.popleft()
                if s == endWord:
                    return ans
                s = list(s)
                # 选择: 每个idx, 每个字母
                for i in range(len(s)):
                    o = s[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == o:
                            continue
                        s[i] = c
                        s2 = "".join(s)
                        if s2 in d:
                            q.append(s2)
                            d.remove(s2)
                    s[i] = o
            ans += 1
        return 0


from typing import Dict


class Solution2:
    """bfs, 预处理. """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 预处理
        dd = {}  # type: Dict[str, List]
        for i in range(len(wordList)):
            s = wordList[i]
            for j in range(len(beginWord)):
                sr = s[:j] + "*" + s[j + 1:]
                if sr not in dd:
                    dd[sr] = []
                dd[sr].append(s)

        #
        d = set(wordList)
        ans = 1
        q = deque([beginWord])
        while len(q) > 0:
            for _ in range(len(q)):
                s = q.popleft()
                if s == endWord:
                    return ans
                # 选择: 每个idx, 每个可能选项.
                for i in range(len(s)):
                    sr = s[:i] + "*" + s[i + 1:]
                    if sr in dd:
                        for s2 in dd[sr]:
                            if s2 in d:
                                q.append(s2)
                                d.remove(s2)
            ans += 1
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(Solution().ladderLength(beginWord, endWord, wordList))
print(Solution2().ladderLength(beginWord, endWord, wordList))
