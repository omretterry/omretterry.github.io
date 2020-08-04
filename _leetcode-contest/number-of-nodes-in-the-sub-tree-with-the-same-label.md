---
layout: default
title: 子树中标签相同的节点数
---

## [1519\. 子树中标签相同的节点数](https://leetcode-cn.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/)

> Medium

#### 思路

要统计子树中的标签相同的节点数，我们就要遍历树。可以想到DFS和BFS两种方式。这道题是统计某个节点的子节点的相同标签的数量，显然使用DFS比较合适。

* **构造数据结构** ，原本想直接够造一个数，`edges`的下标`0`作为父节点，下标`1`作为子节点，但是这样是有问题的。题目中表明这个结构是一个*无环无向图*所以下标不能作为父子节点的依据。构造*邻接表*和`visited`数组结合，从而进行`dfs`
* 将每个节点的子树的标签数量都记录下来，然后提供给父节点使用，**为什么不只记录当前父节点的个数？**比如`示例5`，当我们到了`3`这个节点之后，回溯到父节点，父节点是需要子树中标签`a`的个数的。所以我们都需要记录下来
* 使用**后序遍历**，原因是，左子树的结果和右子树的结果是独立的，我们在计算左子树的时候不能被右子树的结果影响，所以使用**后序遍历**，在最后计算根节点数量

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def sumCounter(self,c1,c2):
      c = collections.defaultdict(int)
      for k in c1.keys() | c2.keys():
        c[k] = c1[k] + c2[k]
      return c

    def helper(self,labels,nodes,visited,res,cur_node):
      counter = collections.defaultdict(int)
      visited.add(cur_node)
      counter[labels[cur_node]] += 1
      for c in nodes[cur_node]:
        if c not in visited:
          childCounter = self.helper(labels, nodes,visited,res,c)
          counter = self.sumCounter(counter,childCounter)
      res[cur_node] = counter[labels[cur_node]]
      return counter

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
      nodes = {}
      for e in edges:
        nodes.setdefault(e[0], []).append(e[1])
        nodes.setdefault(e[1], []).append(e[0])
      res = [1] * n
      visited = set()
      self.helper(labels,nodes,visited,res,0)
      return res
```

* **改进点** 代码中使用了`defaultdict`来记录数量，导致计算和的时候代码比较冗余，可以考虑其他数据结构，优化代码