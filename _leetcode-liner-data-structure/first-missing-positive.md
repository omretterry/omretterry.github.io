---
layout: default
title: 缺失的第一个正数
---

## [41\. 缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/)

> Hard

#### 思路

* 从1遍历到数列中的最大值，如果所有的数都在列表中，说明确实的第一个正数是`max+1`
* **特殊情况** 
    * 如果最大值小于0， 缺失的第一个正数为1
    * 列表为空，缺失的第一个正数也为1

尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
      if len(nums) is 0:
        return 1
      m = max(nums)
      if m <= 0:
        return 1
      for i in range(1,m+1):
        if i not in nums:
          return i
      return m + 1
```

使用哈希表能减少`in`操作的时间复杂度。

但是这道题的难度定的是Hard。主要难点在于限制条件：**时间复杂度为O(n)，使用空间复杂度为O(1)**

如果使用Hash表，时间复杂度可以用到$$O(n)$$，但是需要用到$$O(n)$$的空间复杂度；如果不使用Hash表，直接遍历原数组进行判断的话，时间复杂度为$$O(n^2)$$

所以，如果这道题想到完全符合题目要求的话，还需要寻找别的方法

**新思路**

阅读大佬们的解题获得新思路，新思路还是哈希表。但是这边不是使用默认的set，而是我们自己构造一张哈希表

这个思路主要参考李威威大佬解题中的方法三：[点我前往](https://leetcode-cn.com/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/)

* 将`1`这个数放到下标为`0`的位置，`2`这个数放到下标为`1`的位置，然后再遍历一次数组，第`1`个遇到的它的值不等于下标的那个数，就是我们要找的缺失的第一个正数。
* 这个过程相当于自己构造一个哈希表，规则为：`数值为 i 的数映射到下标为 i - 1 的位置`


#### 代码（李威威大佬解题中的代码）
python3
```python
class Solution:
    # 3 应该放在索引为 2 的地方
    # 4 应该放在索引为 3 的地方
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                self.__swap(nums, i, nums[i] - 1)
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1
        return size + 1

    def __swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]
```