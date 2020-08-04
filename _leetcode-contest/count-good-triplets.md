---
layout: default
title: 统计好三元组
---

## [1534\. 统计好三元组](https://leetcode-cn.com/problems/count-good-triplets/)

> Easy

#### 思路

第一眼，暴力！

再看一眼数据规模，暴力！

以上，AC！

#### 代码
python3
```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
      res = 0
      for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
          for k in range(j+1,len(arr)):
            if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
              res += 1
      return res
```