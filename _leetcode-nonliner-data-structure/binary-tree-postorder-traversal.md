---
layout: default
title: 二叉树的后序遍历
---

## [145\. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)

> Medium

#### 思路

这道题的难度感觉定的有点高了

二叉树的DFS遍历顺序可以分为三种：
    * 前序： `中-左-右`
    * 中序： `左-中-右`
    * 后序： `左-右-中`

这个是二叉树遍历的基础知识，前中后代表的是中间节点的位置。

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
      res = []
      def dfs(node):
        if node is None:
          return 
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
        return
      dfs(root)
      return res
```