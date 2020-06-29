---
layout: default
title: 数组中的第K个最大元素
---

## [215\. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

> Medium

### 方法一（库函数一把梭）

#### 思路

这题理解上没什么问题，就是先将数组从大到小排序，然后取出第k个元素

最快的就是用库一把梭

#### 代码
python3
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      return sorted(nums, reverse=True)[k - 1]
```

### 方法二（快排）

#### 思路

但是话又说回来了，我们不能为了刷题而刷题。这道题的主要考点是排序，暴力就不写了，太熟了。这道题属于面试高频题，主要也是用来考察快排

快排思想网上太多了，这边就不赘述了，面试基本手撕，考察代码熟练度

练习一下代码，TLE！

#### 代码
python3
```python
class Solution:
    def partition(self, l, l_index, r_index):
        i = l_index - 1
        pivot = l[r_index]  # 最右边的这个作为比较的基准

        for cur_index in range(l_index, r_index):
            if l[cur_index] >= pivot:  # 当前的和基准比较
                i += 1
                l[i], l[cur_index] = l[cur_index], l[i]
        l[i+1], l[r_index] = l[r_index], l[i+1]
        return i + 1

    def quickSort(self, l, l_index, r_index):
        if l_index >= r_index:
          return 
        bound = self.partition(l, l_index, r_index)
        self.quickSort(l,l_index, bound-1)
        self.quickSort(l,bound + 1, r_index)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums[k - 1]
```

练习了一下快排，但是这边TLE了，快排最坏情况下的时间复杂度也是$$O(N^2)$$

**改进思路**

快速排序的思路是分治，题目要求找到第`k`大的元素，我们并不需要想整个数组完全排序之后再得出结果。当我们的pivot的位置已经确定下来之后，其实他就不会再动了。

所以说当`pivot`的`index`刚好是`len(nums) - k`时，`pivot`就是我们想要的结果

调整一下代码，AC！

#### 代码（改进版）
python3
```python
class Solution:
    def partition(self, l, l_index, r_index):
        i = l_index - 1
        pivot = l[r_index]

        for cur_index in range(l_index, r_index):
            if l[cur_index] <= pivot:
                i += 1
                l[i], l[cur_index] = l[cur_index], l[i]
        l[i+1], l[r_index] = l[r_index], l[i+1]
        return i + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        target = len(nums) - k
        while left <= right:
          i = self.partition(nums, left, right)
          if i == target:
            return nums[i]
          elif i < target:
            left = i + 1
          else:
            right = i - 1
        return None
```