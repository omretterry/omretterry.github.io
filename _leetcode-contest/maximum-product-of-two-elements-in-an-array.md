---
layout: default
---

## [数组中两元素的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array/)

#### 思路
基本周赛第一题都是签到题，直接遍历，双For暴破，AC！
* 当然也有其他思路：排序之后，使用最后两个数进行计算

#### 代码
python3
```
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r = 0
        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                r = max(r, (nums[i]-1) * (nums[j] -1))
        return r
```