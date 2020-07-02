---
layout: default
title: 有序矩阵中第K小的元素
---

## [378\. 有序矩阵中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)

> Medium

### 方法一（降维排序）

#### 思路

首先想到的最为粗暴的方式，是将二维数组转化成一维数组，重新进行排序之后得出结果

尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
      temp = []
      for i in range(len(matrix)):
        temp += matrix[i]
      return sorted(temp)[k-1]
```

### 方法二（二分）

#### 思路

对于一个有序的数列我们可以使用二分的方式搜索目标值。

* 对于这道题目，左上角的元素是最小的，右下角的元素是最大的
* 我们取一个中间值`mid`，找到这个值是数组中的第`n`个
* 如果`n>=k`我们就找大的值，如果`n<k`我们就往较小的值找

我们这样就需要解决几个问题，一个是如何找到中间值`mid`是第几个最小的元素，另一个是边界条件

对于第一个问题我们可以参考[240. 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)的解法

对于第二个问题，我们可以通过分析边界，可调试来解决

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def findNum(self, matrix, m):
      num = 0
      i = len(matrix) - 1
      j = 0
      while i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix):
        if matrix[i][j] > m:
          i -= 1
        else:
          j += 1
          num += i+1
      return num
        
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
      start = matrix[0][0]
      end = matrix[-1][-1]

      while start < end:
        mid = start + (end - start) // 2
        n = self.findNum(matrix, mid)
        if n >= k:
          end = mid
        else:
          start = mid + 1
      return start
```