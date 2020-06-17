---
layout: default
---

## [166\. 分数到小数](https://leetcode-cn.com/problems/fraction-to-recurring-decimal/)


> Medium


#### 思路


阅题，第一反应先计算出小数，看了眼实例，有限小数没问题，无限小数这种方式做不到。

假如说把保留小数位数拉长呢？比如，1.66666667，6个数超过10个把他处理成循环主体，转成1.(6)。但是不严谨且循环主体很长的话无法判断，过！

又是数学题？google一下，获得新思路

做一个长除法，就是我们小学在纸上计算的那种方式，当余数相同时，则产生循环，如图：![](/public/images/fraction-to-recurring-decimal-1.png)

* 符号问题记录，最后再处理
* 分子分母为0的情况需处理

#### 代码


python3
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
      tag = 1 if numerator * denominator > 0 else -1
      if numerator * denominator == 0:
        return '0'
      numerator = abs(numerator)
      denominator = abs(denominator)   
      result = ''
      # 整数部分
      v = numerator // denominator
      n = numerator % denominator # 余数
      if n == 0:
        return result + str(v) if tag > 0 else '-' + result + str(v)
      result += str(v) + '.'     
      
      # 小数部分
      n_cache = []
      v_cache = []
      while n not in n_cache and n != 0:
        v = n * 10 // denominator
        n_cache.append(n)
        n = n * 10 - (v * denominator)
        v_cache.append(v)
      if n is 0:
        result += ''.join(str(x) for x in v_cache)
      else:
        result += ''.join(str(x) for x in v_cache[:n_cache.index(n)]) \
        + '(' + ''.join(str(x) for x in v_cache[n_cache.index(n):]) + ')'
      return result if tag > 0 else '-' + result
```
