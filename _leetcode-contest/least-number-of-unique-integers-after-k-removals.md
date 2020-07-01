---
layout: default
title: 不同整数的最少数目
---

## [1481\. 不同整数的最少数目](https://leetcode-cn.com/problems/least-number-of-unique-integers-after-k-removals/)

> Medium

#### 思路

周赛这道题没有花多久

* 主要思路：先统计出所有数字的个数，讲这些数字个数从小到大排序。
* 从数量少的开始删，这样可以保证在`k`个数量中，能删除的数字的种类是最多的

以上，AC！

#### 代码
python3
```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
      c = collections.Counter(arr)
      temp = 0
      remove = 0
      sc = sorted(c.values())
      for v in sc:
        if v <= k:
          k = k - v
          remove += 1
      return len(c) - remove
```