---
layout: default
title:  子数组和排序后的区间和
---

## [1508\.  子数组和排序后的区间和](https://leetcode-cn.com/problems/range-sum-of-sorted-subarray-sums/)

> Medium

#### 思路

看到字符组的和，可以想到使用**前缀和**方法来做，在看数据规模，$$O(n^2)$$以下的时间复杂度应该都可以AC。

* 先构造前缀和数组，方便我们后面计算子数组的和
* 将所有子数组和的可能性放到一个新的数组当中
* 排序，根据题目要求求出范围内的和

以上，AC！

#### 代码
python3
```python
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
      presum = [0] * n
      pre = 0
      for i,n in enumerate(nums):
        presum[i] = pre + n
        pre = presum[i]
      presum = [0] + presum

      temp = []
      for i in range(len(presum)):
        for j in range(i+1,len(presum)):
          temp.append(presum[j]-presum[i])
      return sum(sorted(temp)[left-1:right]) % (10**9+7)
```