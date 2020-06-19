---
layout: default
title: 验证回文串
---

## [125\. 验证回文串](https://leetcode-cn.com/problems/valid-palindrome/)

> Easy

#### 思路

##### 方法一（暴力）
首先想到的方法是，将原字符串处理一遍。只取数字和字母。统一转换成小写字母，最后判断处理之后字符串是不是回文串

尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
      if s == '':
        return True
      ns = ''
      for i in s:
        if i.isdigit() or i.isalpha():
          ns += i.lower()
      return ns == ns[::-1]
```

##### 方法二（双指针）
方法一遍历了整个字符串，而且还是使用了额外空间存放新的字符串

我们想到回文字串是前后一致的，可以使用双指针，从两头向中间靠拢进行比较，这样遍历字数可以减少很多

尝试改进代码，AC！

#### 代码
python3
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
      if s == '':
        return True
      i,j = 0,len(s)-1
      while i < j:
        if (s[i].isdigit() or s[i].isalpha()) and (s[j].isdigit() or s[j].isalpha()):
          if s[i].lower() == s[j].lower():
            i += 1
            j -= 1
          else:
            return False
        elif not s[i].isdigit() and not s[i].isalpha():
          i += 1
        elif not s[j].isdigit() and not s[j].isalpha():
          j -= 1
        else:
          i += 1
          j -= 1
      return True
```