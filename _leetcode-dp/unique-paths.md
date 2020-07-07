---
layout: default
title: 不同路径
---

## [62\. 不同路径](https://leetcode-cn.com/problems/unique-paths/)

> Medium

#### 思路

多少种可能性，多少个解，这类题我们可以考虑使用**动态规划**方式求解。

* 对于一个节点，可能是从上面的节点跳到当前节点，也可能是从左边的节点跳到当前的节点。那么对于当前节点来说，到当前节点的可能性就是上面那个节点的可能性，加上左边这个节点的可能性
* 当行号和列号为0时，只有一种可能性（只能一直往下走，或者一直往右走）我们将这两条边的值初始化为`1`

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      dp = [[ 0 for _ in range(n) ] for _ in range(m)]
      
      for i in range(m):
        dp[i][0] = 1
      for j in range(n):
        dp[0][j] = 1
      
      for i in range(1, m):
        for j in range(1, n):
          dp[i][j] = dp[i-1][j] + dp[i][j-1]
      return dp[-1][-1]
```

### 优化

由于我们求当前行的时候，只要用到上面一行的数据，所以我们至于要保留两行的数据就行了

#### 代码
python3
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      pre = [1] * n
      cur = [1] * n
      
      for i in range(1, m):
        for j in range(1, n):
          cur[j] = cur[j-1] + pre[j]
        pre = cur
      return cur[-1]
```

### 优化plus

我们用过的列只会用到本身和本身以后的上一行的列，所以我们可以直接将计算的值保存在当前行，如下图
```
pre 1 2 3 4 5
      ↑
cur 1 2 3 4 5

cur的2要用到的是pre的1+cur的1，我们只要计算后存在cur的1上就行了 
这样也就可以省略pre这个变量了
```

#### 代码
python3
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      cur = [1] * n
      
      for i in range(1, m):
        for j in range(1, n):
          cur[j] += cur[j-1]
      return cur[-1]
```