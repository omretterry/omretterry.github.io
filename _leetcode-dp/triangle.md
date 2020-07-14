---
layout: default
title: 三角形最小路径和
---

## [120\. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/)

> Medium

#### 思路

这道题和路径问题非常相似，思路和路径问题也是一样的。只不多二维数组换成了三角形。

直接梭了，AC!
#### 代码
python3
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
      dp = [ [math.inf for _ in range(len(triangle[-1]))] for _ in range(len(triangle))] 
  
      pre = 0
      for i in range(len(triangle)):
        dp[i][0] = triangle[i][0] + pre
        pre = dp[i][0]

      for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i])):
          dp[i][j] = min(dp[i-1][j] + triangle[i][j] , dp[i-1][j-1] + triangle[i][j])
      return min(dp[-1])
```

#### 从下向上DP

从下向上考察的话，对于上一个节点，要选择的子节点，肯定是下层两个节点中较小的那一个。这样有个好处是不用处理边界因素。因为下面的元素总是比上面的多

#### 代码
python3
```python
class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    dp = [[ math.inf for i in range(len(triangle[-1])) ] for _ in range(len(triangle))]
    for i,v in enumerate(triangle[-1]):
      dp[-1][i] = v

    for i in range(len(triangle) - 2, -1 ,-1):
      for j in range(len(triangle[i])):
        dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
    return dp[0][0]
```

#### 优化

使用**滚动数组**的方式进行**降维**。具体思考过程，可以参考[62.不同路径](./unique-paths)

#### 代码
python3
```python
class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    dp = [[ math.inf for i in range(len(triangle[-1])) ] for _ in range(len(triangle))]
    for i,v in enumerate(triangle[-1]):
      dp[i] = v

    for i in range(len(triangle) - 2, -1 ,-1):
      for j in range(len(triangle[i])):
        dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]
    return dp[0]
```