---
layout: default
title: 平衡二叉树
---

## [110\. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)

> Easy

#### 思路

* 左子树的高度是左边最深节点的深度，右边也是一样
* 使用DFS遍历左树和右树，如果左右树直接的高度超过1，就记录下来，说明是失败的
* 最终遍历结果，如果结果中有失败节点，返回`False`

#### 代码
python3
```python
class Solution:
  def isBalanced(self, root: TreeNode) -> bool:
    res = []
    def dfs(node, h):
      if node is None:
        return h
      lh = dfs(node.left, h+1)
      rh = dfs(node.right, h+1)
      if abs(lh - rh) > 1:
        res.append(False)
      else:
        res.append(True)
      return max(lh,rh)
    dfs(root,0)
    return False not in res
```