---
layout: default
title: 和为奇数的子数组数目
---

## [1524\. 和为奇数的子数组数目](https://leetcode-cn.com/problems/number-of-sub-arrays-with-odd-sum/)

> Medium

#### 思路

**读题，获得一些线索**
* 看到连续的子数组的和，我们想到使用**前缀和**的方式求解。
* 查看数据规模，我们应该尽量是在$$O(n)$$的时间复杂度完成，否则有可能会超时。

**尝试求解**
* 首先构造前缀和数组，子数组的和为，大的索引的值减去小的索引的值
* 但是我们如果需要求出所有子数组的和，在进行数量统计的话，时间复杂度为$$O(n^2)$$，显然是要超时的
* 题目中是要求统计奇偶，我们知道被减数和减数中有且只有一个数为奇数时，差为奇数
* 遍历一遍前缀和数组，分别统计奇数和偶数的个数。当遇到奇数时，之前统计的所有的偶数和当前值构成的差（即某个子数组的和）为奇数；反之，当遇到偶数时，之前统计的所有奇数与当前值构成的差也为奇数

以上，AC！

#### 代码
python3
```python
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
      presum = [0] * len(arr)
      pre = 0
      for i,v in enumerate(arr):
        presum[i] = pre + v
        pre = presum[i]
      presum = [0] + presum
      
      cnt1 = 0
      cnt2 = 0
      res = 0
      for i in presum:
        if i % 2 == 0:
          cnt2 += 1
          res += cnt1
        else:
          cnt1 += 1
          res += cnt2
      return res % (10**9+7)
```