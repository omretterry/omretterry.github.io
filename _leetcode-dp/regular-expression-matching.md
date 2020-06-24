---
layout: default
title: 正则表达式匹配
---

## [10\. 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)

> Hard

#### 思路

抖机灵，一下想到的就是，使用正则表达式求解正则表达式。

写一下代码，AC！

#### 代码
python3
```python
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      result = re.fullmatch(p, s)
      return False if result == None else True
```

**正经解法**

这道题的正经解法，是使用**dp**来做

说一下解法思路吧，还是要细品一下，如果来给我一次机会也许我还是想不到使用**dp**来求解

* 定义一个dp数组，**dp[i][j]**代表，当index到i时的`text`,能够匹配index到j时的`pattern`
* 分析dp推导式
  * `if str[i] == pattern[j] or pattern[j] == '.':  dp[i][j]=dp[i-1][j-1]` 相同的话我们当前的结果就是之前比配的结果
  * `if pattern[j] == '*'` 分两种情况
    * 第一种情况，假如匹配空，就是说前一个字和`*`都不考虑。那就是`dp[i][j-2]`
    * 第二种情况，`if str[i] == pattern[j-1] || pattern[j-1] == '.'` 就是说，假如前一个pattern字符匹配成功，或者说是`.`代表任意字符的话，值为`dp[i-1][j]`
  * 其他情况都为`False`

如下图，我们可以用一个例子来推导一遍，验证我们的通项公式是正确的 
<img src="/public/images/regular-expression-matching-1.jpg" width="300px" height="300px" style="margin: 12px  auto"/>
<img src="/public/images/regular-expression-matching-2.jpg" width="300px" height="350px" style="margin: 12px auto"/>

尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)] 
    dp[0][0] = True
    for c in range(1, len(p) + 1):
      if p[c-1] == '*':
        dp[0][c] = dp[0][c-2]

    for i in range(1, len(s) + 1):
      for j in range(1, len(p) + 1):
        if s[i-1] == p[j-1] or p[j-1] == '.':
          dp[i][j] = dp[i-1][j-1]
        elif p[j-1] == '*':
          k = False
          if p[j-2] == s[i-1] or p[j-2] == '.':
            k = dp[i-1][j]
          dp[i][j] = k or dp[i][j-2]
    return dp[-1][-1]   

```