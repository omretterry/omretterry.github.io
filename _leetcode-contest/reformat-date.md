---
layout: default
title: 转变日期格式
---

## [1507\. 转变日期格式](https://leetcode-cn.com/problems/reformat-date/)

> Easy

#### 思路

使用`split`，分割之后，单独对年月日进行处理，最后合并

AC！

#### 代码
python3
```python
import re
class Solution:
    def reformatDate(self, date: str) -> str:
      d = date.split(' ')
      t = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
      b = t.index(d[1])
      if b + 1 > 9:
        b = str(b+1)
      else:
        b = '0' + str(b+1)
      a = d[2]
      c = re.findall("\d+", d[0])[0]
      if len(c) is 1:
        c = '0' + c
      return a + '-' + b + '-' + c
```