---
layout: default
title: 长度最小的子数组
---

## [209\. 长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)

> Medium

### 方法一（双指针，滑动窗口）

#### 思路

应为题目中要求的连续的子数组，想到可以使用双指针滑动窗口的方式来求解，这样遍历的范围都是连续的子数组

* 刚开始两个指针都指向开头
* 首先向后移动一个指针，当这个窗口中的数字之和$$>=s$$即满足题目要求时，压缩左边指针
* 当左边指针移动到窗口中的数字和`<s`时，表示这是其中一种可能的解
* 继续遍历，直到窗口移动到结尾，返回结果

尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = 0
        j = 1
        min_length = math.inf
        while j <= len(nums):
          if sum(nums[i:j]) < s:
            j += 1
          else:
            while sum(nums[i:j]) >= s:
              min_length = min(min_length, j - i)
              i += 1

        return 0 if min_length == math.inf else min_length
```

### 方法二（前缀和）

#### 思路

* 方法一使用滑动窗口，时间复杂度为$$O(n)$$，题目要求改进方案的时间复杂度为$$O(nlogn)$$
* 从时间复杂度可以看出，我们需要使用，二分求解
* 题目要求连续子数组，又不能打乱原有的顺序，自然想到使用前缀和方式求解（前缀和数组，是单调递增数组）

尝试写一下代码，AC！

个人觉得，还是滑动串口的方法更容易想到

#### 代码
python3
```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
      presum = [0]
      sum = 0
      ans = math.inf
      for i in nums:
        sum += i
        presum.append(sum)
      for k in range(1, len(presum) + 1):
        t = s + presum[k - 1]
        closest_index = bisect.bisect_left(presum, t)
        if closest_index <= len(nums):
          ans = min(ans, closest_index - k + 1)
      return 0 if ans == math.inf else ans
```