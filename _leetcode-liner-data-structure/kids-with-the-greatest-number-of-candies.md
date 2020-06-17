---
layout: default
---

## [1431\. 拥有最多糖果的孩子](https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/)

> Easy

#### 思路

题目还是很容易理解。自然想到的方法是，先获取分糖之前，最富有的那个孩子是多少个糖。然后遍历孩子，假如我把多余的糖都给他，检查他能否超过最大值，AC！

#### 代码

pyhton3
```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      result = [False] * len(candies)
      m = max(candies)
      for i,c in enumerate(candies):
        if c + extraCandies >= m:
          result[i] = True
      return result
```
