---
layout: default
title: 三次操作后最大值与最小值的最小差
---

## [1509\. 三次操作后最大值与最小值的最小差](https://leetcode-cn.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/)

> Medium

#### 思路

* 首先有一点显而易见的，当数组的长度小于等于`4`的时候，结果为`0`，因为可以将三个数字变成和剩下的一样，差值就为`0`
* 进而发现，我们将三个数字变成任意数的操作，和选三个数删除的效果是一样的。
* 如果我们要选择删除三个数使得剩下的值的最大值和最小值的差最小的话肯定是在前三个和最后三个这几个元素中选三个删除
* 于是有了如下图，前后元素合起来是一个大小为`3`的窗口，计算这些可能性中的最小值，即我们要的结果
![](/public/images/minimum-difference-between-largest-and-smallest-value-in-three-moves-1.png)

以上，AC！

#### 代码
python3
```python
class Solution:
    def minDifference(self, nums: List[int]) -> int:
      if len(nums) < 5:
        return 0
      nums.sort()
      res = math.inf
      for i in range(4):
        res = min(res, nums[-(4-i)]-nums[i])
      return res
```