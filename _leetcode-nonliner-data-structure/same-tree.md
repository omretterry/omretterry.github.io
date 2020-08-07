---
layout: default
title: 相同的树
---

## [100\. 相同的树](https://leetcode-cn.com/problems/same-tree/)

> Easy

#### 思路

遍历树，比较两棵树的子树

* 思路很清晰，这边我们使用DFS方法来求解
* 树1的左子树比较树2的左子树，树1的右子树比较树2的右子树，向下递归
* **递归终止条件** 当需要比较的两个节点中有一个节点为`None`时无法向下递归，递归终止。
    * 两个节点都为`None`时，说明遍历了所有节点，且当前节点也相同，返回`True`
    * 两个节点中如果有一个节点为`None`，另一个节点不为`None`，说明最终节点不相同，返回`False`

以上，尝试一下代码，AC！

#### 代码
python3
```python
class Solution:
    def helper(self, node1, node2):
      if node1 is None and node2 is not None:
        return False
      elif node2 is None and node1 is not None:
        return False
      elif node1 is None and node2 is None:
        return True
      if node1.val != node2.val:
        return False
      return self.helper(node1.left, node2.left) and self.helper(node1.right ,node2.right)
      
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
      return self.helper(p,q)
```