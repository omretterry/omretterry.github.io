---
layout: default
title: 换酒问题
---

## [1518\. 换酒问题](https://leetcode-cn.com/problems/water-bottles/)

> Easy

#### 思路

直接照着题目意思思考

* 如果喝完之后的空瓶，能在换新酒，那就一直换下去，直到不够换了为之
* 下一次兑换的空瓶由兑换剩下的和换了之后喝剩的空瓶组成

以上，AC！

#### 代码
python3
```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
      empty = numBottles
      res = numBottles
      while empty // numExchange > 0:
        e = empty // numExchange
        res += e
        empty = empty % numExchange + e
      return res
```