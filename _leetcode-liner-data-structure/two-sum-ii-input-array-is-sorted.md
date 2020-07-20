---
layout: default
title: 两数之和 II - 输入有序数组
---

## [167\. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

> Easy

### 方法一（二分搜索）
#### 思路

* 应为是有序的数列，我们可以使用**二分搜索**寻找目标值
* 遍历数组，对于当前元素，我们只需要在当前元素之后的元素中寻找值为`target-cur`的坐标即可。
* 找到了，就返回当前的`坐标+1`和`目标值的坐标+1`
* 找不到，就继续往后寻找

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      for left,v in enumerate(numbers):
        offset = bisect.bisect_left(numbers[left+1:],target-v)
        right = offset + left + 1
        if right >= len(numbers):
          continue
        if v + numbers[right] == target:
          return [left+1,right+1]
```

### 方法二（双指针）
#### 思路

* 应为数列是有序的，我们可以使用*对向双指针*来结局这个问题
* 最开始的时候两个指针分别指向开始元素和最后一个元素
* 如果两个指针指向的元素之和比目标值小，左边元素向右移动一位（和是增大的）
* 如果元素之和比目标值大，右边元素向左移动一位（和是减小的）
* 如果想好相等，那就是我们想要的结果，返回两个指针的坐标（注意，坐标不是从0开始的）

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      i = 0
      j = len(numbers) - 1
      for _ in range(len(numbers)):
        t = numbers[i] + numbers[j]
        if t < target:
          i += 1
        elif t == target:
          return [i+1,j+1]
        else:
          j -= 1
      return [0,0]  
```