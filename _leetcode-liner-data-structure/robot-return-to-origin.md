---
layout: default
title: 机器人能否返回原点
---

## [657\. 机器人能否返回原点](https://leetcode-cn.com/problems/robot-return-to-origin/)

> Easy

#### 思路

思路应该还是比较清晰的

* 首先我们知道，向上走和向下走可以相消回到原点，向左走和向右走可以相消回到原点
* 怎么走的先后顺序其实不用考虑，比如，之前走过'上'，之后无论什么时候走'下'都能将他抵消掉
* 用一个**哈希表**统计上下左右的数量，遍历走的路线进行添加或者抵消，最终得出结果

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def judgeCircle(self, moves: str) -> bool: 
    counter = {"R":0,"L":0,"U":0,"D":0}
    pairs = {"R":"L","L":"R","U":"D","D":"U"}
    for m in moves:
      if counter[pairs[m]] > 0:
        counter[pairs[m]] -= 1
      else:
        counter[m] += 1
    for k,v in counter.items():
      if v != 0:
        return False
    return True
```