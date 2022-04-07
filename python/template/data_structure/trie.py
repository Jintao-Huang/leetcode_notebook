# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import Dict


class TreeNode2:
    def __init__(self, word: str = ""):
        self.word = word  # type: str # 完整word
        self.children = {}  # type: Dict[str, TreeNode2]


class Trie:
    def __init__(self):
        self.root = TreeNode2()  # 根

    def insert(self, word: str) -> None:
        n = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in n.children:
                n.children[c] = TreeNode2()
            n = n.children[c]
        n.word = word

    def search(self, word: str) -> bool:
        n = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in n.children:
                return False
            n = n.children[c]
        return len(n.word) > 0

    def startsWith(self, prefix: str) -> bool:
        n = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in n.children:
                return False
            n = n.children[c]
        return True
