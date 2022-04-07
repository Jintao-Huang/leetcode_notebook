# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.data_structure.trie import Trie, TreeNode2


# 499个.后面跟一个Z. O(26^n)
# 建议用{}做 O(nm). m是之前加入的长度为n的字符串个数
class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def dfs(self, n: TreeNode2, word: str, i: int) -> bool:
        if i == len(word):
            if len(n.word) > 0:
                return True
            else:
                return False
        for ch, n2 in n.children.items():
            ch2 = word[i]
            if ch2 == '.':
                if self.dfs(n2, word, i + 1):
                    return True
            elif ch2 == ch:
                if self.dfs(n2, word, i + 1):
                    return True
                break
        return False

    def search(self, word: str) -> bool:
        r = self.trie.root
        return self.dfs(r, word, 0)

from template.build.call_func import call_func

print(call_func(["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
                , [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]], globals()))