---
layout: default
title: 字符串相加
---

## [415\. 字符串相加](https://leetcode-cn.com/problems/add-strings/)

> Easy

#### 思路

按照我们数学上计算两个数相加的思路
* 倒序，从最后两个数的最后一个数字开始相加
* 纪录进位，如果两数相加超过`10`要向前进一位

以上，尝试一下代码，AC！

#### 代码
python3
```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
      if len(num1) < len(num2): 
        s,l = num1,num2 
      else:
        s,l = num2,num1
      car = 0
      res = ''
      rs = s[::-1]
      rl = l[::-1]
      for i in range(len(rl)):
        t = int(rl[i]) + car
        if i < len(rs):
          t += int(rs[i])
        res += str(t % 10)
        car = 0
        if t >= 10:
          car += 1
      return res[::-1] if car == 0 else '1' + res[::-1]
```