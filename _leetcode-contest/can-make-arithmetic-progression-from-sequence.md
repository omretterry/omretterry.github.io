---
layout: default
title: 判断能否形成等差数列
---

## [1502\. 判断能否形成等差数列](https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence/)

> Easy

#### 思路

签到题，这题主要考察的是排序，但是周赛时间有限，直接使用库函数

排序之后，遍历检查元素之间的差值是否相等。如果遇到不相等的情况，直接返回`False`

以上，AC！

#### 代码
python3
```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
      arr.sort()
      if len(arr) is 2:
        return True
      k = arr[1] - arr[0]
      for i in range(1,len(arr)):
        if arr[i] - arr[i-1] != k:
          return False
      return True
```