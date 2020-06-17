---
layout: default
---

## [摘樱桃 II](https://leetcode-cn.com/problems/cherry-pickup-ii/)

#### 思路

周赛时放弃了，虽然知道是动态规划，但是没有什么思路

**拜读大佬解法，获得新思路**

* 因为只能向下走，行号具有**后无效性**，可以进行状态转移，使用dp
* 有两个机器人还需要使用两个维度记录记录两个机器人所在的位置
* dp[r][i][j], r为行号，i为Robot#1（以下简称R1） 所在的位置，j为Robot#2（以下简称R2） 所在的位置
* dp表示走到r行，R1在i位置，R2在j位置，所能摘到的最多的樱桃数
* **状态转移思考:** 对于dp[r][i][j] 想到状态转移方程 
` dp[r][i][j] = max(dp[r-1][k1+i][k2+j]) + (grid[r][i] + grid[r][j]),  k1,k2 = -1, 0 ,1 `
**说人话**，就是针对dp[r][i][j]会有3x3，9种可能性从上一行过来。针对当前行，我们不管他上面是怎么走的，反正要想dp[r][i][j]位置获取的最多，那肯定是从上一行最多的地方过来。然后再加上这一行两个机器人所在位置的樱桃数，就是当前位置能够获取的最大数量。这样我们判断一下最后一行的最大值，就是我们想要的结果。
* 考虑边界条件，左右两个机器人，都最多只能再自己的一个三角形区域活动，且不能超过边界$$ [0,cols) $$

尝试着写一下代码。

AC!，如果dp接触不多还是需要多思考一下，理解dp的**最优子问题**和**后无效性**条件。

#### 代码
python3
```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
      rows = len(grid)
      cols = len(grid[0])
      dirs = [-1,0,1]
      dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]
      # basecase
      dp[0][0][-1] = grid[0][0] + grid[0][-1]
      for r in range(1,rows): # 行号
        for i in range(r+1): # 列号,左边机器人
          for j in range(cols-r-1, cols): # 列号,右边机器人
            for ii in dirs: # 9种组合可能性
              for jj in dirs:
                if (i < cols) and (j >= 0) \
                and (i + ii >= 0) and (i + ii < cols) \
                and (j + jj >= 0) and (j + jj < cols) \
                and (i != j):
                  dp[r][i][j] = max(dp[r-1][i+ii][j+jj] + grid[r][i] + grid[r][j], dp[r][i][j])
      result = 0
      for i in dp[-1]:
        for j in i:
          result = max(result, j)
      return result
```