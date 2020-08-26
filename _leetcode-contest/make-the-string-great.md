---
layout: default
title: 整理字符串
---

## [1544\. 整理字符串](https://leetcode-cn.com/problems/make-the-string-great/)

> Easy

#### 思路

这道题和有效扩号是相同的思路，使用**栈**，比较栈顶元素，如果是相同的字母且大小写相反的话。将栈顶元素出栈。最终返回栈内元素组成的字符串。

#### 代码
python3
```python
class Solution:
    def makeGood(self, s: str) -> str:
      stack = []
      for i in range(len(s)):
        if i == 0 or len(stack) == 0:
          stack.append(s[i])
          continue
        cur = stack[-1]
        if (cur.lower() == s[i].lower()) and \
          ((cur.islower() and s[i].isupper()) or (cur.isupper() and s[i].islower())):
          stack.pop()
          continue
        else:
          stack.append(s[i])
      return ''.join(stack)
```