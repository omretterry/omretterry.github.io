---
layout: default
title: 矩阵中的最长递增路径
---

## [329\. 矩阵中的最长递增路径](https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/)

> Hard

#### 思路

* 从每个点出发，下一个节点的选择有四个方向，四种可能性
* 选择下一个节点之后又有四种可能性，形成一个树状结构，使用DFS递归求解
* 递归终止条件为：1.遇到边界情况不能再走；2.不满足递增，即下一个节点<=当前节点
* 每一个的点都可以作为起点，所以要遍历数组

以上，尝试写一下代码，TLE！

* 实际运行过程中发现很多重复运算。比如示例1中的答案为`[1, 2, 6, 9]`，当计算`6`时，计算了`[6,9]`;计算`2`时，计算了`[2,6,9]`。

引入记忆化递归优化，AC！

#### 代码
python3
```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
      @functools.lru_cache(None)
      def helper(x,y,r,c):
        cur = matrix[x][y]
        dises = [1]
        for d in dirs:
          cx = x + d[0]
          cy = y + d[1]
          if cx >= 0 and cx < r and cy >= 0 and cy < c:
            if matrix[cx][cy] > cur:
              dises.append(helper(cx,cy,r,c)+1)
        return max(dises)

      dirs = [(0,1),(0,-1),(-1,0),(1,0)]
      if matrix == []:
        return 0

      r = len(matrix)
      c = len(matrix[0])
      dis = 0
      for i in range(r):
        for j in range(c):
          dis = max(dis,helper(i,j,r,c))
      return dis
```