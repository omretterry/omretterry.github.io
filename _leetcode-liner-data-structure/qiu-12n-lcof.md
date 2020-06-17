---
layout: default
---

## [面试题64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)
>Easy

#### 思路
一眼看到题目就蹦出一句话，`首项加尾项乘以项数除以2` -- 等差数组求和公式。

题目要求不能使用乘除、条件语句，于是优先想到两种方案：
* 内置函数
* 位运算

挑个简单的，AC！
时间复杂度 $$ O(n) $$
空间复杂度 $$ O(n) $$

#### 代码
python3
```python
class Solution:
    def sumNums(self, n: int) -> int:
      return sum([x for x in range(1,n+1)])
```