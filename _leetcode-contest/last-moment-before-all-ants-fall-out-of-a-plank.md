---
layout: default
title: 所有蚂蚁掉下来前的最后一刻
---

## [1503\. 所有蚂蚁掉下来前的最后一刻](https://leetcode-cn.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/)

> Medium

#### 思路

这道题主要考的是思路，能想到就能很快的写出代码

* 所有的蚂蚁都是一样的
* 碰撞之后掉头，和两个蚂蚁穿透的效果是一样的

以上，AC！

#### 代码
python3
```python
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
      return max(max(left) if len(left) else 0, n - (min(right) if len(right) else n))
```