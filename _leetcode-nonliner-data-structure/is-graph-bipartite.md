---
layout: default
title: 判断二分图
---

## [785\. 判断二分图](https://leetcode-cn.com/problems/is-graph-bipartite/)

> Medium

#### 思路

首先读题，二分图似乎是一个固有的概念，搜一下相关文档先
> https://blog.nowcoder.net/n/0e9a713d93f54bc79739588e928f091a

二分图的文章很多，看起来也不是很费劲。二分图似乎还牵扯到了**匈牙利算法**，这道题用不到，暂且搁置

对于二分图的判定，我们使用**涂色法**。**涂色法**的意思是，同一个节点出发，相邻的节点和自身涂成不同的颜色。如果发现相邻的节点已经被上过颜色，而且和自身相同，说明不能构成二分图。对于题目示例我们可以看下图：
![](/public/images/is-graph-bipartite-1.png)

* 示例1，涂色没有冲突，表示是二分图
* 示例2，当涂到1号节点的子节点2号节点时，发现相邻的1号2号为相同颜色，涂色存在冲突，不是二分图
* 图可能存在多个分路，所以外层要进行一次遍历，如果节点已经被访问过就直接跳过
* 涂色的过程是一个树状选择过程，使用DFS或BFS都行

以上，这边选用BFS，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    visited = [0] * len(graph) #已经访问的列表 0:未访问，1：蓝色 2：绿色
    queue= []
    for i in range(len(graph)):
      if visited[i]:
        continue

      queue.append([i,graph[i]])
      visited[i] =  1
      while len(queue):
        p = queue[0]
        del queue[0]
        
        for c in p[1]:
          if visited[c] == 0: #没被染色过
            visited[c] = 1 if visited[p[0]] is 2 else 2
            queue.append([c,graph[c]])
          else:
            if visited[c] == visited[p[0]]:
              print(c,p[0])
              print(visited)
              return False
    return True
```