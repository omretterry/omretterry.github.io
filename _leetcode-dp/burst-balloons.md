---
layout: default
title: 戳气球
---

## [312\. 戳气球](https://leetcode-cn.com/problems/burst-balloons/)

> Hard

#### 思路

看到问题是最大的数量是多少，想到使用动态规划方法来求解

* 定义`dp`数组，`dp[i][j]`表示在`[i:j+1]`范围中，所能的到的最大值
* 题目中边界情况左右两个边界之外还有两个虚拟的气球，不能戳破，模拟值为`1`，直接在原来的数组中插入，方便计算
* 对于这么多气球，假如，在`[i:j+1]`这个范围里面，我们要留下气球`k`，那么我们需要戳爆`[i:k]`和`[k+1:j+1]`范围中的所有气球，如下图
![](/public/images/burst-balloons-1.png)
* 现在的问题是`[i:j+1]`这个范围里面，到底留哪个气球能够使值最大。我们就遍历一遍，每个都计算一遍，取最大的那个。即，$$max(dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1]);i <= k <= j $$
这边需要稍微留意一下下标，应为我们在前后都加了一个元素
* 对于`[i:k]`和`[k+1:j+1]`范围里面能够拿到多少最大数量，我们发现这个就是上述问题的子问题，和上面的思考过程是一样的
* 动态规划来思考的话，我们需要显得到最小子问题的结果，然后自底向上的得出问题的结果，我们这边需要先求子问题的解，而这边的子问题是短的字串中，去戳气球。所以我们这边从长度为`1`的字串开始求解
* 答案为`dp[1][n]`，即我们从第一个到最后一个气球获得的最大值

以上，尝试写一下代码，AC!

#### 代码
python3
```python
class Solution:
  def maxCoins(self, nums: List[int]) -> int:
    # dp[i][j] = maxCoins(nums[i:j+1])
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

    for l in range(1, n + 1):
      for i in range(1, n - l + 2):
        j = i + l - 1
        for k in range(i, j + 1):
          dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1])
    return dp[1][n]
```