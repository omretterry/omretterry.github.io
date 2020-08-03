---
layout: default
title: 魔术索引
---

## [面试题 08.03\. 魔术索引](https://leetcode-cn.com/problems/magic-index-lcci/)

> Easy

### 方法一（暴力）
#### 思路

暴力解法思路比较清晰：遍历数组，遇到索引和值相同的情况返回

#### 代码
python3
```python
class Solution:
  def findMagicIndex(self, nums: List[int]) -> int:
    for i,v in enumerate(nums):
      if i == v:
        return i
    return -1
```

### 方法二（分治，DFS）
#### 思路

应为数组是有序的，我们想到能不能用二分方法去做。

* 应为有相同的元素，确定了中间点位后，不能明确的确定*魔术索引*是在左半部分还是右半部分
* 两种可能性都有的话，类似于形成了一个二叉树，我们可以使用DFS来做

最坏情况也是$$O(n)$$

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def helper(self,start,end,nums):
    if start > end:
      return -1
    mid = start + (end-start) // 2
    if mid == nums[mid]:
      return mid
    l_res = self.helper(start,mid-1,nums)
    if l_res == -1:
      return self.helper(mid+1,end,nums)  
    else:
      return l_res 
  def findMagicIndex(self, nums: List[int]) -> int:
    return self.helper(0, len(nums)-1, nums)
```