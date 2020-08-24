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


### 方法三（Manacher马拉车）

#### 思路

阅读大佬解题获得新思路，`Manacher算法`，俗称`马拉车`
它可以*线性的查找一个字符串的最长回文字串*


相关文档：
> [https://www.cxyxiaowu.com/2665.html](https://www.cxyxiaowu.com/2665.html)

上边的文章讲的讲的相当清晰，基本仔细阅读一遍理解上应该没什么问题，写的非常详细。

回到这道题目:
* 按着*马拉车*的流程走一下，首先构造分割符
* `maxRight` 用于记录当前最右侧的边界，`i`表示当前的对称轴
* **注意**重要的也是马拉车的关键代码为`p[i] = min(p[mirror], maxRight - i + 1)`，需要结合上边的教程理解
* 最后得出每个点的`最长回文字串`，既可以的到最后的结果

以上，尝试写一下代码，AC！（边界搞死人，建议多在草稿纸上画图）

#### 代码
python3
```python
class Solution:
  def initMString(self, s): 
    return '$#' + '#'.join(s) + '#&'
  def countSubstrings(self, s: str) -> int: 
    ms = self.initMString(s)
    maxRight = 0
    center = 0
    p = [1] * (len(ms)-1)
    ans = 0

    for i in range(1, len(ms)-1):
      # 马拉车 核心代码
      if i <= maxRight:
        mirror = center * 2 - i
        p[i] = min(p[mirror], maxRight - i + 1)

      # 扩展左右边界
      left = i - p[i]
      right = i + p[i]

      while ms[left] == ms[right]:
        left -= 1
        right += 1
        p[i] += 1

      if i + p[i] - 1 > maxRight:
        maxRight = i + p[i] - 1
        center = i
      ans += p[i] // 2

    return ans
```