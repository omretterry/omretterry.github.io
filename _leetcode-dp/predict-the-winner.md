---
layout: default
title: 预测赢家
---

## [486\. 预测赢家](https://leetcode-cn.com/problems/predict-the-winner/)

> Medium

### 方法一（记忆化递归）

#### 思路

* 题目条件可知，我们可以选择第一个数和最后一个数，最终的选择构成一个树状结构，如下图，（来自leetcode官方解题）
![](https://assets.leetcode-cn.com/solution-static/486/486_fig1.png)
* 这边有个巧妙的思路就是怎么判断是*玩家一*获胜还是*玩家二*获胜。这边使用一个总数，总数表示先手得分和后手得分之间的差。当`总分 >= 0`时表示先手获胜，反之，表示先手无法获胜

#### 代码
python3
```python
class Solution:
  def PredictTheWinner(self, nums: List[int]) -> bool:
    @functools.lru_cache(None)
    def helper(start,end):
      if start == end:
        return nums[start]
      left = nums[start] - helper(start+1,end)
      right = nums[end] - helper(start,end-1)
      return max(left,right)

    return helper(0,len(nums)-1) >= 0
```

### 方法二（动态规划）

#### 思路

记忆化递归通常可以转换成自底向上的动态规划方式来做

* 定义`dp`数组，`dp[i][j]`表示选择当前人作为先手的前提下在区间`[i,j]`中，所能获得的最大相对分数
* *相对分数*为先手分数和第二次选择的分数之差
* BaseCase：当`i == j`时，表示只能选`i`，值为`nums[i]` 
* 有了上面递归的过程，我们可以很容易推导出状态转移：
`dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])`
* 要注意的我们递推的顺序，应为要从最低层情况开始遍历，所以我们要从最大边界开始遍历

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True
        dp = [[0]*length for i in range(length)]
        for i in range(length):
            dp[i][i] = nums[i]
        for m in range(1,length): #覆盖长度
            for n in range(length-m): #i在该覆盖长度下的取值范围
                dp[n][n+m] = max(nums[n]-dp[n+1][n+m],nums[n+m]-dp[n][n+m-1])
        return dp[0][length-1]>=0
```