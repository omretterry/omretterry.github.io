---
layout: default
title: 删掉一个元素以后全为 1 的最长子数组
---

## [1493\. 删掉一个元素以后全为 1 的最长子数组](https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

> Medium

#### 思路

从数据量大小判断，肯定是要用时间复杂度$$O(n)$$算法求解

* 遍历一遍数组，遍历时记录`1`的数量，遇到`0`时记录一下，第一次遇到，这个`0`是可删除的。再次遇到`0`，不能删除，比较较大的数，记录到结果中
* 特判一下，如果都为`1`则直接返回`数组长度-1`

以上，尝试一下代码，AC！

#### 代码
python3
```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
      if nums.count(1) == len(nums):
        return len(nums) - 1
      pc = 0
      cnt = 0      
      r = 0
      for i in nums:
        if i == 1:
          cnt += 1
        else:
          r = max(r, pc+cnt)
          pc = cnt
          cnt = 0
        prev = i
      r = max(r, pc+cnt)
      return r
```