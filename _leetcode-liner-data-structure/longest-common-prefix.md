---
layout: default
---

## [14\. 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

>Easy

#### 思路

要求最长的公共前缀，我们可以想成是字符串都排好，然后我们从左到右扫描一遍。观察都是否都相同，又不相同或者超出字串的长度，就结束。如下图
```python
result      f
            ↓
            f l o w e r
            f l o w
            f l i g h t 

result      f l
              ↓
            f l o w e r
            f l o w
            f l i g h t 

result      f l
              ↓
            f l o w e r
            f l o w
            f l i g h t 
```
尝试写一下代码，AC！

#### 代码

python3
```python
class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
      return ''
    result = ''
    cur = 0
    while True:
      temp = ''
      for s in strs:
        if cur >= len(s):
          return result
        if temp == '':
          temp = s[cur]
        elif temp != '' and temp != s[cur]:
          return result
      result += temp
      temp = ''
      cur += 1
    return result
```