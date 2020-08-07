---
layout: default
title: 回文对
---

## [336\. 回文对](https://leetcode-cn.com/problems/palindrome-pairs/)

> Hard


### 方法一（暴力）（TLE）
#### 思路

首先想到了方式是暴力求解，遍历所有索引对，判断所有拼成的字是不是回文字。如果是的话，将索引对放到结果当中

尝试写一下代码，TLE

#### 代码
python3
```python
class Solution:
    def isPalindrome(self, word):
      i = 0
      j = len(word) - 1
      while i < j:
        if word[i] == word[j]:
          i += 1
          j -= 1
        else:
          return False
      return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
      res = []
      for i in range(len(words)-1):
        for j in range(i+1, len(words)):
          if self.isPalindrome(words[i]+words[j]):
            res.append([i,j])
          if self.isPalindrome(words[j]+words[i]):
            res.append([j,i])
      return res
```

### 方法二（哈希表）

#### 思路

优化以上代码，我们可以从单词拆分的角度出发。

* 假如一个单词是回文字，说明这个单词是`轴对称`的。中轴左右拓展的单词的子串都是回文的
* 如果说我们能在某个单词中，找到回文字的`中轴周围的区域`的话，那么多出来的部分的倒序，能在列表中找到的话，说明可以组成一个回文字，如下图：
![](/public/images/palindrome-pairs-1.png)
* 遍历每个字的所有切割方式，可能是`回文字+需要寻到的倒序`，也可能是`需要寻找的倒序+回文字`
* 需要考虑空字符串，但是`空+需要寻找的倒序`和`需要寻找的倒序+空`会有重复统计，最后去一下重

尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def isPalindrome(self, w):
      i, j = 0, len(w)-1
      while i < j:
        if w[i] == w[j]:
          i += 1
          j -= 1
        else:
          return False
      return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
      res = []
      rs = {}
      for i,w in enumerate(words):
        rs[w[::-1]] = i
      for k,w in enumerate(words):
        for i in range(len(w)+1):
          w1 = w[:i]
          w2 = w[i:]
          if self.isPalindrome(w1) and w2 in rs and rs[w2] != k:
            res.append([rs[w2],k])
          if self.isPalindrome(w2) and w1 in rs and rs[w1] != k:
            res.append([k,rs[w1]])
      return list(set([tuple(x) for x in res]))
```