---
layout: default
title: 跳水板
---

## [面试题 16.11\. 跳水板](https://leetcode-cn.com/problems/diving-board-lcci/)

> Easy

#### 思路

* 首先想到的是，每次选择我们可以选择，有两种选择：可以选长的那块，也可以选短的那块
* 那我们每一次的选择都有两种可能性
* 总共要选k次

很明显，每次选择形成了一个二叉树，我们可以使用递归来做

#### 代码（TLE）
python3
```python
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
      r = []
      def dfs(t, res):
        if res <= 0:
          r.append(t)
          return 
        dfs(t + shorter, res - 1)
        dfs(t + longer, res - 1)
      dfs(0,k)
      return list(set(r))
```

### 改进

上面方法TLE了，我们可以发现其中有很多的重复计算：`选了1，再选2 和 选了2，再选1`对于结果来说是一样的

其中就有很多重复计算，而且`k`的范围是`0 <= k <= 100000`,这个二叉树的规模显然是不能直接使用递归来做的

**换种思路**

* 最小的可能性肯定是`shorter * k`
* 最大的可能性为`longer * k`
* 我们可以定义dp数组，`dp[i]`表示`k`中有`i`个长板子
* 那么**状态转移方程**为`dp[i] = dp[i-1] + longer - shorter  , i = [0,k]`
* Base Case: `dp[0] = shorter * k`
* 特殊情况考虑：
    * `k == 0`的话，直接返回空数组
    * `shorter == longer`，返回`[shorter * k]`

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
      if k is 0:
        return []
      if shorter is longer:
        return [shorter * k]
      dp = [] * k
      dp[0] = shorter * k
      for i in range(1,k+1):
        dp[i] = dp[i-1] + longer - shorter
      return dp
```