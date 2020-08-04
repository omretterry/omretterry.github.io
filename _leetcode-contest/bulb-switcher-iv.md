---
layout: default
title: 灯泡开关 IV
---

## [1529\. 灯泡开关 IV](https://leetcode-cn.com/problems/bulb-switcher-iv/)

> Medium

#### 思路

第一眼看到题目，感觉无从下手，只能在纸上画一画慢慢分析了

分析的出一下结论（给小伙伴提示，最好还是能自己在纸上画一画，更加直观）
* 连续的`1`连续的`0`和一个`1`一个`0`的效果是一样的，需要开关的次数是一样的
* **贪心**思考，对于`10011`，首先简化来看就变成了`101`，贪心优先满足前面的`1`，第一步肯定是都开。变为`111`,然后关再开，具体开哪几个关哪几个，取决于后面`1`和`0`的位置
* 所以的出结论，如果遇到一个不连续的`1`，那我们需要两次操作来满足。即`10`这种形式需要多两次。
* 结尾如果是`1`还需要再加上一次

不知道小伙伴有没有理解，这个还是需要自己推演一遍

以上，AC！

#### 代码
python3
```python
class Solution:
    def minFlips(self, target: str) -> int:
      res = 0
      pre = '0'
      for i in target:
        if i == '0':
          if pre == '1':
            res += 2
        pre = i
      if pre == '1':
        res += 1
  
      return res
```