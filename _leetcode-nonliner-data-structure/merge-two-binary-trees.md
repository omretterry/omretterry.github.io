---
layout: default
title: 合并二叉树
---

## [617\. 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees/)

> Easy

#### 思路

合并两个二叉树，我们想到可以使用相同的方式同时遍历两棵树

需要处理一下，一个节点为空，另一个节点有值的情况即可。这边选择使用DFS方式遍历

以上，尝试写一下代码，AC！

#### 代码
python3
```python 
class Solution:
  def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    def dfs(node1, node2):
      if node1 is None and node2 is None:
        return None
      val = 0
      if node1 is not None:
        val += node1.val
      if node2 is not None:
        val += node2.val
      node = TreeNode(val)
      node1_left = node1.left if node1 is not None else None 
      node2_left = node2.left if node2 is not None else None 
      node1_right = node1.right if node1 is not None else None 
      node2_right = node2.right if node2 is not None else None 
      
      node.left = dfs(node1_left, node2_left)
      node.right = dfs(node1_right, node2_right)
      
      return node
    return dfs(t1,t2)
```