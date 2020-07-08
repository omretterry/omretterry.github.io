---
layout: default
title: 不同路径 II
---

## [63\. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)

> Medium

#### 思路

这题和[62. 不同路径](./unique-paths-ii)基本是一样的，唯一增加的条件就是中间可能有障碍物的情况

* 同样也是定义`dp`数组，`dp[i][j]`表示`(i,j)`节点可能的路径
* 如果`(i,j)`节点恰好是障碍物，可能路径为`0`
* 如果不是障碍物，就和[62. 不同路径](./unique-paths-ii)一样，为`dp[i][j] = dp[i-1][j] + dp[i][j-1]`
* BaseCase: 边界同样也是初始化为`1`但是如果障碍物在边界，碰到之后，后面的都是`0`

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
      row = len(obstacleGrid)
      col = len(obstacleGrid[0])
      dp = [[ 0 for _ in range(col) ] for _ in range(row)]
      for k in range(row):
        if obstacleGrid[k][0] == 1:
          break
        dp[k][0] = 1

      for k in range(col):
        if obstacleGrid[0][k] == 1:
          break
        dp[0][k] = 1

      for i in range(1,row):
        for j in range(1,col):
          if obstacleGrid[i][j] == 1:
            dp[i][j] = 0
          else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
      print(dp)
      return dp[-1][-1]
```