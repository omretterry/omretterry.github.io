---
layout: default
title: 安排邮筒
---

## [1478\. 安排邮筒](https://leetcode-cn.com/problems/allocate-mailboxes/)

> Hard

#### 思路

要求解这道题，不能陷入到题目的描述当中，需要提取题目表述，简化条件。

* `houses`数组是无序的，首先需要先将`houses`排序
* `i`个房子里面插入`k`个邮筒。可以转化成，将`houses`数组，分成`k`份，`k`置于这几个分组中间。使得距离和最小
* 每个区间中的元素到邮筒的距离最小。转化成，给定一个数组，在数组中放置一个元素。使得每个节点到这个元素的距离和最小。这个元素其实就是中位数。所以给定了一个区间，这个区间有一个邮筒。那这个区间里的邮筒的最小距离就能计算出来 
* 定义一个dp数组，`dp[i][j]` 表示，`i`个数字这个区间划分`j`份的最小距离
* 最终的答案为`dp[n][k]`

#### 补充

**为什么是中位数**

对于一个数组，一个邮筒的情况。为什么放置在中位数节点是距离和最小的情况。我们可以一对一对的看，假如房子的数量是2个，那么我们放在中间任意的位置距离和都是一样的。假如房子数量是3，那我们放在中间那个房子的距离和是最小的。扩展，房子的偶数个，邮箱放在对中间的一对房子的任意位置，距离和最小。房子个数是奇数个，邮箱放在中间那个房子的节点位置，距离和最小

结论：一个邮箱的情况，只要放在中位数节点，就可以值距离和最小

**状态转移**

对于最后一个邮箱来说，

最大的负责范围是第`j-1`个房间，到`i`的房间，最坏就是前面的一个邮箱管一个房子。那最后一个就得剩下的都管

最小的负责范围是第`i`个房间，前面的房间，都被前边的邮箱管走了，只用管最后一个房间就行了

所以状态转移方程为

$$dp[i][j]=min(dp[t-1][j-1] + distance(t,i), dp[i][j])$$
$$i>=t>=j-1$$

尝试写一下代码，AC！真不容易，主要是边界条件还是不熟，还是要单步慢慢调，还是太弱鸡阿。

#### 代码
python3
```python
class Solution:
    # houses在区间[i,j]中放置一个邮筒的最小距离和
    def distance(self, houses, i, j):
      dis = 0
      m = (i+j) // 2
      for k in range(i,j+1):
        dis += abs(houses[k-1] - houses[m-1])
      return dis

    def minDistance(self, houses: List[int], k: int) -> int:
      houses.sort()
      #定义dp数组,dp[i][j]表示i个数前分成j组的最小距离
      dp = [[math.inf for _ in range(k+1)] for _ in range(len(houses)+1)]

      for h in range(1, len(houses) + 1):
        dp[h][1] = self.distance(houses, 1, h)

      for i in range(1, len(houses)+1):
        for j in range(2, k+1):
          for t in range(j-1, i+1):
            dis = self.distance(houses, t, i)
            dp[i][j] = min(dp[i][j], dp[t-1][j-1] + dis)
      return dp[len(houses)][k]
```