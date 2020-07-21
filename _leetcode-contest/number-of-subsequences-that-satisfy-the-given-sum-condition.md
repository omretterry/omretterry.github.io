---
layout: default
title: 满足条件的子序列数目
---

## [1498\. 满足条件的子序列数目](https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

> Medium

#### 思路

题目大意为：寻找子数组，使的子数组中的最大值和最小值的和小于`target`并统计子数组的数量。

* 关键因素就是找到这个最大值和最小值，如果我们能够找到最大值和最小值的临界值，即`min+max`恰好`<=target`那么我们这个数组里面填充这个范围的任意值都能成立，而且还能将最大值替换成比他小的数，如下图
![](/public/images/number-of-subsequences-that-satisfy-the-given-sum-condition-1.png)
* 对于找到符合条件的最大最小值，我们想到可以使用*对向双指针*的方式来做
* 找到了符合条件的范围，如何统计中范围中的子数组？对于`[num1,num2...numx]`来说，所有的可能性为`2^n-1`，也就是`[num2...numx]`每个数都有两种可能性，可以取，可以不取

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
      nums.sort()
      i = 0 
      j = len(nums)-1
      res = 0
      while i <= j:
        if nums[i] + nums[j] <= target:
          res += 2**(j-i)
          i += 1
        else :
          j -= 1
      return res % (10**9+7)
```