---
layout: default
title: 子矩阵查询
---

## [1476\.子矩阵查询](https://leetcode-cn.com/problems/subrectangle-queries/)

#### 思路

本题主要就是更新二维数组中值的操作

使用暴力方法，知道了范围，使用双for暴力，更新范围内的所有内容，即可

尝试写一下代码，AC！

#### 代码
python3
```python
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
      self.m = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
      for i in range(row1,row2+1):
        for j in range(col1,col2+1):
          self.m[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
      return self.m[row][col]
```