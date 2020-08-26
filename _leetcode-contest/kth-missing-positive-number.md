---
layout: default
title: 第 k 个缺失的正整数
---

## [1539\. 第 k 个缺失的正整数](https://leetcode-cn.com/problems/kth-missing-positive-number/)

> Easy

#### 思路

将现有数组构造成哈希表，然后逐个遍历，直到数出不在哈希表中的第`k`个数

以上，AC！

#### 代码
python3
```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
      s = set(arr)
      res = 0
      l = 0
      for x in range(1,10000):
        if l == k:
          return res
        if x not in s:
          res = x
          l += 1
```