---
layout: default
title: 钥匙和房间
---

## [841\. 钥匙和房间](https://leetcode-cn.com/problems/keys-and-rooms/)

> Medium

#### 思路

* 根据题目意思可以基本发现，每一个房间构成一个图，房间中的钥匙就是该节点的`出度`
* 使用DFS遍历图，当经过的所有节点，等于房间数量的时候，表示将所有房间都走过，返回`True`
* 如果没有走完左右房间，返回`False`

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = set()
    def helper(curIndex):
      visited.add(curIndex)
      for n in rooms[curIndex]:
        if n not in visited:
          helper(n)
    helper(0)
    return len(visited) == len(rooms)
```