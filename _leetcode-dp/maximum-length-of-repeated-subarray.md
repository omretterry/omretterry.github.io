---
layout: default
title: 最长重复子数组
---

## [718\. 最长重复子数组](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/)

> Medium

#### 思路

这道是一道非常经典的dp题，做这道题的时候，刚看完最长公共字串问题，做这道题的时候被绕进去了。dp题还是要多想一想，想明白状态转移，代码部分写起来就很快了

* 设置dp数组，`dp[i][j]`表示比较的公共子数组以`A[i]`结尾和以`B[j]`结尾时的最长长度
* 当`A[i]`和`B[j]`相同时，公共字串的长度为最后一个字之前的匹配的结果+1
* 当`A[i]`和`B[j]`不相同时，直接为0，应为需要连续的字串，如果不相同，也就不能增加长度了
* 总结出状态转移方程：
$$dp[i][j] = dp[i-1][j-1] + 1 if A[i] == B[j]$$
$$dp[i][k] = 0 if A[i] != b[j]$$

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
      dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
      r = 0
      for i in range(1, (len(A) + 1)):
        for j in range(1, (len(B) + 1)):
          if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            r = max(r, dp[i][j])
      return r
```