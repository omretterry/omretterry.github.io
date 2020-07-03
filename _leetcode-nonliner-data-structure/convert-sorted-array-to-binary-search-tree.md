---
layout: default
title: 将有序数组转换为二叉搜索树
---

## [108\. 将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)

> Easy

#### 思路

思路其实很简单，明显的递归题

* BST 是左树小右树大的特点
* 数组是已经排序好的，那中间的数就作为节点的数值，这样分为左右两部分，分别对应左树和右树
* 左右两部分在继续上面的操作
* 如果数组为空，直接返回None，说明已经结束了

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def build(self, nums):
        if len(nums) is 0:
            return None
        mid = len(nums) // 2
        m = nums[mid]
        left = nums[:mid]
        right = nums[mid+1:]
        node = TreeNode(m)
        node.left = self.build(left)
        node.right = self.build(right)
        return node 

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build(nums)
```