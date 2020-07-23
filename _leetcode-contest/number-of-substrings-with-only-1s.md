---
layout: default
title: 仅含 1 的子串数
---

## [1513\. 仅含 1 的子串数](https://leetcode-cn.com/problems/number-of-substrings-with-only-1s/)

> Medium

#### 思路

看数据规模，可以判断代码的时间复杂度控制在`O(n)`。

* 当遇到`1`时，移动窗口的右边界，窗口即连续`1`的区域
* 当遇到`0`时，得到窗口的大小也就是统计`1`的个数
* 连续的`1`的序列中子串的个数，也就是$$sum(1...n)$$，这个演算一下就可以理解，这边不过多解释了

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def numSub(self, s: str) -> int:
      i = 0
      j = 0
      res = 0
      for i in range(len(s) + 1):
        if i == len(s) or s[i] == '0':
          res += ((i-j) * (i-j+1) // 2) % (10**9+7)
          j = i + 1
      return res
```