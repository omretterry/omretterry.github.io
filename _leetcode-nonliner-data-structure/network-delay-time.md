---
layout: default
---

## [743\. 网络延迟时间](https://leetcode-cn.com/problems/network-delay-time/)

> Medium

#### 思路

`双周赛 #27` 和 `周赛 #193` 碰到了两道图的题目，[课程安排 IV](/leetcode/contest/course-schedule-iv) 学习了，Floyd算法（多源最短路径算法）。同时接触到了Dijkstra 同源最短路径算法，但是一直没有时间学习。通过这道题，边学习边尝试写一下。

**Dijkstra算法学习**

>有关Dijkstra的解释，看完以下的文章就理解了，讲的非常清晰
> * [https://www.codingame.com/playgrounds/1608/shortest-paths-with-dijkstras-algorithm/introduction](https://www.codingame.com/playgrounds/1608/shortest-paths-with-dijkstras-algorithm/introduction)
> * [https://wiki.jikexueyuan.com/project/easy-learn-algorithm/dijkstra.html](https://wiki.jikexueyuan.com/project/easy-learn-algorithm/dijkstra.html)

>图的问题，无论是使用什么算法，基本上我们都需要构造邻接图或邻接矩阵。看完下面的文章，应该可以掌握了
>* [https://www.jianshu.com/p/ce4109962031](https://www.jianshu.com/p/ce4109962031)
>* [https://www.jianshu.com/p/fbbabb0331ce](https://www.jianshu.com/p/fbbabb0331ce)

**新手总结**

* **邻接表的构造**，我们可以使用矩阵的方式，即**邻接矩阵**。矩阵有两个维度，可以表示方向。矩阵的值用于存放带权图中的权重，比如，所花时间，费用，距离等等
* **dis数组**，还需要使用一个一维数组，用于存放点到目标点的距离。根据邻接矩阵初始化，经过对当前点的关联点的遍历和距离计算，更新数组中到当前点的距离值。
* **dis数组的更新**，下一个点选用`dis数组`中距离当前点最近的点开始，不断更新距离值，这个操作叫做`松弛`
* **path数组**， 本题没有用到，但是假如我们就要找到最短路径并且打印出该路径。我们就需要使用一个数组用于存放所走的路径。每次更新`dis数组`时，说明我们找到一条更近的路径，我们就需要将这个节点更新到`path数组`当中。具体可以查阅Disjkstra算法学习的第一个链接。

**回到本题**

* 再回到这道题，其实已经很明显了。题目给定了一个带权有向图，并且指定从某个点出发，正好符合Dijkstra算法的使用场景。
* 重新理解提议，题目就是求到达所有点的最小路径的中取最大值。
* 首先构造有向图的邻接表。
* 从k点出发，如果遍历邻接表结束后，最终还有节点没有访问到。说明无法使所有节点都达到，返回`-1`


以上，知识储备已就位，尝试写一下代码，AC！

#### 代码

python3
```python
class Solution:
    # 根据当前节点，选出距离当前节点最近的节点
    def closestNode(self, visited, node, dis):
        temp = math.inf
        cur_node = 0
        for n in range(len(dis)):
            if n not in visited and n != 0 and n != node:
                if dis[n] < temp:
                    temp = dis[n]
                    cur_node = n
        return cur_node
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 构造邻接表/邻接矩阵
        graph = [[math.inf for _ in range(N+1)] for _ in range(N+1)]  # 多个(0,0),这样使符合题目中节点值等于下标
        for t in times:
            graph[t[0]][t[1]] = t[2]
        for n in range(N+1):
            graph[n][n] = 0
        visited = set()
        dis = [math.inf] * (N + 1)  # 记录节点的距离，index代表数字，多个0
        for n in range(N+1):
          dis[n] = graph[K][n]
        dis[0] = -1
        dis[K] = 0
        cur_node = K
        for _ in range(N+1):
          for d in range(1, len(dis)):
            if (dis[cur_node] + graph[cur_node][d]) < dis[d]:
              dis[d] = dis[cur_node] + graph[cur_node][d]
          visited.add(cur_node)
          cur_node = self.closestNode(visited, cur_node, dis)
        result = max(dis)
        return result if result < math.inf else -1
```