---
layout: default
---

## [9\. 回文数](https://leetcode-cn.com/problems/palindrome-number/)

>Easy

#### 思路

首先理解什么是回文，回文的意思是，反过来读和正着读是一样的，那我们按照这个思路写出代码，AC！

#### 代码

python3

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
      return str(x) == str(x)[::-1]
```

题目要求不转成字符串来解题，那我们需要用数学的方法来进行操作


**更新思路** 
* 负数前面有符号，不可能形成回文数，直接返回
* 能被10整除的数，即末尾有0的数，不能形成回文数，数字的开头不可能为0
* 上述条件排除数字0，0可以被10整数，但他也是回文数
* 使用取模操作获取最后一个数字。如`12%10=2`
* 将最后一个数乘上10再加上新来的数字，即可反转。

```python
12 % 10 = 2
1 % 10 = 1
2 * 10 + 1 = 21
```

* 不需要整个都比较，我们比较一半的数字就可以了，所以每次操作，都将原来的数字去除反转的数字
* 基数长度的数字中间的不需要比较，偶数长度就是正常比较对半的数字
综上，尝试写一下代码，AC！

#### 代码

python3

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
      if x < 0 or (x%10 == 0 and x != 0):
        return False
      res = 0
      while x > res:
        res = res * 10 + x % 10
        x //= 10
      return x == res or x == res//10
```