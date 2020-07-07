---
layout: default
title: 路径总和
---

## [112\. 路径总和](https://leetcode-cn.com/problems/path-sum/)

> Easy

#### 思路

首先阅读理解，我们需要寻找出一条路径使这个路径的和等于`sum`

一眼就是使用DFS来遍历二叉树，然后同时得到路径的和与`sum`做比较。我们可以初始给`sum`，然后向下遍历的过程中逐步减去当前节点的值。

如果值变成`0`,说明所经过的路径的节点和恰好是`sum`

**注意**题目要求是到根节点。也就是说当数值变成`0`时，也需要保证当前节点是最后一个节点。也就是说左右子节点都为空

以上，AC！

#### 代码
python3
```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
      def dfs(node,t):
        if node is None:
          return False
        t -= node.val
        if t is 0 and node.left is None and node.right is None:
          return True
        return dfs(node.left,t) or dfs(node.right,t)
      return dfs(root,sum)
```