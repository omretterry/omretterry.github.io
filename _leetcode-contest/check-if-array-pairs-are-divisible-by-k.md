---
layout: default
title: 检查数组对是否可以被 k 整除
---

## [1497\. 检查数组对是否可以被 k 整除](https://leetcode-cn.com/problems/check-if-array-pairs-are-divisible-by-k/)

> Medium

#### 思路

* 根据余数进行排序，余数为`0`的数两两组合可以被`k`整除
* 余数为`0`的数的数量为奇数，说明不能形成两两成对
* 余数最小的数和余数最大的数，组合如果可以被`k`整除，说明可以成对，否则不能成对

以上，AC！

#### 代码
python3
```python
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
      res = [x%k for x in arr]
      res.sort()
      if res.count(0) % 2 == 1:
        return False
      i = 0
      j = len(arr) - 1
      while i < j:
        if res[i] == 0:
          i += 1
          continue
        if (res[i] + res[j]) != k:
          return False
        i += 1
        j -= 1
      return True
```