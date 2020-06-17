---
layout: default
---

## [课程安排 IV](https://leetcode-cn.com/problems/course-schedule-iv/)

#### 思路
这道题在周赛的时候卡了我很久，简单分享一下我的思路吧。构建一张表，index代表课程，他的值为改课程所有的先修课程，如图：
```
示例：
 n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
构造表，如下：
index  value
0     →  null
1     →  0 2
2     →  null
```
遍历该表就能知道，是否为先修课程。但是实际做的过程中发现，我需要不断遍历更新这张表，才能获取正确的值。因为，先修课程可能不是直接联系的，可能中间还隔了好几个。
虽然AC了，但是代码非常糟糕。主要也是因为思路太糟糕。
（补，其实有点邻接表的那个意思了，但是当时对我来说超纲了）

**拜读大佬解法，获得新知识: Floyd-Warshall 算法**
> 相关文章：
> [https://brilliant.org/wiki/floyd-warshall-algorithm/](https://brilliant.org/wiki/floyd-warshall-algorithm/)
> [https://juejin.im/post/5cc79c93f265da035b61a42e](https://juejin.im/post/5cc79c93f265da035b61a42e)
> [https://houbb.github.io/2020/01/23/data-struct-learn-03-graph-floyd](https://houbb.github.io/2020/01/23/data-struct-learn-03-graph-floyd)

花半天时间搞懂了，只能说真的是相当精彩！小伙伴可以看上面的链接，基本都看完应该就能理解了。AC！

#### 代码
python3
```
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
      dp = [[False] * n for _ in range(n)]
      for i,j in prerequisites:
        dp[i][j] = True
      for k in range(n):
        for i in range(n):
          for j in range(n):
            dp[i][j] = (dp[i][k] and dp[k][j]) or dp[i][j]
      return [dp[r][c] for r,c in queries]
```
