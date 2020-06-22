---
layout: default
title: 正则表达式匹配
---

## [10\. 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)

> Hard

#### 思路

抖机灵，一下想到的就是，使用正则表达式求解正则表达式。

写一下代码，AC！

#### 代码
python3
```python
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      result = re.fullmatch(p, s)
      return False if result == None else True
```

**正经解法**

未完待续。。。