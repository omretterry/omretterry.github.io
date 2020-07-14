---
layout: default
title: 好数对的数目
---

## [1512\. 好数对的数目](https://leetcode-cn.com/problems/number-of-good-pairs/)

> Easy

#### 思路

周赛时间有限，首先想到的肯定是**双for爆破**

AC!

#### 代码
python3
```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
      r = 0
      for i in range(len(nums)):
        for j in range(i+1,len(nums)):
          if nums[i] == nums[j]:
            r += 1
      return r
```

#### 哈希表+排列组合

还有一种方法，可以使用哈希表，统计每个数字的数量，然后计算相同数字的排列组合

这种方法也很简单

AC！

#### 代码
python3
```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
      c = collections.Counter(nums)
      r = 0
      for k,v in c.items():
        if v >= 2:
          r += math.comb(v,2)
      return r
```