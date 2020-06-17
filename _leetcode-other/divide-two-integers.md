---
layout: default
---

## [29\. 两数相除](https://leetcode-cn.com/problems/divide-two-integers/)


> Medium


#### 思路


刚看题目第一反应直接使用python3中`//`求商并向下去整操作，商为负数情况需处理一下，但是题目要求不能使用除法运算符。过！
<br>
没有想法，学习一波大佬解法，获得新思路
* `A / B = C` => `找到一个整数T，使得B的T倍最接近A但是不超过A`
* 负数转成正数统一考虑，最后将负数符号添加
* 不能使用乘法操作，倍数操作使用`位运算`
* n >> m    =>    $$ n/2^{m} $$
* n << m    =>    $$ n * 2^{m} $$
* 倍数增长次数太多 => TLE
* 指数增长，超出之后再递归复位到1指数增长，优化增长速度

解题过程需考虑边界条件（$$ [-2^{31}, 2^{31} - 1] $$），以及除数为0的情况
<br>


#### 代码


python3
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return0
        if dividend == (0 - (2 << 30)) and divisor == \-1:
            return (2 << 30) - 1
        if (dividend > 0and divisor > 0) or (dividend < 0and divisor < 0):
            tag = 1
        else:
            tag = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = dividend
        c = 0
        while res >= divisor:
            a = 0
            while res - (divisor = 0:
                res = res - (divisor << a)
                a += 1
            if a >= 0:
                c += (2 << a - 1) - 1
        return c if tag == 1else0 - c
```
