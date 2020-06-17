---
layout: default
---

## [切割后面积最大的蛋糕](https://leetcode-cn.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)

#### 思路

这道题首先意思是，横着切几刀，竖着切几刀。然后形成了若干个区域，问这些区域中最大的面积是多少。

* 要想面积最大，也就是横向最大的间隔和纵向最大的间隔所形成的的区域
* 考虑边界，切割线和边界也能形成间隔
* 那么我们要先排序，因为排序之后我们才知道，哪几条切割线是和边界形成区域的
* 最后，结果对对$$ 10^9 + 7 $$取余取余

AC！

#### 代码

python3
```python
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        hs = horizontalCuts[0]
        vs = verticalCuts[0]
        for l in range(1, len(horizontalCuts)):
          hs = max(hs, horizontalCuts[l] - horizontalCuts[l-1])
        for v in range(1, len(verticalCuts)):
          vs = max(vs, verticalCuts[v] - verticalCuts[v-1])
        hs = max(hs, h - horizontalCuts[-1])
        vs = max(vs, w - verticalCuts[-1])
        return (hs % (10 ** 9 + 7) * vs % (10 ** 9 + 7)) % (10 ** 9 + 7)
```