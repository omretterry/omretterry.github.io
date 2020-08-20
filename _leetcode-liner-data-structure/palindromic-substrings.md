---
layout: default
title: 回文子串
---

## [647\. 回文子串](https://leetcode-cn.com/problems/palindromic-substrings/)

> Medium

### 方法一（暴力）

#### 思路
* 使用双指针的方式进行回文字符串的判断
* 遍历字符串取出所有子字符串，进行判断，最后返回结果

尝试一下代码，C++：AC！，python3：TLE！

#### 代码
C++
```cpp
class Solution {
public:
    bool isPalindromic(string s) {
      int i = 0;
      int j = s.size() - 1;
      while(i<j){
        if (s[i] == s[j]){
          i++;
          j--;
        } else {
          return false;
        }
      }
      return true;
    }

    int countSubstrings(string s) {
      int res = 0;
      for (int l = 1; l<=s.size(); ++l){
        for (int i = 0; i<=s.size()-l; ++i) {
          if (isPalindromic(s.substr(i,l))) {
            res ++;
          }
        }
      }
      return res;
    }
};
```

### 方法二（中心扩展法）

#### 思路

* 回文字符串的特点是轴对称，即选中一个中点之后向两边扩展的字符都是相同的，如果不同则不是回文字符串
* 回文字符串长度是奇数的情况下，中点是单独的字符
* 回文字符串长度是偶数的情况下，中点介于两个字符中间
* 两种情况分别遍历计算一下，得出结果
* 时间复杂度$$O(n^2)$$

尝试一下代码，AC！

#### 代码
python3
```python
class Solution:
  def countSubstrings(self, s: str) -> int:
    res = 0
    #回文串长度为偶数
    for i in range(len(s)):
      k,j = i,i
      while k >= 0 and j < len(s):
        if s[k] == s[j]:
          res += 1
        else:
          break
        k -= 1
        j += 1
    #回文串长度为奇数
    for i in range(len(s)-1):
      k,j = i, i + 1
      while k >= 0 and j < len(s):
        if s[k] == s[j]:
          res += 1
        else:
          break
        k -= 1
        j += 1
    return res
```
