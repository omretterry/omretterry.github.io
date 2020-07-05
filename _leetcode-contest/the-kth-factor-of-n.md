---
layout: default
title: n 的第 k 个因子
---

## [1492\. n 的第 k 个因子](https://leetcode-cn.com/problems/the-kth-factor-of-n/)

> Medium

#### 思路

首先想到的就是使用暴力求解，从小到大一次求出因子。当的到了k个因子时，结束循环返回结果

周赛考虑时间有限，先尝试最明显简单的思路

尝试一下，AC！

#### 代码
python3
```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
      result = []
      for i in range(1,n+1):
        if n % i == 0:
          result.append(i)
          if len(result) == k:
            return i
      return -1
```
