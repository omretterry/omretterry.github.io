---
layout: default
title: 不同的二叉搜索树 II
---

## [95\. 不同的二叉搜索树 II](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/)

> Medium

#### 思路

* 构建树，我们使用递归的方式，搜索二叉树的特征是，比节点小的节点作为左子树，比节点大的节点作为右节点
* 一般构建一棵树，但是我们这边要多种可能性。将没有节点的左子树和右子树的所有可能性进行组合，组合到父节点中
* 当`n==0`的情况，直接返回空树，即`None`

以上，尝试写一下代码，AC！

这道题难点就是要，理解节点的左右子树自由组合的过程，最好还是在纸上推演一下，写出代码之后debug，会清晰很多

#### 代码
python3
```python
class Solution:
  def generateTrees(self, n: int) -> List[TreeNode]:
    def helper(lo,hi):
      res = []
      if lo > hi:
        res.append(None)
        return res
      for i in range(lo,hi+1):
        left_list = helper(lo,i-1)
        right_list = helper(i+1,hi)
        
        for l in left_list:
          for r in right_list:
            node = TreeNode(i,l,r)
            res.append(node)
      return res

    if n is 0:
      return None
    return helper(1,n)
```