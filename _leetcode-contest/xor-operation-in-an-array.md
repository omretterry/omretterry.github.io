---
layout: default
title: 数组异或操作
---

## [1486\. 数组异或操作](https://leetcode-cn.com/problems/xor-operation-in-an-array/)

> Easy

#### 思路

签到题，直接根据题目意思生成数组，遍历异或求解，AC！

#### 代码
python3
```python
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
      r = 0
      a = [start + x*2 for x in range(n)]
      for i in a:
        r = r ^ i
      return r
```