---
layout: default
title: 打家劫舍 III
---

## [337\. 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/)

> Medium

#### 思路

思路其实不是很复杂，只要能想到那个点。

* 针对某个树的节点来说，当前节点有两种情况：抢或者不抢
* 当前节点抢的话，值为，抢孙子节点+当前节点的值
* 当前节点不抢的话，值为，抢子节点
* 这两种情况的较大值就是我们要的结果

以上，尝试写一下代码，TLE。

使用记忆化递归优化，减少重复计算，AC！

#### 代码
python3
```python
class Solution:
  @functools.lru_cache(None)
  def helper(self,node):
    if node is None:
      return 0
    #打劫根
    v1 = node.val
    if node.left:
      v1 += self.helper(node.left.left) + self.helper(node.left.right)
    if node.right:
      v1 += self.helper(node.right.left) + self.helper(node.right.right)
    #不打劫根
    v2 = self.helper(node.left) + self.helper(node.right)
    return max(v1,v2)

  def rob(self, root: TreeNode) -> int:
    return self.helper(root)
```