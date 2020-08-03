---
layout: default
title: 概率最大的路径
---

## [1514\. 概率最大的路径](https://leetcode-cn.com/problems/path-with-maximum-probability/)

> Medium

#### 思路

看了数据规模估计**Floyd算法**会超时，果然TLE

尝试使用**Dijkstra同源最短路径算法**，有关**Dijkstra算法**的具体教程，可以查看[743. 网络延迟时间](/leetcode/nonliner-data-structure/network-delay-time)的解题

* 这题与我们的模块题有点不一样的地方是，**松弛**的过程。模板题我们只要选择交长边作为我们下一个节点就行了，这边的话我们需要计算到当前节点的概率，再计算出较大的概率。

**遇到的问题**
* 用二维矩阵形式表示的*邻接矩阵*超时，应为有无效的边也表示在矩阵当中了。改用*字典*形式的*邻接表*优化
* 起始点可能不在给定的图中，也就是说起始点没有相邻的点，直接返回`0`
* 计算下一个点（即到起始点概率最大的点）使用普通队列存放，遍历获取，TLE。改用*优先队列*优化

以上，有点费劲的AC！

#### 代码
python3
```python
class Solution:
    def closestNode(self,visited,queue):
      probs, node = heapq.heappop(queue)
      while visited[node] and len(queue) > 0:
        probs, node = heapq.heappop(queue)
      return probs, node

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
      graph = {}
      for i, item in enumerate(edges):
          s, e, p = item[0], item[1], succProb[i]
          graph.setdefault(s, []).append((e, p))
          graph.setdefault(e, []).append((s, p)) 
      visited = [False for _ in range(n)]
      cur_node = start
      queue = []
      heapq.heappush(queue, (-1, start))
      for _ in range(n):
        if len(queue) == 0:
          return 0
        cur_probs, cur_node = self.closestNode(visited,queue)
        if cur_node not in graph:
          return 0
        visited[cur_node] = True
        if cur_node == end:
          return -cur_probs
        for i in graph[cur_node]:
          if not visited[i[0]]:
            heapq.heappush(queue, (i[1] * cur_probs , i[0]))
      return 0
```