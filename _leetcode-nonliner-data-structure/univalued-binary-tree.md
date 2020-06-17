---
layout: default
---

## [965\. 单值二叉树](https://leetcode-cn.com/problems/univalued-binary-tree/)

>Easy

#### 思路

判断有没有其他数字，那肯定就是要遍历二叉树。记录节点值，判断当前节点是否与其他的节点不同。遍历二叉树，也就是深度优先和广度优先，这边选用DFS。

尝试写一下代码，AC！

#### 代码

python3
``` python
class Solution:
  def dfs(self, val, node):
    if node is None:
      return True
    if node.val != val:
      return False
    return self.dfs(val, node.left) and self.dfs(val, node.right)

  def isUnivalTree(self, root: TreeNode) -> bool:
    if root is None:
      return True
    val = root.val
    return self.dfs(val, root) 
```