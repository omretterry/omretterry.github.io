---
layout: default
title: 二叉树的最大深度
---

## [104\. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

> Easy

#### 思路

* 二叉树分左子树和右子树，我们只要计算左右子树中深度比较大的那个作为结果返回即可
* 很明显是**DFS递归求解**向下走一层，深度`+1`
* 递归终止条件为，节点为`None`表示到了根节点了，返回`0`

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def helper(self, node):
      if node == None:
        return 0
      left_depth = 1 + self.helper(node.left)
      right_depth = 1 + self.helper(node.right)
      return max(left_depth,right_depth)

    def maxDepth(self, root: TreeNode) -> int:
      return self.helper(root)
```