---
layout: default
---

##  [171\.Excel表列序号](https://leetcode-cn.com/problems/excel-sheet-column-number/) 
> Easy


### 思路


```python
A->1
Z->26
ord(A)->65
ord(Z)->90

题目转换成一个26进制的数10进制的值
```

### 代码

python3
```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        r = 0
        for i in range(len(s)):
            r += 26 ** (len(s) - i - 1) * (ord(s[i]) - 64)
        return r
```
