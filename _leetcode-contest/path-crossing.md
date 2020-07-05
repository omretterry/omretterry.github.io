---
layout: default
title: 判断路径是否相交
---

## [1496\. 判断路径是否相交](https://leetcode-cn.com/problems/path-crossing/)

> Easy

#### 思路

走一遍整个路径，记录每一个经过的坐标，如果新的坐标在之前的坐标中出现过，说明路径是相交的

以上，AC！

#### 代码
python3
```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
      cur = [0,0]
      visited = []
      visited.append(cur)
      for i in path:
        if i == 'N':
          cur = [cur[0], cur[1] + 1] 
        elif i == 'S':
          cur = [cur[0], cur[1] - 1] 
        elif i == 'E':
          cur = [cur[0] + 1, cur[1]] 
        else:
          cur = [cur[0] - 1, cur[1]] 
        print(cur)
        if cur in visited:
          return True
        visited.append(cur)
      return False
```