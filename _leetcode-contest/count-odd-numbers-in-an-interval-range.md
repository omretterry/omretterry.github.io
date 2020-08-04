---
layout: default
title: 在区间范围内统计奇数数目
---

## [1523\. 在区间范围内统计奇数数目](https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range/)

> Easy

#### 思路

第一眼想到暴力，计算处于所有奇数，然后在统计他们的个数。

这边肯定不用这么麻烦，我们知道，奇数偶数是交替出现的。那个数就是和边界范围有关。考虑一下边界条件，举两个示例测试一下，就能找到规律了。

以上，AC！

#### 代码
python3
```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
      res = (high - low)//2
      if low % 2 == 1 or high % 2== 1:
        return res + 1
      else:
        return res
```