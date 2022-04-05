# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import Dict


class TreeNode:
    def __init__(self, val: str, end: bool):
        self.val: str = val
        self.end: bool = end
        self.children: Dict[str, TreeNode] = {}


"""
1. 防止列表、str的复制，可以使用idx: int。lo, hi等
"""


class WordDictionary:
    """
    211. 添加与搜索单词 - 数据结构设计. 使用前缀树
    """

    def __init__(self):
        self.root = TreeNode('', False)

    def addWord(self, word: str) -> None:
        """O(Len(W))"""
        p: TreeNode = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TreeNode(c, False)
            p = p.children[c]
        p.end = True

    def search(self, word: str) -> bool:
        """O(Len(W)) 或 O(N)"""

        def _search(tn: TreeNode, i: int) -> bool:
            if i == len(word):
                return tn.end
            if word[i] == '.':
                for ctn in tn.children.values():
                    if _search(ctn, i + 1):
                        return True
                return False
            elif word[i] in tn.children:
                tn = tn.children[word[i]]
                return _search(tn, i + 1)
            else:
                return False

        return _search(self.root, 0)

    def search2(self, word: str) -> bool:
        """O(Len(W)) 或 O(N)"""

        def _search(tn: TreeNode, idx: int) -> bool:
            for i in range(idx, len(word)):
                if word[i] == '.':
                    for ctn in tn.children.values():
                        if _search(ctn, i + 1):
                            return True
                    else:
                        return False
                if word[i] in tn.children:
                    tn = tn.children[word[i]]
                else:
                    return False
            return tn.end

        return _search(self.root, 0)


wd = WordDictionary()
wd.addWord("a")
print(wd.search("a."))
print(wd.search2("a."))
"""
False
False
"""


class WordDictionary2:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        """Ot(1)"""
        length = len(word)
        if length in self.d:
            self.d[length] += [word]
        else:
            self.d[length] = [word]

    def search(self, word: str) -> bool:
        """
        使用字典. Ot(LEN_MAX(D[]))
        """
        length = len(word)
        if length not in self.d:
            return False
        for s in self.d[length]:
            for i, c in enumerate(word):
                if c == '.' or c == s[i]:
                    continue
                break
            else:
                return True
        return False


wd = WordDictionary()
wd.addWord("bad")
wd.addWord("baa")
print(wd.search("bad"))
print(wd.search("baa"))
"""
True
True
"""

from typing import Dict


class TreeNode:
    def __init__(self, val: str, end: bool):
        self.val: str = val
        self.children: Dict[str, TreeNode] = {}
        self.end: bool = end


class Trie:
    """208. 实现 Trie (前缀树)"""

    def __init__(self):
        self.root = TreeNode("", False)

    def insert(self, word: str) -> None:
        """Ot(Len(W))"""
        tn: TreeNode = self.root
        for c in word:
            if c not in tn.children:
                tn.children[c] = TreeNode(c, False)
            tn = tn.children[c]
        tn.end = True

    def search(self, word: str) -> bool:
        """Ot(Len(W))"""
        tn: TreeNode = self.root
        for c in word:
            if c in tn.children:
                tn = tn.children[c]
            else:
                return False
        return tn.end

    def startsWith(self, prefix: str) -> bool:
        """Ot(Len(P))"""
        tn: TreeNode = self.root
        for c in prefix:
            if c in tn.children:
                tn = tn.children[c]
            else:
                return False
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))

"""
True
False
True
True
"""

from typing import List


class TreeNode2:
    def __init__(self, word: str = ""):
        self.word: str = word
        self.children: Dict[str, TreeNode2] = {}


class Trie2:
    """208. 实现 Trie (前缀树)"""

    def __init__(self):
        self.root = TreeNode2()

    def insert(self, word: str) -> None:
        """Ot(Len(W))"""
        tn: TreeNode2 = self.root
        for c in word:
            if c not in tn.children:
                tn.children[c] = TreeNode2()
            tn = tn.children[c]
        tn.word = word

    def search(self, word: str) -> bool:
        """Ot(Len(W))"""
        tn: TreeNode2 = self.root
        for c in word:
            if c in tn.children:
                tn = tn.children[c]
            else:
                return False
        return len(tn.word) > 0

    def startsWith(self, prefix: str) -> bool:
        """Ot(Len(P))"""
        tn: TreeNode2 = self.root
        for c in prefix:
            if c in tn.children:
                tn = tn.children[c]
            else:
                return False
        return True


print("-------------")
trie = Trie2()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
"""
True
False
True
True
"""

"""
1. 图的广搜/深搜需要is_visited.
  树不需要
"""


class Solution720:
    """词典中最长的单词"""

    def longestWord(self, words: List[str]) -> str:
        """前缀树"""
        trie = Trie()
        for w in words:
            trie.insert(w)

        res = []
        res_tmp = []

        def _longestWord(tn: TreeNode) -> None:
            nonlocal res
            for ctn in tn.children.values():
                if ctn.end is False:
                    continue
                res_tmp.append(ctn.val)
                if len(res_tmp) > len(res) or len(res_tmp) == len(res) and res_tmp < res:
                    res = res_tmp.copy()
                _longestWord(ctn)
                res_tmp.pop()

        _longestWord(trie.root)
        return "".join(res)

    def longestWord2(self, words: List[str]) -> str:
        """暴力法."""
        word_set = set(words)
        words.sort(key=lambda c: (-len(c), c))  # 从长到短
        for w in words:
            for i in range(1, len(w)):
                if w[:i] not in word_set:
                    break
            else:
                return w
        return ""

    def longestWord3(self, words: List[str]) -> str:
        """暴力法"""
        word_set = set(words)
        words.sort(key=lambda c: (-len(c), c))  # 从长到短
        for w in words:
            if all(w[:i] in word_set for i in range(1, len(w))):
                return w
        return ""

    def longestWord4(self, words: List[str]) -> str:
        """前缀树"""
        trie = Trie2()
        for w in words:
            trie.insert(w)

        res = ""

        def _longestWord(tn: TreeNode2) -> None:
            """DFS"""
            nonlocal res
            for ctn in tn.children.values():
                if ctn.word is "":
                    continue
                if len(ctn.word) > len(res) or len(ctn.word) == len(res) and ctn.word < res:
                    res = ctn.word
                _longestWord(ctn)

        _longestWord(trie.root)
        return res


words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(Solution720().longestWord(words))
print(Solution720().longestWord2(words))
print(Solution720().longestWord3(words))
print(Solution720().longestWord4(words))

# TreeNode = lambda word="": {"word":word, "children":{}}
