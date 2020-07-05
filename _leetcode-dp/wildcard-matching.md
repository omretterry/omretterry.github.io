---
layout: default
title: 通配符匹配
---

## [44\. 通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/)

> Hard

#### 思路

看到这道题，想到了之前做过的一道dp题: [10.正则表达匹配](./regular-expression-matching)

仔细阅读发现这题和之前那一题是差不多的，使用动态规划求解

* 这题中的`?`和[10.正则表达匹配](./regular-expression-matching)中的`.`是一个含义
* 这题主要的差别是`*`,这题中`*`是可以匹配任意字符串
* 定义`dp`数组，`dp[i][j]`表示`s[0:i]`和`p[0:j]`的匹配状态
* **分析状态转移** 
    * 如果当前匹配的字相同或者是`?`也就是匹配任意字符，`dp[i][j] = dp[i-1][j-1]`
    * 否则，如果当前的模式是`*`，说明当前这个可以匹配或者不匹配，假如不匹配，`dp[i][j] = dp[i][j-1]`;如果匹配任意字符，`dp[i][j] = dp[i-1][j]`
    * 如果以`*`号开头的话，默认可以匹配空字符串，即`dp[0][i] = True`

尝试写一下代码，AC!

#### 代码
python3
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)] 
      dp[0][0] = True
      for i in range(1,len(p)+1):
        if p[i-1] != '*':
          break
        dp[0][i] = True

      for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
          if s[i-1] == p[j-1] or p[j-1] == '?':
            dp[i][j] = dp[i-1][j-1]
          else:
            if p[j-1] == '*':
              dp[i][j] = dp[i-1][j] or dp[i][j-1]
      return dp[-1][-1]   
```