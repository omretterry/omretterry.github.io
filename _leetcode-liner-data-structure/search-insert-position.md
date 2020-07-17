---
layout: default
title: 搜索插入位置
---

## [35\. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

> Easy

#### 方法一（暴力）
#### 思路

* 遍历数组，发现第一个不小于元素的位置，那就是我们需要插入的位置
* 遍历结束后还是没有找到，说明是插入到数组的后面

#### 代码
python3
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
        if nums[i] >= target:
            return i
        return len(nums)
```

#### 方法二（二分搜索）
#### 思路

对于这种在排序好的列表中搜索目标值，一眼就是二分搜索题

直接使用python二分库，AC！

#### 代码
python3
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      return bisect.bisect_left(nums,target)
```

面试中肯定不能用库了，手撕也行，AC！

#### 代码
python3
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      lo = 0
      hi = len(nums) - 1
      if nums[-1] < target:
        return len(nums)
      while lo < hi:
        mid = lo + (hi-lo) // 2
        if target <= nums[mid]:
          hi = mid
        else:
          lo = mid + 1
      return lo
```

