---
layout: default
title: 从先序遍历还原二叉树
---

## [1028\. 从先序遍历还原二叉树](https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/)

> Hard

#### 思路

看到还原二叉树的题目，想到之前有一题做的类似的。[105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

105这道题是通过前序和中序确定一个二叉树。仔细思考一下我们就能发现，光有一个维度是确定不了二叉树的。

回到1028，光有前序肯定是不够的。发现还有`-`节点的深度

**思考过程**

* **前序**遍历，`S`的第一个元素作为根节点
* 确定了根节点之后，接着要确定，左半部分树和右半部分树。将`S`分成两个字符串：`ls`和`rs`
* 划分左右两部分的依据是，每个数字前面的`-`最少的，肯定是下一层的两个节点。在这两个节点切两刀，就是左半部分和右半部分
* 对于`ls`,`ls`的第一个元素是根节点，再把剩下的分成左右两部分。**明显的递归过程**
* **递归终止条件** 要构造节点的那个字符串中没有元素了，递归终止
* 有的节点可能只有一个子节点，这种情况的判断依据是，只有一个数字前的`-`数量最少

以上，尝试写一下代码

**过程中的问题**
* 具体如何分成左右两部分，我的方法是，在递归方法中使用一个参数记录当前的层级，数字前的`-`数量等于当前层级，就是当前层级的元素

#### 代码

python3
```python
class Solution:
    def getNodeValue(self, s):
      for i in s.split('-'):
        if i != '':
          return i
          
    def split(self, s, l):
        left_found = False
        left_start = -1
        right_start = -1
        pre_number = False #避免出现多位数字的情况
        count = 0
        for i, v in enumerate(s):
            if v != '-':
                if count == l+1:
                  if left_found:
                    right_start = i
                    break
                  else:
                    left_start = i
                    left_found = not left_found
                if not pre_number:
                  count = 0
                else:
                  count += 1
            else:
                count += 1
                pre_Number = False
        offset = l + 1
        if right_start > 0:
            ls = s[left_start-offset:right_start-offset]
            rs = s[right_start-offset:]
        else:
            ls = s[left_start-offset:]
            rs = None
        # print(ls,rs)
        return ls, rs

    def buildNode(self, S, l):
        if len(S) == 0 or l > S.count('-'):
            return None
        node = TreeNode(self.getNodeValue(S))
        ls, rs = self.split(S, l)
        node.left = self.buildNode(ls, l+1)
        if rs:
            node.right = self.buildNode(rs, l+1)
        return node

    def recoverFromPreorder(self, S: str) -> TreeNode:
        node = self.buildNode(S, 0)
        return node
```


代码冗余很多，主要的原因是分割字符串的操作不聪明。找了一下大佬们的解法

* 由于是DFS之后的结果，使用栈来存放数据，按层存放，先处理一遍数据。将节点和层号存入栈中
* 做出栈，构造节点操作，变量记录当前层级，与栈顶元素层级比较

暂时还没有尝试，感兴趣的小伙伴可以试一下