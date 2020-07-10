---
layout: default
title: 实现 Trie (前缀树)
---

## [208\. 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)

> Medium

#### 思路

首先需要获取**Trie**知识

##### Trie 树的特征
* 根节点的值为空
* 每个节点只需要保存当前字符（也可以记录额外的信息，比如当前节点结束是否组成单词）
* 每个节点所包含的字符各不相同

##### 使用Trie的优缺点

###### 优点
* 插入和查询的效率很高，都为$$O(m)$$,`m` 是待插入/查询的字符串的长度。
* 会有人说 hash 表时间复杂度是$$O(1)$$不是更快？但是，哈希搜索的效率通常取决于 hash 函数的好坏，若一个坏的 hash 函数导致很多的冲突，效率并不一定比Trie树高。
* Trie树中不同的关键字不会产生冲突。
* Trie树只有在允许一个关键字关联多个值的情况下才有类似hash碰撞发生。
* Trie树不用求 hash 值，对短字符串有更快的速度。通常，求hash值也是需要遍历字符串的。
* Trie树可以对关键字按字典序排序。

###### 缺点
* 当 hash 函数很好时，Trie树的查找效率会低于哈希搜索。
* 空间消耗比较大。

所以在一般的工程中，Trie见得比较少，应为要做测试才能比较Trie和Hash的效率。而且一般语言都有Hash的库，但是Trie对象要手撕

##### 刷题中Trie的使用场景
明显用Trie来做的题目的主要特征是，需要大量判断某个字符串是否是给定单词列表中的前缀或后缀

以上，尝试实现Trie

#### 代码
python3
```python
class TrieNode:
  def __init__(self):
    self.children = {}
    self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
          if i not in node.children:
            node.children[i] = TrieNode()
          node = node.children[i]
        node.isWord = True


    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
          if i not in node.children:
            return False
          node = node.children[i]
        return node.isWord


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for p in prefix:
          if p not in node.children:
              return False
          node = node.children[p]
        return True
```