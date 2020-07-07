---
layout: default
title: 避免洪水泛滥
---

## [1488\. 避免洪水泛滥](https://leetcode-cn.com/problems/avoid-flood-in-the-city/)

> Medium

#### 思路

周赛没有解出来，拜读大佬思想获取思路

* **核心思路：** 延时决策
    * 先不在晴天的时候做出决策
    * 在雨天时，再决定需要在之前的某个晴天抽水
* 先将所有的晴天的信息收集起来，等到后面下雨天的时候使用
* 当某一个湖已经满了，然后又要下雨了，我们需要找到一个晴天来抽干，如果找不到的话，说明无解
* **如何决定哪个晴天来进行抽水？** 
    * 找到上次这个湖下雨后的第一个晴天来抽
    * 使用之后，这个晴天就不能在抽水了，需要删除这个晴天记录
* 搜索某一天后的第一个晴天，最坏情况的时间复杂度为$$O(n^2)$$，题目中的数据范围$$10^5$$显然不能完成。使用二分搜索进行优化

**为什么要用上一次这个湖下雨后的第一个晴天来抽取？**

`012012` 对于这个实例来说，第二个`1`时发现需要抽水，有两个晴天但是不是每一个晴天都是可用的。第一个`0`在`1`之前，所以抽了对`1`没有什么影响，所以选需要选择上一次下雨之后的晴天来使用。假如下雨之后有多个晴天可以使用，通过贪心的思想，我们就使用最近的一个晴天。因为后面的日子选择的余地肯定比刚发生的是要多的。需要细品。

尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def search(self,target,suns):
      i = 0
      j = len(suns) - 1
      while i < j:
        mid = i + (j - i) // 2
        if suns[mid] <= target:
          i = mid + 1
        else:
          j = mid
      return suns[i], i

  def avoidFlood(self, rains: List[int]) -> List[int]:
    suns = [] #保存晴天的日子
    record = {} #下雨的日子，有两个内容要保存：湖泊编号，日子。用dict减少查询复杂度
    res = [1 for _ in range(len(rains))]
    for i,rain in enumerate(rains):
      if rain is 0:
        suns.append(i) #记录晴天的日子
      else:
        res[i] = -1
        if rain not in record:
          record[rain] = i #之前没有下过雨
        else:
          start = record[rain] #上次下雨的日子
          if len(suns) is 0:
            return []
          s,k = self.search(start,suns) #搜索上次下雨最近一个晴天
          if s >= i or s <= start:
            return []
          record[rain] = i #更新记录
          res[s] = rain
          del suns[k]
    return res
```