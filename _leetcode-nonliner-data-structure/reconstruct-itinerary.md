---
layout: default
title: 重新安排行程
---

## [332\. 重新安排行程](https://leetcode-cn.com/problems/reconstruct-itinerary/)

> Medium

#### 思路

**抽象题目大意**

* 所有的机票，指定了两个节点和一个变，我们可以构造成一个**图**，使用**邻接表**表示
* 题目要求的值，就是求**欧拉路径**
* 题目中提示说*假定所有机票至少存在一种合理的行程*，即，我们构造的图一定是**半欧拉图**

**欧拉图的相关文档**
> [https://zhuanlan.zhihu.com/p/108411618](https://zhuanlan.zhihu.com/p/108411618)

* 这道题主要利用**半欧拉图**中的一个特性：一个节点的**出度**为0的时候，说明这个节点为终点
* 将走过的路径，即节点的边删除。遇到出度为0的节点时，说明为终点
* 使用**栈**存放终点的节点，然后进行回溯。剩下的图为新的子问题
* 最终结果即为栈中的元素取反

建议草稿纸上演算一下，一图胜千言，参考解题：[链接](https://leetcode-cn.com/problems/reconstruct-itinerary/solution/gua-he-xin-shou-de-shi-pin-jiang-jie-by-sheldonx-5/)

以上，尝试一下代码，AC！

#### 代码
python3
```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      graph = collections.defaultdict(list)
      for t in tickets:
        graph[t[0]].append(t[1])
        graph[t[0]].sort()
      res = []
      def helper(node):
        while graph[node]:
          helper(graph[node].pop(0))
        res.append(node)

      helper('JFK')
      return res[::-1]
```