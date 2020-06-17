---
layout: default
---

## [检查一个字符串是否包含所有长度为 K 的二进制子串](https://leetcode-cn.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)

#### 思路
* 当看到这道题，最开始蹦出来的想法是：根据长度K生成所有可能的二进制字符串。再遍历这些字符串，判断是不是存在于string中。这样显然不是很好，应为K的长度是不可控的，题目限定最大值为20，即最多`$ 2^{20} $`。
* **更换思路**，一共两个变量，s和k。那换个维度，从s角度入手。遍历s，拿出所有长度为k的字串，判断是不是都包含所有k长的二进制字符串
* 如何判断呢？从s中拿出字串有很多重复，要排除重复自然想到用hashmap存放。既然排除了重复就没必要比较内容了，我们只要判断所有没有重复的字串的个数是不是k能生成所有可能性的个数就好了
AC！

#### 代码
python3
```
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
      m = set()
      for i in range(len(s)-k+1):
        m.add(s[i:i+k])
      return len(m) == (1 << k)
```