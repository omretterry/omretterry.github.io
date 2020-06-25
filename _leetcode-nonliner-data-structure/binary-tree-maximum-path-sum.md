---
layout: default
title: 二叉树中的最大路径和
---

## [124\. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)

> Hard

#### 思路

先进行**阅读理解**

从一个节点出发，走到另一个节点。返回这个路径的和的最大值。最少节点个数为一个，也就是说单独的一个节点的数值也可以作为结果。

但是要注意的点是，我们走路径时节点是不能重复走的。这点很重要，如下图：
![](/public/images/binary-tree-maximum-path-sum-1.png)

如果选了黄色的子树部分，就不能选择绿色了，即使绿色的值在大也是走不到的。

* 首先肯定要遍历树，两种方式：DFS、BFS。
* 这道题，节点直接寻找路径，使用BFS有点麻烦，应为层序一般只考虑层级，如果要考虑父子关系还要将父级信息一起存在队列中，相对麻烦。选择BFS来做
* 我们是以某个单独节点作为root，那么针对这个单独的节点，有几种情况：
    * 当前最大
    * 当前节点加左子树最大
    * 当前节点加右子树最大
    * 当前节点加左子树加右子树最大（这种情况就要考虑上图的情形，不能作为父级的子节点计算的）

尝试写一下代码

#### 代码
python3
```python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
      def dfs(node):
        if node is None:
          return 0
        left = dfs(node.left)
        right = dfs(node.right)
        # 前三种情况、
        # >> 后面提到的优化块
        cont = max(node.val, node.val + left, node.val + right)
        # 第四种情况，记录到结果当中，不会在走递归了
        self.r = max(self.r, node.val + max(0,left) + max(0,right))
        return cont
        # >>  

      if root is None:
        return 0
      self.r = float('-inf')
      dfs(root)
      return self.r
```

**优化：** 上面的`# >>`代码块，也可以进行优化，可改为一下代码，看上去更简洁，但是要细想一下才能理解
```python
    self.r = max(self.r, node.val + max(0,left) + max(0,right))
    return node.val + max(0, left, right)
```