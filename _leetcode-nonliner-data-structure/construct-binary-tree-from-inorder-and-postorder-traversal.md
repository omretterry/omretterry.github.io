---
layout: default
title: 从中序与后序遍历序列构造二叉树
---

## [106\. 从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

> Medium

#### 思路

首先，要理解中序与后序的遍历区别：
    中序：`前-中-后`
    后序：`前-后-中`
构造一棵树的话，我们必须要确定根节点，然后确定左子树的元素和右子树的元素。同理，子问题也是这样，递归求解。

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

    def helper(cur, start, end):
      if start >= end:
        return None
        
      node = TreeNode()
      for p in range(cur - 1, -1 , -1):
        if postorder[p] in inorder[start:end]:
          i = inorder.index(postorder[p])
          node.val = postorder[p]
          break
      
      node.left = helper(cur - 1, start, i)
      node.right = helper(cur - 1, i+1, end)
      return node

    return helper(len(postorder), 0, len(postorder))
```