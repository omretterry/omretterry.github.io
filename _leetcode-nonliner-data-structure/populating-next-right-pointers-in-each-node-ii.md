---
layout: default
title: 填充每个节点的下一个右侧节点指针 II
---

## [117\. 填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)

> Medium

#### 思路

首先，我们想到如果要操作二叉树中的每一个一点，必须要遍历这整个二叉树。两种方式：BFS、DFS

题目要求我们同行的节点串联起来，这边肯定需要使用`BFS`。使用BFS遍历，相同层高的节点进行关联

注意对空树进行特判

以上，尝试一下代码，AC！

#### 代码
python3
```python
class Solution:
  def connect(self, root: 'Node') -> 'Node':
    if root is None:
      return None
    queue = [{
      "level": 1,
      "node": root
    }]
    while len(queue) > 0:
      item = queue.pop(0)
      level = item['level']
      node = item['node']

      if node.left is not None:
        if len(queue) > 0 and queue[-1]['level'] == level + 1:
          queue[-1]['node'].next = node.left
        queue.append({
          "level": level + 1,
          "node": node.left
        })
      if node.right is not None:
        if len(queue) > 0 and queue[-1]['level'] == level + 1:
          queue[-1]['node'].next = node.right
        queue.append({
          "level": level + 1,
          "node": node.right
        })
    return root
```