---
layout: default
title: 重新安排行程
---

## [332\. 重新安排行程](https://leetcode-cn.com/problems/reconstruct-itinerary/)

> Medium

#### 思路

**抽象题目大意**

* 所有的机票，指定了两个节点和一个变，我们可以构造成一个**图**，使用**邻接表**表示
* 题目要求的值，就是求**欧拉路径**
* 题目中提示说*假定所有机票至少存在一种合理的行程*，即，我们构造的图一定是**半欧拉图**

**欧拉图的相关文档**
> [https://zhuanlan.zhihu.com/p/108411618](https://zhuanlan.zhihu.com/p/108411618)

#### 代码