---
layout: default
title: 最多的不重叠子字符串
---

## [1520\. 最多的不重叠子字符串](https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-substrings/)

> Medium

#### 思路

参考了大佬们的思路

* 首先找出所有字母的范围，也就是说某个字母第一次出现和最后一次出现的位置。这样可以保证字符中所有的这个字母都是存在于这个范围中的
* 但是这个区间不能直接拿来使用，应为这个区间中如果包含了别的字符，而且其他字符的范围更广的话，我们需要扩展当前字符的范围
* 通过这个过程我们可以发现，这些区间只有包含的关系没有交叉的关系，应为如果是交叉的说明，还是有范围没有扩展
* 使用**贪心**，当我们左边为基准的时候，这个有边界尽量的小，就是我们需要的最小的一个范围。都取最小的范围，就能保证我们范围的个数最多

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
      chars = {}
      for i,c in enumerate(s):
        if c not in chars:
          chars[c] = [i,i+1]
        else:
          chars[c][1] = i+1
      #扩展字母的范围
      lrange = []
      for start, end in chars.values():
        i = start + 1
        max_end = end
        while i < max_end:  # 不断往后拓展区间，以满足条件 2
          if chars[s[i]][0] < start:  # 不往前拓展
            break
          max_end = max(max_end, chars[s[i]][1])
          i += 1
        else:
          lrange.append([start, max_end])

      lrange.sort()
      prer = [0, 0]
      res = []
      for r in lrange:
        left,right  = r[0], r[1]
        if right <= prer[1] and len(res):
          res.pop(-1)
        res.append(s[left:right])
        prer = [left, right]
      return res
```