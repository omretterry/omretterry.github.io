---
layout: default
title: 地下城游戏
---

## [174\. 地下城游戏](https://leetcode-cn.com/problems/dungeon-game/)

> Hard

### 方法一（记忆化递归）

#### 思路

这种题目第一眼感觉是可以用动态规划来做。很多dp我们可以先使用递归的思考方式先做，然后转换成bottom-up的动态规划比较方便

先使用递归方法思考问题。使用递归方式，我们从上到下的方式思考，考虑首先要解决什么问题，然后在把子部分，作为主体往下解决

* 对于这道题目，我们选择的路线有两个，一个是向右走，一个向下走 
* 为了保证后面的格子能走的下去，`当前血量 + 这个点的变化值 = 下个点的血量`，
    * 假如往右走，稳妥血量即为`右边的区域的稳妥血量 - dungeon[i][j]`
    * 假如往下走，稳妥血量为`下边的区域的稳妥血量 - dungeon[i][j]`
* 右边区域的值就是接着递归上面的过程
* 假如`后边的区域 - dungeon[i][j] < 1`说明，只要1滴血过来也肯定够，当前加的血就够后面用了，直接返回1。（0是错误的，应为至少要有一点血）
* **递归终止条件** 当走到最后一个格子时，结束递归，
    * `dungeon[i][j] > 0` 返回 `1` 保证最小血量过来就行了
    * `dungeon[i][j] <= 0` 返回 `1 - dungeon[i][j]` 这样过来的血量过来在加上当前的血量，就还是会有1点血

以上，尝试写一下代码，TLE

过程中有很多的重复计算，路径的选择形成了一颗二叉树，但是中间有很多都是已经计算过了。

使用记忆化递归优化，AC！

#### 代码
python3
```python
class Solution:
  def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    r = len(dungeon) - 1 
    c = len(dungeon[0]) - 1
    @functools.lru_cache(None)
    def dfs(i,j):
      if i == r and j == c:
        #如果说要到终点的话，需要带着1-dungeon[i][j]的血量才不会死
        return 1 - dungeon[i][j] if dungeon[i][j] < 0 else 1
      down, right = math.inf,math.inf
      #没到最后一行，就能往下走
      if i < r:
        down = dfs(i+1,j)
      #没到最后一列，可以往右走
      if j < c:
        right = dfs(i,j+1)
      if down < right:
        if down - dungeon[i][j] < 1 :
          return 1
        else:
          return down - dungeon[i][j]
      else:
        if right - dungeon[i][j] < 1:
          return 1
        else:
          return right - dungeon[i][j]
    r = dfs(0,0)
    return r
```

### 方法二（动态规划）

#### 思路

使用动态规划方式来思考这道题。通过上边递归的方式其实我们可以看到，**前面的最小健康值是取决于后面的元素**

换个角度，从起点开始进行状态转移，开头的健康值是不能确认的。但是从终点考虑的话，可以确定终点的血量一定是`1`（原因是要保证血量最小完成）

于是我们可以从终点开始考虑状态转移

* 定义dp数组，`dp[i][j]` 表示`(i,j)`位置能够保证走通的最小血量
* 那么对于中间的某个点来说，最小血量为，从下面过来的和从右边过来的较小的那个值再减当前值，即`dp[i][j] = min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j]`
* 想象一下，假如数字都是正数，那最小血量为`1`，这部分和递归的思考过程是一样的
* 设置Basecase，从而让终点也满足状态转移方程。`dp[-1][-2] = 1, dp[-2][-1] = 1`

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    r = len(dungeon)
    c = len(dungeon[0])
    dp = [[ math.inf for _ in range(c + 1)] for _ in range(r + 1)]
    dp[-1][-2] = 1
    dp[-2][-1] = 1
    for i in range(r-1, -1 ,-1):
      for j in range(c-1, -1, -1):
        m = min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j]
        if m < 1:
          dp[i][j] = 1
        else:
          dp[i][j] = m
    return dp[0][0]
```