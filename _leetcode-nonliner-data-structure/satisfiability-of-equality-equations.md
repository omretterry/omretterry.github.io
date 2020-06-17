---
layout: default
---

## [990\. 等式方程的可满足性](https://leetcode-cn.com/problems/satisfiability-of-equality-equations/)

>Medium

#### 思路

**首先还是一样，阅读理解** 先看等式，`a==b , b==c` 从此，我们可以得到隐藏的条件`a == c`，这时假如数组中有`a != c`，那就是矛盾的。

* 可以想到，我们可以将相等连接的元素即`==`符号链接的元素，形成一个树状结构
* 这时在树状结构的路中，有一个矛盾的内容，也就是`!=`符号连接，那就返回`false`
* 组成链路，我们想到用并查集方法
* 遍历两次数组，一次构建连接树，一次查找

综上，AC！

#### 代码

python3
```python
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
      class UnionFind():
        def __init__(self, equations):
          self.s = {}
          for e in equations:
            self.s[e[0]] = e[0]
            self.s[e[3]] = e[3]
        
        def find(self, x):
          while x != self.s[x]:
            x = self.s[x]
          return x

        def union(self, a ,b):
          if self.find(a) != self.find(b):
            self.s[self.find(a)] = self.find(b)

      uf = UnionFind(equations)
      for e in equations:
        if e[1] != "!":
          uf.union(e[0], e[3])
      for e in equations:
        if e[1] == "!":
          if uf.find(e[0]) == uf.find(e[3]):
            return False
      return True
```