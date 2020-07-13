---
layout: default
title: 最佳买卖股票时机含冷冻期
---

## [309\. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

> Medium

#### 思路

这道和之前做的动态规划题稍微有点不太一样，之前做的一些题题，有的两个状态就是横坐标和纵坐标，比如，[不同路径](./unique-paths)

* 分析，动态规划的本质是分析**状态转移过程**。本题中，一个状态是确定的是**天数**。另一个状态需要我们抽象出来，买、卖、冻结，其实就是三种不同的状态，第二个状态就是**股票持有状态**，状态有三种：**持有，未持有，冻结**
* 第二个状态的转换过程，其实是一个有限状态机，如下图
    ![](/public/images/best-time-to-buy-and-sell-stock-with-cooldown-1.png)
* 定义`dp`数组
    * `dp[i][0]`表示第`i`天，未持有状态的最大利润
    * `dp[i][1]`表示第`i`天，持有状态的最大利润
    * `dp[i][2]`表示第`i`天，冻结状态的最大利润
* 根据上图中的状态转移，结合**天数**推导出**状态转移方程**
    * `dp[i][0] = max(dp[i-1][0], dp[i-1][2])`
    * `dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])`
    * `dp[i][2] = dp[i-1][1] + prices[i]`
* 最后一天取三种状态的最大值，就是我们需要的结果

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      if len(prices) is 0:
        return 0
      #三种状态
      #0：表示未持有股票状态
      #1：表示持有股票状态
      #2: 表示被冻结状态
      dp = [[-math.inf for _ in range(3)] for _ in range(len(prices))]
      dp[0][0] = 0
      dp[0][1] = -prices[0]
      dp[0][2] = 0
      for i in range(1,len(prices)):
        dp[i][0] = max(dp[i-1][0], dp[i-1][2])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        dp[i][2] = dp[i-1][1] + prices[i]
      return max(dp[-1])
```