---
layout: default
title: 计数二进制子串
---

## [696\. 计数二进制子串](https://leetcode-cn.com/problems/count-binary-substrings/)

> Easy

#### 思路

* 因为只有`0`和`1`两种字符，我们可以统计连续的字符的数量，这样，前后连续数量相同的字串，就是相邻两个计数中，较少的值。
* 统计连续字符数量，可以使用**双指针**的方式来做

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
      cnts = []
      i = 0
      j = 1
      while i < len(s) and j < len(s):
        if s[j] != s[i]:
          cnts.append(j-i)
          i = j
          j = i + 1 
        else:
          j += 1
      cnts.append(j-i)
      res = 0
      for k in range(1,len(cnts)):
        res += min(cnts[k], cnts[k-1])
      return res
```