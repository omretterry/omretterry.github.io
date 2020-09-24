---
layout: default
title: 二叉搜索树中的众数
---

## [501\. 二叉搜索树中的众数](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/)

> Easy

#### 思路

使用最简单粗暴的方式求解：

* 使用一个计数器，统计遍历到的节点的值的数量
* 使用DFS方式遍历树
* 最后将计数器排序，统计出计数器中数量最多的值

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def findMode(self, root: TreeNode) -> List[int]:
    counter = collections.defaultdict(int)
    def dfs(node):
      if node is None:
        return
      counter[node.val] += 1
      dfs(node.left)
      dfs(node.right)
      return 

    dfs(root)
    sorted_counter = sorted(counter.items(), key = lambda kv: kv[1], reverse = True)
    pre_c = 0
    res = []
    for i in sorted_counter:
      if i[1] >= pre_c:
        res.append(i[0])
        pre_c = i[1]
      else:
        break
    return res
```