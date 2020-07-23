---
layout: default
title: 最小路径和
---

## [64\. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)

> Medium

#### 思路

求最小的和为多少，想到使用**动态规划**求解

* 定义`dp`，`dp[i][j]`表示当走到`(i,j)`的位置时的最小和
* **状态转移** `dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]` 这个状态转移也很好理解，`(i,j)`节点的值可能是`(i-1,j)`和`(i,j-1)`这两个点过来的再加上当前的值。那最小值就为这两种可能性中较小的那个
* Basecase： 第一行的点只能从左边的点过来，上面没点。左边边界只能从上面过来

以上，尝试写一下代码，AC！

#### 代码
python
```python3
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      dp = [[math.inf for _ in range(len(grid[0]))] for _ in range(len(grid))]

      pre = 0
      for i in range(len(grid)):
        dp[i][0] = pre + grid[i][0]
        pre = dp[i][0]

      pre = 0
      for j in range(len(grid[0])):
        dp[0][j] = pre + grid[0][j]
        pre = dp[0][j]
        
      for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
          dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
      return dp[-1][-1]
```

#### 优化

我们可以使用**滚动数组**的方式，把`dp`数组降维到1维。具体思想可以参考[62.不同路径](./unique-paths)

以上，尝试优化代码，AC！

#### 代码
python3
```python
class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    dp = [math.inf for _ in range(len(grid[0]))]
    dp[0] = 0
    for i in range(len(grid)):
      dp[0] += grid[i][0]
      for j in range(1, len(grid[0])):
        dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
    return dp[-1]
```