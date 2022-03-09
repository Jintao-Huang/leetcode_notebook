# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict, Deque, Tuple
from collections import deque


class Node:
    def __init__(self, s):
        self.s = s
        self.children = []


class Solution:
    """bfs, dfs, 预处理"""

    def __init__(self):
        self.ans: List[List[str]]

    def _bfs(self, beginWord: str, endWord: str, wordList: List[str], dd: Dict[str, List[str]]) -> Tuple[Node, bool]:

        node_mapper = {beginWord: Node(beginWord)}  # type: Dict[str, Node]
        d = set(wordList)
        if beginWord in d:
            d.remove(beginWord)
        prev_d = d.copy()
        #
        head = node_mapper[beginWord]
        q = deque([head])  # type: Deque[Node]
        find = False
        while not find and len(q) > 0:
            for _ in range(len(q)):
                n = q.popleft()
                s = n.s
                if s == endWord:
                    find = True
                # 选择: 每个idx, 每个可能选项.
                for i in range(len(s)):
                    sr = s[:i] + "*" + s[i + 1:]
                    if sr in dd:
                        for s2 in dd[sr]:
                            if s2 in prev_d:
                                if s2 not in node_mapper:
                                    node_mapper[s2] = Node(s2)
                                n2 = node_mapper[s2]
                                n.children.append(n2)
                                if s2 in d:
                                    q.append(n2)
                                    d.remove(s2)
            prev_d = d.copy()
        return head, find

    def _dfs(self, n: Node, path: List[str], endWord: str) -> None:
        if n.s == endWord:
            self.ans.append(path.copy())
            return
        for c in n.children:
            path.append(c.s)
            self._dfs(c, path, endWord)
            path.pop()

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.ans = []
        #
        dd = {}  # type: Dict[str, List[str]]
        for i in range(len(wordList)):
            s = wordList[i]
            for j in range(len(beginWord)):
                sr = s[:j] + "*" + s[j + 1:]
                if sr not in dd:
                    dd[sr] = []
                dd[sr].append(s)

        # bfs
        head, find = self._bfs(beginWord, endWord, wordList, dd)
        # dfs
        if find:
            self._dfs(head, [beginWord], endWord)

        return self.ans


# beginWord = "aa"
# endWord = "bb"
# wordList = ["ab", "ba", "bb"]
# print(Solution().findLadders(beginWord, endWord, wordList))
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().findLadders(beginWord, endWord, wordList))
beginWord = "red"
endWord = "tax"
wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
print(Solution().findLadders(beginWord, endWord, wordList))
