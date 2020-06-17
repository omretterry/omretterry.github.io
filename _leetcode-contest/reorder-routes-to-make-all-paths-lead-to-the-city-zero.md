---
layout: default
---

## [重新规划路线](https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

#### 思路
题目里面已经给了我们一些提示，所有的路径形成树。对于树来说无非是BFS&DFS。先不管，还是先分析题目
* 两点之间只有一条路线  &rarr; 相邻的节点形成树（不管方向）
* 要求修改之后所有的点都能走向0节点，那自然可以想到以0作为树的根的话，所有节点的方向都要指向根，要是没有指向上面，就要修改他的方向
```
示例: [[0,1],[1,3],[2,3],[4,0],[4,5]]

            0
          ↙ ↖
         1     4  
       ↙        ↘
      3            5 
    ↗
   2    

向下指的箭头，需要修改方向， result = 3
```
BFS,DFS 这道题应该都可以AC，这边尝试BFS。
实际做的过程中，TLE。 
主要问题在于BFS遍历下一层时，遍历数组并找到包含下一层的路径，且将该路径记录为visited，下次遍历时需要判断路径在不在visited中的路径。其中python的`in`操作太多，增加了时间复杂度。
**改进代码及思路**，进行BFS前，先构建一个邻接表。BFS时对邻接表进行遍历。
#### 代码
python3
```
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
      routes = {}
      for i,o in connections:
        routes[i] = routes.get(i,[]) + [(o, 1)]
        routes[o] = routes.get(o,[]) + [(i, 0)]
      print(routes)
      queue = [0]
      visited = set([0])
      result = 0
      while len(queue):
        node = queue[0]
        del queue[0]
        for n,d in routes[node]:
          if n in visited:
            continue
          result += d
          queue.append(n)
          visited.add(n)
      return result
```
