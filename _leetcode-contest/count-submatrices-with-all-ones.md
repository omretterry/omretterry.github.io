---
layout: default
title: 统计全 1 子矩形
---

## [1504\. 统计全 1 子矩形](https://leetcode-cn.com/problems/count-submatrices-with-all-ones/)

> Medium

#### 思路

刚拿到这道题，首先想到，如果说我们能够找到一个大的矩形的话，那我们其实是可以知道这个矩形中的子矩阵的个数的。但是这个题目中，我们使用遍历的方式不太方便。因为一行中有多个，直接找到最大的矩阵有点麻烦。

获取大佬思路使用**统计加压缩**，先一行一行的统计，然后我们进行压缩，接着统计大一行的矩形的个数，如下图：
![](/public/images/count-submatrices-with-all-ones-1.png)

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def numSubmat(self, mat: List[List[int]]) -> int:
    r = len(mat)
    c = len(mat[0])
    self.res = 0

    def count(i):
      num = 0 
      for j in range(c):
        if mat[i][j] == 0:
          self.res += (num + 1) * num // 2
          num = 0
        else:
          num += 1 
      self.res += (num + 1) * num // 2

    def downzip():
      temp = [[0 for _ in range(c)] for _ in range(r)]
      for i in range(1,r):
        for j in range(c):
          temp[i][j] = mat[i][j] & mat[i-1][j]
      return temp

    for k in range(r):
      for i in range(k,r):
        count(i)
      mat = downzip()

    return self.res
```