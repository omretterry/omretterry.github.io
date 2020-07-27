---
layout: default
title: 判断子序列
---

## [392\. 判断子序列](https://leetcode-cn.com/problems/is-subsequence/)

> Easy

#### 思路

* 使用双指针方式，一个指针`i`指向`s`的开头，另一个指向`t`的开头
* 第二个指针遍历`t`,当遇到`s[i]`与当前元素相同时,`i`向后移动一位
* 当`i`移动完了之后，说明匹配成功，否则匹配失败
* 特判：当`s == ""`返回`True`

以上，AC！

#### 代码
python3
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      if s is "":
        return True
      i = 0
      for l in t:
        if s[i] == l:
          i += 1
          if i >= len(s):
            return True
      return False
```