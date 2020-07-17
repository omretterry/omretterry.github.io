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

