---
layout: default
title: 恢复空格
---

## [面试题 17.13\. 恢复空格](https://leetcode-cn.com/problems/re-space-lcci/)

> Medium

#### 思路

使用动态规划方式思考问题

* 定义dp数组`dp[i]`表示`index`为`i`之前的字符串未识别的最少数量
* 把`setence[:i]`记作`s`，`dp[i]` 的状态可能有两种情况：
    * `s`中没有字在字典中的话，那么`dp[i] = dp[i-1] + 1`
    * `s`中包括新加的字`i`组成的词在字典中的话，`dp[i]`等于组成那个字之前的字符串的未识别的最小数量
* 上述第二种情况中的`word`的可能性为`s[j:i] ,j = [1,i]`，一旦这些词在字典中的话，`dp[i] = min(dp[j-1],dp[i])`，这些可能性中的最小的那个，就是未识别的最小的数量
* Base Case： 空字符串不能被识别，`dp[0] = 0`

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def respace(self, dictionary: List[str], sentence: str) -> int:
    dp = [ len(sentence) for _ in range(len(sentence) + 1) ]
    dp[0] = 0
    for i in range(1,len(sentence) + 1):
      dp[i] = dp[i-1] + 1
      for j in range(1, i+1):
        word = sentence[j-1:i]
        if word in dictionary:
          dp[i] =  min(dp[j-1], dp[i])
    return dp[-1]
```

#### 改进

上面方法的**时间复杂度**为： $$O(n^2 * m)$$

在看下本题给的数据规模，最坏情况下为 $$10 ^ 6 * 1.5 * 10^5$$，基本上测试用例严格一点就过不了了

拜读大佬解法，使用**Trie**

对于**Trie**的学习，可以查看 [208. 实现 Trie (前缀树)](./implement-trie-prefix-tree)。作为前置知识可以先做208在回头做这道题

尝试改进代码，AC！

#### 代码
python3
```python
class TrieNode:
  def __init__(self):
    self.children = {}
    self.isWord = False

class Trie:
  def  __init__(self):
    self.root = TrieNode()

  def insert(self,word):
    node = self.root
    for i in range(len(word)-1,-1,-1):
      if word[i] not in node.children:
        node.children[word[i]] = TrieNode()
      node = node.children[word[i]]
    node.isWord = True

  #返回所有i结尾的单词开头的下标
  def search(self,s,i):
    r = []
    node = self.root
    for i in range(i, -1, -1):
      if s[i] not in node.children:
        break
      node = node.children[s[i]]
      if node.isWord:
        r.append(i)
    return r

class Solution:
  def respace(self, dictionary: List[str], sentence: str) -> int:
    trie = Trie()
    for w in dictionary:
      trie.insert(w)

    dp = [ len(sentence) for _ in range(len(sentence) + 1) ]
    dp[0] = 0
    for i in range(1,len(sentence) + 1):
      dp[i] = dp[i-1] + 1

      ws = trie.search(sentence, i-1)
      for w in ws:
        dp[i] =  min(dp[w], dp[i])
    return dp[-1]
```