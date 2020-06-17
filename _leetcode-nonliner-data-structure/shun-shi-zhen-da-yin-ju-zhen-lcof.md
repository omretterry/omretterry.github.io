---
layout: default
---

## [面试题29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

>Easy

#### 思路

* 按着题目理解的方式进行遍历
* 一圈分成4个步骤，代码使用 `%4` 来区分步骤
* 一圈结束后，要向内圈缩进一格
* 遍历次数为m * n

#### 代码

python3
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        r = []
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        i = 0
        j = 0
        for k in range(m * n):
            #print((i,j))
            r.append(matrix[i][j])
            if count % 4 == 0:
                if j < (n - 1 - int(count / 4)):
                    j +=1
                else:
                    i+=1
                    count += 1
            elif count % 4 == 1:
                if i < (m - 1 - int(count / 4)):
                    i +=1
                else:
                    j-=1
                    count +=1
            elif count % 4 == 2:
                if j > int(count / 4):
                    j-=1
                else:
                    i-=1
                    count +=1
            else:
                if i> int(count/4) + 1:
                    i-=1
                else:
                    j+=1
                    count +=1
        return r
```
