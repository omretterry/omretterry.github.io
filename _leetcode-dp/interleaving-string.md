---
layout: default
title: 交错字符串
---

## [97\. 交错字符串](https://leetcode-cn.com/problems/interleaving-string/)

> Hard

#### 思路

这种字符串类型的题目我们之前做过几道，使用动态规划的方式来求解。这道题同样也从动态规划的角度来思考问题

* 大体的思路如图，[图片来自gousiqi的leetcode解题](https://leetcode-cn.com/problems/interleaving-string/solution/lei-si-lu-jing-wen-ti-zhao-zhun-zhuang-tai-fang-ch/)
![](https://pic.leetcode-cn.com/5b5dc439d4ec4bdb35a68607a86558ff8b820e70726eeaf4178dc44a49ea9a33-image.png)
* `target`字符串如果是交替去拿`s1`和`s2`中的字串，就说明是*交错字符串*。这样的话也就是说如果能在图中，有一条，向右向下走的路线，能够走到右下角，说明就是*交错字符串*
* 定义dp数组，`dp[i][j]`表示`s1`到第`i`位置，和`s2`到`j`位置，是否能交替组成`s3[0:i+j]`
* 分析状态转移方程：
    * `dp[i][j] = dp[i-1][j] and s3[i+j-1] is s1[i-1]` 表示我们可以继续选择`s1`来组到`target`
    * `dp[i][j] = dp[i][j-1] and s3[i+j-1] is s2[j-1]` 表示我们可以选择`s2`来组到`target`
* BaseCase: 当`i=0`是，表示只能选`s2`,那么就必须保证，`s2[j] == s3[j]`,如果不一样后面的都走不通，即后面的都为`False`；相反对于`s1`也是一样的

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
      l1 = len(s1)
      l2 = len(s2)
      if l1 + l2 != len(s3):
        return False
      dp = [[ False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
      dp[0][0] = True
      for i in range(1,l1 + 1):
        dp[i][0] = dp[i-1][0] and s1[i-1] is s3[i-1]
      
      for j in range(1,l2 + 1):
        dp[0][j] = dp[0][j-1] and s2[j-1] is s3[j-1]

      for i in range(1,l1 + 1):
        for j in range(1,l2 + 1):
          if s1[i-1] is s3[i+j-1] and dp[i-1][j] is True:
            dp[i][j] = True
          elif s2[j-1] is s3[i+j-1] and dp[i][j-1] is True:
            dp[i][j] = True
      return dp[-1][-1]
```