---
layout: default
title: 分割数组的最大值
---

## [410\. 分割数组的最大值](https://leetcode-cn.com/problems/split-array-largest-sum/)

> Hard

### 方法一（二分搜索）
#### 思路

首先我们分析一下题目的意思，将数组分割到`m`个子数组，然后确保这些字数组的和的最小的最大值是多少。

可以确定的是最大值得范围一定是在`[max(n), sum(n)]`的区间范围当中。我们要在范围中找到一个目标值想到可以使用`二分查找`来求解。

* 假设我们要找一个`target`，`target`表示每个数组和的最大值的最小值。
* 每次二分取得中间值`mid`，那加入说这个`mid`的值是我们想要的`target`说明则有，每个子数组的和都`<=mid`
* **如何判断mid是不是我们想要的值?** 上面我们说到假如`mid`是`target`的话，所有子数组的和都应该`<=mid`我们可以利用分组的数量和`m`的关系来确定，`target`在二分的左区间还是右区间
* 按照`mid`的数值，进行分组并统计分组的数量。假如分组小了，说明`mid`大了，在右区间。反之，在左区间

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def splitArray(self, nums: List[int], m: int) -> int:
    def count(nums,target):
      s = 0
      cnt = 1 #不分割就是有一个
      for i,v in enumerate(nums):
        s += v
        if s > target:
          cnt += 1
          s = v
      return cnt

    i = max(nums)
    j = sum(nums)
    while i < j:
      mid = i+(j-i)//2
      if count(nums,mid) > m:
        i = mid + 1
      else:
        j = mid    
    return i
```

### 方法二（动态规划）(python3 TLE)
#### 思路

这道题也可以考虑动态规划的方式求解

* 设置`dp`数组，`dp[k][i]`表示分成`k-1`组（因为从`0`开始）到坐标`i`为止的最小的最大值
* 那么对于`dp[k][j]`来说，最后一组的可能是`[x:j]`,`x`的范围为`[1...j]`。取这些可能性中的结果的最小值就是我们想要的答案，如下图：
![](/public/images/split-array-largest-sum-1.png)
* basecase：当`k=0`时，就是分一个组，`dp[0][i]`就是前缀和数组

以上，尝试写一下代码，TLE

#### 代码
python3
```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
      dp = [[math.inf for _ in range(len(nums))] for _ in range(m)]
      
      pre = 0
      presum = [0] * (len(nums) + 1)
      for i,v in enumerate(nums):
        dp[0][i] = pre + v
        presum[i+1] = dp[0][i]
        pre = dp[0][i]

      for k in range(1,m):
        for i in range(1,len(nums)):
          for j in range(1,i+1):
            dp[k][i] = min(dp[k][i], max(dp[k-1][j-1], presum[i+1] - presum[j]))

      return dp[m-1][-1]
```

据说用`C++`使用`动态规划`是可以AC的，未做尝试。