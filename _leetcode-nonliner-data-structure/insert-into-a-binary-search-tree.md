---
layout: default
title: 二叉搜索树中的插入操作
---

## [701\. 二叉搜索树中的插入操作](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)

> Medium

#### 思路

题目不是很难，应该可以算是一眼题了，但是首先要知道什么是二叉搜索树

`二叉搜索树`简单来说，即，对于所有节点，节点的左节点的值比当前节点的值小，右节点的值比当前的节点的值大。

所以我们只要能够需要寻找到插入的节点，就能解决这道题。使用`DFS`，比较节点的值，判断接下来应该是往左子树走还是往右子树走。

当节点没有子节点时，我们就能将目标节点插入

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    def dfs(node):
      n_node = TreeNode(val)
      if node is None:
        return
      if val < node.val:
        if node.left is None:
          node.left = n_node
        else:
          dfs(node.left)
      else:
        if node.right is None:
          node.right = n_node
        else:
          dfs(node.right)
      return
    if root is None:
      return TreeNode(val)
    dfs(root)
    return root
```