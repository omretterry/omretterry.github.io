---
layout: default
title: 一维数组的动态和
---

## [1480\. 一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array/)

> Easy

#### 思路

可以发现这道题就是求前缀和，是处理一些复杂问题的前置操作

使用一个变量记录当前数字之前的和，在加上当前数字就是到当前数字位置的和

尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      temp = 0
      result = [0] * len(nums)
      for i in range(len(nums)):
        result[i] = temp + nums[i]
        temp = result[i]
      return result
```