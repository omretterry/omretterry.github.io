---
layout: default
title: 两个数组的交集 II
---

## [350\. 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)

> Easy

#### 思路

本题也有多种方法求解，这边选择使用**哈希表**方式

* 使用一个数组，统计数组中各个元素的个数
* 遍历另一个数组，如果这个这个数组中的元素在计数中，且个数不为0，说明这个元素是公共的
* 提取公众元素之后，需要更新技术。将这个元素的技术`-1`，说明已经找到了一个相同的元素

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      r = []
      c = dict(collections.Counter(nums1))
      for i in nums2:
        if i in c and c[i]:
          r.append(i)
          c[i] -= 1
      return r
```