---
layout: default
---

## [198\. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)
> Easy

#### 思路

先审题，一般题目问最大的金额，最多的路径，解的个数之类的问题，很多情况是考察动态规划。抛开已有认知，还是先分析题目。

* 第一次选择，可以选任意
* 第二次选择，不能选择相邻位置

这样的话，暴破得出所有解法， 然后求出和，再进行比较是一种方法，但是应该会TLE，过！需改善思路。

分解问题，以`[2,7,9,3,1]` 为例，从前到后一个房子一个房子抢，分析抢到当前房子能够抢到的最大，*只考虑到当前，不考虑后面的*
 
```python
i:index, h:代表房子, 箭头:当前偷到的位置, m:当前位置能偷到的最多的钱


第1步
i    0  1  2  3  4
h    2  7  9  3  1 
     ↑ 
m    2
假如只有1个房子那肯定抢


第2步
i    0  1  2  3  4
h    2  7  9  3  1 
        ↑ 
m    2  7
到第二个房子，怎么考虑抢或不抢？
假如拿了h0(第一个房间)就不能拿h1，应为不能拿相邻的；
那h1比h0值钱，我肯定就放弃h0，抢h1。所以到第二个房间的最多是7


第3步
i    0  1  2  3  4
h    2  7  9  3  1 
           ↑ 
m    2  7  11
到第三个房子了，那h2抢不抢?
1. 抢: h2抢，那h1不能抢，取h0位置的能抢的最大和自身位置和，m2 = h2 + m0 = 11
2. 不抢:  那就抢h1，为7
两种情况取大值，故11


第4步
i    0  1  2  3  4
h    2  7  9  3  1 
              ↑ 
m    2  7  11 11 12
后面同理了，简单过一遍
1. 抢: m3 = h3 + m1 = 3 + 7 = 10
2. 不抢:  11
max(10,11) 故 11


第5步
i    0  1  2  3  4
h    2  7  9  3  1 
              ↑ 
m    2  7  11 11 12
1. 抢: m4 = h4 + m2 = 1 + 11 = 12
2. 不抢:  11
max(12,11) 故 12
```

那这道题的最终答案就是`m[-1]`，而且我们通过遍历h列表计算出m列表，

通项公式：

$$ i = 0: m[0] = h[0] $$
$$ i = 1: m[1] = max(h[0], h[1]) $$
$$ i > 1:  m[i] = max(h[i]+m[i-2], m[i-1]) $$


#### 代码

python3
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        # base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
```

