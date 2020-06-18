---
layout: default
title: 汉明距离
---

## [461\. 汉明距离](https://leetcode-cn.com/problems/hamming-distance/)

> Easy

#### 思路

题目要求统计，二进制不相同的数量。

首先想到的方法是：1.转成二进制 2.然后在转成字符串 3.逐字遍历比较

感觉有点麻烦，再想一下

转成二进制了之后，**异或**操作，位数是1的，就是说明两数的相同位置的二进制数是不相同的。

尝试写一下代码，AC！

#### 代码

python3
```python
class Solution:
  def hammingDistance(self, x: int, y: int) -> int:
    return bin(x^y).count('1')
```