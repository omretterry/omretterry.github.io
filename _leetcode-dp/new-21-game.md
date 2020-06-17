---
layout: default
---

## [837\. 新21点](https://leetcode-cn.com/problems/new-21-game/)
> Medium

#### 思路

首先进行**阅读理解**：

* 从0开始抽卡，然后累加抽到卡的积分
* 卡片的数字是 $$ [1, W] $$
* 积分 `<K` ， 不继续抽牌，积分`>=K`时停止抽牌
* 停止抽牌后，积分`<=N`获胜， 积分`>N`失败

阅读理解结束，开始**思考过程**：

* 对于 $$ [1, W] $$ 的卡片，抽取每张卡片的概率都是 $$ 1/W $$
* 想要和在范围中，那就是抽取这些组合的概率和。举个栗子，就清楚了：

```
掷两次骰子，求两次骰子和在4-6之间的概率
4的可能的组合为: (1,3)、(2,2)、(3,1)
5的可能的组合为: (2,3)、(3,2)
6的可能的组合为: (1,5)、(2,4)、(3,3)、(4,2)、(5,1)
P(sum) = P(4) + P(5) + P(6) = 3/36 + 2/36 + 5/36 = 5/18
```

* 对于我们这道题，如果和`<K` ，我们还要继续抽卡，这样就是 $$ 1/W $$ 还要在乘上后面的概率。就类似我们上面掷骰子例子中掷骰子的次数。
* 所以递归终止条件为`当前和 >= K `
* 递归结束后，假如在N的范围里和最后一次的概率为1，代表结束抽卡之后结果必定成功概率为100%，反之为0

使用记忆化递归，TLE

python3

```python
class Solution:
    @lru_cache(None)
    def dfs(self, cur, N, K, W):
      if cur >= K:
        if cur <= N:
          return 1
        else:
          return 0
      sum = 0
      for i in range(1, W+1):
        sum += 1.0 / W * self.dfs(cur + i, N, K, W)
      return sum
    def new21Game(self, N: int, K: int, W: int) -> float:
      return self.dfs(0,N,K,W)
```

**TLE，需要更新思路** 记忆化递归通常我们可以转成dp，bottom-up方式来优化。

**拜读大佬解法，获得新思路**

* 类似于动态规划爬楼梯解题的思路，想要爬到第i阶，要么是从i-1过来，要么是从i-2过来
* 对于我们这道题最终要使和为i，那必然是从$$ [i-1,i-W] $$这个区间跳过来的

##### 概率分析

* 已有i-1，再抽1，最终为i
* 已有i-2，再抽2，最终为i
* ...
* 以后i-W，再抽W，最终为i
* i的概率，` P(i) = P(i-1) * 1/W + P(i-2) * 1/W...P(i-W) * 1/W = (P(i-1)+... + P(i-W)) * 1/W `

##### 动态规划

* 前面的概率决定了当前状态，后面的状态不会影响当前状态，具有后无效性，可以进行状态转移，使用动态规划。
* 定义dp数组，`dp[i]`表示和为i的概率。
* dp数组的长度为`N+1`，代表和为`0~N`的概率。题目是求解 `N` 范围内的概率，所以后面的不用考虑
* **状态转移**：$$ \displaystyle{dp[i] =  (\sum_{k=i-W}^{i-1} dp_{k}},i\le K) * 1/W $$
* 求和过程中需要保证i <= K也就是，应为>K 的已经结束了，概率已经确定，不需要计算在后面的概率中
* 最终结果为 $$ result = \displaystyle{\sum_{k=K} ^ N}dp_{k} $$

综上，进行尝试，TLE。我真的是太难了。。

python3

```python
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
      dp = [None] * (N + 1)
      dp[0] = 1
      for i in range(1, N + 1):
        left = 0 if (i-W) < 0 else (i-W)
        right = i if i <= K else K 
        dp[i] = sum(dp[left:right]) * (1/W)
      return sum(dp[K:])
```

**还需进行优化**

* `dp[i]` 求$$ [i-W,i-1] $$范围的值，虽然每次都向右移动了一个，但是还是整个遍历求和了。
* 使用滑动窗口，中间部分不重复计算，只判断头尾元素。

综上，进行尝试，AC！

#### 代码

python3
```python
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
      dp = [None] * (N + 1)
      dp[0] = 1
      presum = 0
      for i in range(1, N + 1):
        if i-W > 0:
          presum -= dp[i-W-1]
        if i <= K:
          presum += dp[i-1]
        dp[i] = presum * (1/W)
      return sum(dp[K:])
```
