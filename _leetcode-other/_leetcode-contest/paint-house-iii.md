---
layout: default
---

## [1473\. 给房子涂色 III](https://leetcode-cn.com/problems/paint-house-iii/)

#### 思路

根据Hard必死定律，再加上周赛dp必死定律。这道题依旧是没有做出来。但是这次做完了阅读理解，也尝试着在纸上构造了一下转态转移，也算是小有进步吧。

阅读大佬解法，获得新思路：

* 动态规划我们首先要找出状态，状态之前满足**最优子问题**和**后无效性**，确定状态转移方程，然后开始求解
* 这道题中，分析状态，主要有三个：`房子`、`颜色`、`街区`
* 构造dp数组 `dp[k][i][j]` 代表涂到第k个房子，使用颜色i，街区数量为j时的最小花费
* 遍历房子进行涂色，当前房子涂成什么颜色，是根据前边的房子来的。所以将涂到第几个房子作为第一维度。
* 假设0个房子有颜色1，`dp[0][1][1] = 0; dp[0][other][1] = math.inf` ，表示第0个房子已经涂了颜色了，不需要再涂，所以花费为0。其他的颜色无法再涂，花费为无穷大
* 假设一个房子的最小花费是无穷大，表示不可行，那也无法从这个房子进行状态转移
* **状态转移**

```python
1.当前房子有颜色
    1.dp[k][i][j] = dp[k-1][i][j] （颜色相同，街区不加，且当前房子有颜色费用为0）
    2.dp[k][i][j+1] = dp[k-1][!=i][j] （颜色不同，街区加1，当前房子有颜色，不用刷，当前费用为0）
2.当前房子没有颜色
    1.dp[k][i][j] = dp[k-1][i][j] + cost[k][i] （颜色相同，街区不加，加上刷当前的房子的费用）
    2.dp[k][i][j+1] = dp[k-1][!=i][j] + cost[k][i]（颜色不同，街区加1，加上刷当前的房子的费用）
```

以上，尝试写一下代码。

#### 代码

python3
```python
class Solution:
  def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    dp = [[[math.inf for _ in range(m+1)] for _ in range(n+1)] for _ in range(m)]
    if houses[0] != 0:
      dp[0][houses[0]][1] = 0
    else:
      for i in range(1,n+1):
        dp[0][i][1] = cost[0][i-1]
    for k in range(1, m):
      for pc in range(1,n+1): #前一个房间的颜色
        for j in range(1,m):
          if dp[k-1][pc][j] == math.inf: #已经无效，无法进行状态转移
            continue
          if houses[k] != 0: #当前房子已经涂过颜色
            if houses[k] == pc: #当前房子和前一个颜色相同，分组不加
              dp[k][houses[k]][j] = min(dp[k][houses[k]][j], dp[k-1][pc][j])
            else: #不同颜色分组加1
              dp[k][houses[k]][j+1] = min(dp[k][houses[k]][j+1], dp[k-1][pc][j])
          else:
            for c in range(1,n+1): #当前房子未涂过颜色，可以涂任意的颜色
              if c == pc: #当前颜色，不等于前一个颜色，分组不加
                dp[k][c][j] = min(dp[k][c][j], dp[k-1][pc][j] + cost[k][c-1])
              else: #不同颜色，分组加1
                dp[k][c][j+1] = min(dp[k][c][j+1], dp[k-1][pc][j] + cost[k][c-1])
    r = math.inf
    for i in range(1, n+1):
      r = min(r, dp[m-1][i][target])
    return -1 if r == math.inf else r
```