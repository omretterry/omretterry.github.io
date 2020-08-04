---
layout: default
title: 重新排列字符串
---

## [1528\. 重新排列字符串](https://leetcode-cn.com/problems/shuffle-string/)

> Easy

#### 思路

构造一个长度为字符串的数组，遍历索引，将字符串中对应的字符放到应该在的索引位置上。最后转换成字符串。

以上，AC！

#### 代码
python3
```python
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
      t = ['' for _ in range(len(s))] 
      for i,v in enumerate(indices):
        t[v] = s[i]
      return ''.join(t)
```