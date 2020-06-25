---
layout: default
title: 最接近的三数之和
---

## [16\. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/)

> Medium

#### 思路

看到三数之和，想到[15.三数之和](https://leetcode-cn.com/problems/3sum/)，这道题可以在三数之和的基础上思考。

* 首先想到暴力解法，我们如果使用暴力的方式来做的话，时间复杂度是$$O(n^3)$$，肯定是需要优化的
* 题目要求返回的是和，跟数组的下标没有关系，也就是说原数组的顺序是可以打乱的
* 当我们先确认一个数之后，问题就转变成，剩下的有序列表中选两个，使三数的和最接近于`target`
* 可以使用双指针中的碰撞指针，指向数组两端，向中间收缩。时间复杂度为$$O(n)$$
* 第一个数字确认，遍历最外层即可。最终的时间复杂度为$$O(n^2)$$

接下来就能写出代码了，AC！

#### 代码
python3
```python
class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    result = math.inf
    for i in range(len(nums)):
      j = i + 1
      k = len(nums) - 1
      while j < k:
        s = nums[i] + nums[j] + nums[k]
        if s == target:
          return s
        if s > target:
          k -= 1
        else:
          j += 1
        if abs(target-s) <= abs(target-result):
          result = s
    return result
```