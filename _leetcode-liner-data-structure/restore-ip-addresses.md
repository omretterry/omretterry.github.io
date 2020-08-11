---
layout: default
title: 复原IP地址
---

## [93\. 复原IP地址](https://leetcode-cn.com/problems/restore-ip-addresses/)

> Medium

#### 思路

不同类型的题目还是要反复做一做，太久没有做回溯的题，这道题做的时候稍微就有点费劲了

* 对于一个ip地址的字符串来说，我们要把这个字符串分为4段。每段的数字是`0-255`，那么我们可以截取`[1-3]`，长度的字符，再将不合要求的去除。借用李威威大佬解题中的图来说明
![](https://pic.leetcode-cn.com/b581bdde1cef982f0af3182af17fc3c41960c76a7445af0dcfd445c89b4c2eaa-%E3%80%8C%E5%8A%9B%E6%89%A3%E3%80%8D%E7%AC%AC%2093%20%E9%A2%98%EF%BC%9A%E5%A4%8D%E5%8E%9F%20IP%20%E5%9C%B0%E5%9D%80-1.png)
* 使用回溯算法。常规操作定义一个`helper`方法
    * `s`: 需要处理的字符串
    * `begin`: 此次节点开始选择数字的在`s`中的起始位置
    * `path`: 记录到当前节点的路径（回溯常规变量）
    * `cnt`: 当前已经分了多少个区域了，ip地址是四个区域，这个也是我们的终止递归需要判断的条件
    * `res`: 用于记录符合条件的路径

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def helper(self, s, start, cnt, path, res):
      if cnt > 4:
        return
      elif cnt == 4:
        if start == len(s):
          res.append('.'.join(path))
        return
      for i in range(1,4):
        if start+i > len(s):
          break
        sub = s[start:start+i]
        if len(sub) > 1 and sub.startswith('0'):
          return
        if int(sub) > 255:
          return
        path.append(sub)
        self.helper(s,start+i, cnt+1, path, res)
        path.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
      res = []
      self.helper(s, 0, 0, [], res)
      return res
```
