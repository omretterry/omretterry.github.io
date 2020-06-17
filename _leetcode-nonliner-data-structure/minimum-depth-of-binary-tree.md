---
layout: default
---

## [111\. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)


>Easy


#### 思路


* 求最小的深度，那我们自然想到使用层序遍历，使用广度优先算法。
* 碰到第一个没有子元素的节点，说明是就是最近的子节点。
* 每向下走一层，记录一下层号。
* 没有子节点，结束遍历，返回结果

综上，尝试写一下代码，AC！

#### 代码


python3
```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
      if root is None:
        return 0
      queue = [{'item':root,'depth': 1}]
      while len(queue):
        node = queue[0]['item']
        depth = queue[0]['depth']
        del queue[0]
        if node.left is None and node.right is None:
          return depth
        if node.left is not None:
          queue.append({'item':node.left,'depth': depth + 1})
        if node.right is not None:
          queue.append({'item':node.right,'depth': depth + 1})
      return 0
```