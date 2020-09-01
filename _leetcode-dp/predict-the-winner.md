---
layout: default
title: 预测赢家
---

## [486\. 预测赢家](https://leetcode-cn.com/problems/predict-the-winner/)

> Medium

### 方法一（记忆化递归）

#### 思路

* 题目条件可知，我们可以选择第一个数和最后一个数，最终的选择构成一个树状结构，如下图，（来自leetcode官方解题）
![](https://assets.leetcode-cn.com/solution-static/486/486_fig1.png)
* 这边有个巧妙的思路就是怎么判断是*玩家一*获胜还是*玩家二*获胜。这边使用一个总数，总数表示先手得分和后手得分之间的差。当`总分 >= 0`时表示先手获胜，反之，表示先手无法获胜

#### 代码
python3
```python
class Solution:
  def PredictTheWinner(self, nums: List[int]) -> bool:
    @functools.lru_cache(None)
    def helper(start,end):
      if start == end:
        return nums[start]
      left = nums[start] - helper(start+1,end)
      right = nums[end] - helper(start,end-1)
      return max(left,right)

    return helper(0,len(nums)-1) >= 0
```