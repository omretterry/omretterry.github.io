---
layout: default
title: 最佳观光组合
---

## [1014\. 最佳观光组合](https://leetcode-cn.com/problems/best-sightseeing-pair/)

> Medium

#### 思路

一开始的想法使用暴力法，双for然后计算出每一个景点和当前景点组成的景点对的评分，再求出最大值

但是如果能AC肯定不是Medium题，但是双for很快。花个半分钟试一下，不亏

TLE！

#### 代码（TLE）
python3
```python
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
      r = 0
      for i in range(len(A)):
        for j in range(i+1, len(A)):
          r = max(r, A[i] + A[j] + i - j)
      return r
```

**改进思路**

和设想的一样，果不其然，TLE了。需要改进思路，再分析一下题意。

* 题目要求`max(A[i]+A[j]+i-j)`，其实就等价于`max(A[i]+i+A[j]-j)`，等于`max(A[i]+i) + max(A[j]-j)`
* 在遍历过程中，我们使用一个变量保存`max(A[i]+i)`
* 如果单独在计算`max(A[j]+j)`,又需要在遍历一次，又是$$O(n^2)$$
* 我们可以直接定义dp变量，`dp`表示当前到i位置最大的值，即`dp = max(dp,dp+max(A[i]+i)`
* 使用**滚动数组**思想，将结果取最大值，每次遍历如果比当前的结果大，就更新结果

尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        dp = -1
        pre = A[0]
        for i in range(1,len(A)):
            dp = max(dp, A[i] - i + pre)
            pre = max(pre, A[i] + i)
        return dp
```