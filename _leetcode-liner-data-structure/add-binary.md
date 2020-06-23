---
layout: default
title: 二进制求和
---

## [67\. 二进制求和](https://leetcode-cn.com/problems/add-binary/)

> Easy

#### 思路

*2020-06-23* 今天的周赛题终于是一眼题了，前几天唯唯诺诺，今天重拳出击！

首先想到的方法是将字符串转成数字，计算之后，再转成2进制字符串显示

python一行流，AC！

#### 代码
python3
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
      return "{0:b}".format(int(a,2) + int(b,2))
```

**不转化类型解法**

不转换类型的话，就是正常计算的方式来思考为题。我们从最后一位开始，两个都是1，就向前进一位，最后得出结果

不做尝试了，也不是很复杂，感兴趣的小伙伴可以尝试