---
layout: default
title: 课程表
---

## [207\. 课程表](https://leetcode-cn.com/problems/course-schedule/)

> Medium

#### 思路

##### 前置知识

**拓扑排序**
* [什么是拓扑排序?](https://www.jianshu.com/p/b59db381561a)
    * 拓扑排序，是有向无环图（DAG）的所有顶点的线性序列
    * 只有DAG（有向无环图）有拓扑排序

**解题思路**
* 题目可以转换为，判断有向图中是否存在环。所有课程又先后关系，如果存在环说明先后关系矛盾
* 看了上边的连接，我们应该能想到这题的解决办法：使用拓扑排序来判断题目给定的图中是否存在环
* 构建一个**入度表**，入度为`0`表示没有指向当前节点的节点。那么这个节点应该是在拓扑排序较前的位置
* 使用一个队列，将入度为`0`的节点放入队列中，从这些节点出发，向他们的下一个节点走。走完之后，将这个节点的入度设为`-1`下一个节点的入度设置为`0`，表示从图中删除这个节点
* 如果图中没有环，最后左右节点都删除，也就是所有出队的节点数是等于图中的节点数的。如果有环则不相等

>Krahets大佬解题中的动图相当直观，可以看一下: [链接](https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/)

以上，尝试写一下代码，AC！

#### 代码
python
```python3
class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adja = [[] for _ in range(numCourses)]
    indeg = [0] * numCourses
    for p in prerequisites:
      indeg[p[0]] += 1
      adja[p[1]].append(p[0])
    queue = []
    for i,d in enumerate(indeg):
      if d == 0:
        queue.append(i)
    nums = 0
    while len(queue):
      cur = queue[0]
      del queue[0]
      nums += 1
      indeg[cur] -= 1
      for a in adja[cur]:
        indeg[a] -= 1
        if indeg[a] == 0:
          queue.append(a)
    return nums == numCourses
```