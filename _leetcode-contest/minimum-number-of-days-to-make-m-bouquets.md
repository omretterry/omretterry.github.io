---
layout: default
title: 制作 m 束花所需的最少天数
---

## [1482\. 制作 m 束花所需的最少天数](https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets/)

> Medium

#### 思路

周赛的时候没有想到是用二分的方式来做。陷入了暴力的漩涡中。

* 把天数想象成柱状图的感觉，如下图
![](/public/images/minimum-number-of-days-to-make-m-bouquets-1.png)
* 对一个天数`k`,针对特定的某一个花，如果`k`能长成花的话，`k+1`肯定也能长成花。具有单调性
* 可以使用二分，来找到某一天，使得那天的花束满足题目要求

尝试写一下代码，AC！

这道题也可以作为二分法的模板题来记忆一下

#### 代码
python3
```python
class Solution:
    def bouquetNum(self, bloomDay, days, k):
      cnt = 0
      flowers = 0
      for d in bloomDay:
        if d > days:
          flowers = 0
          continue
        flowers += 1
        if flowers == k:
          cnt += 1
          flowers = 0
      return cnt

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
      start = min(bloomDay)
      end = max(bloomDay)

      while start + 1 < end:
        mid = start + (end - start) // 2

        if self.bouquetNum(bloomDay, mid, k) < m:
          start = mid
        else:
          end = mid

      if self.bouquetNum(bloomDay, start, k) >= m:
        return start
      elif self.bouquetNum(bloomDay, end ,k) >= m:
        return end
      
      return -1
```