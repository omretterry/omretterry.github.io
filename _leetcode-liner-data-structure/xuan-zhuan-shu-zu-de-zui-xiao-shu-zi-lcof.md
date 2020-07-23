---
layout: default
title: 旋转数组的最小数字
---

## [剑指 Offer 11\. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

> Easy

### 方法一（暴力）
#### 思路

不管怎么旋转交换数组，最小的永远都是那个最小的

时间复杂度$$O(n)$$

所以，直接返回最小值，AC！

#### 代码
python3
```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
      return min(numbers)
```

### 方法二（二分搜索）
#### 思路

题目中数组形成的方式是，在一个有序的数组中，截取的前面一段，放到了后面。那我们只要找到转换的这个分割点，就是我们想要的答案。

* 分析一下，题目中数组的特征：
    * 数组是由两个递增数组拼接起来得到的，按照这样的方式数组可以分成两个区域
    * 两个区域自身都是单调增
    * 后面一个区域的所有元素都小于等于前一个区域的所有元素

* 二分搜索对于中间值和区间`[i,j]`，有三种情况：
    * `numbers[mid] > numbers[j]` 中点值比右边界的值大，说明`mid`节点在区域一（大的那个区域），转换点肯定在右侧
    * `numbers[mid] < numbers[j]` 中点值比右边界小，应为区域一里面的每个数都比区域二中的小，所以转换点肯定是在左边。**特殊情况**：假如区间`[i,j]`本身是个单调增数组，说明转换点是`0`,同样满足在左侧区域
    * `numbers[mid] == numbers[j]` 中间值和右边界相同，无法判断，应为元素可以是相等的，如：`1,1,2,2,2`和`1,2,2,1,2`一个转折点是在左边区域，一个在右边区域。
* 对于第三种情况，我们使区间变成`[i,j-1]`，比较的相同，说明将边界`j`去掉之后，对于结果是没有影响，即使`j`的值是最小的也有`mid`和他相同。（**注意**，应为这道题是返回旋转的节点的值，我们可以这样简单处理）
* **为什么都是比较右边界？** 比较左边界`i`，无法确定是在哪个区域。比如，`1,2,3,4` 这样的列表，转换点是`index:0`的位置，当`numbers[mid] > numbers[i]` 时在右边，列表为`4,1,2,3`在左边，不好确认。比较`j`边界不会出现这种情况，应为j都是在右边区域。

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def minArray(self, numbers: List[int]) -> int:
    i = 0
    j = len(numbers) - 1
    while i < j:
      mid = i + (j-i) // 2 
      if numbers[mid] < numbers[j]:
        j = mid
      elif numbers[mid] > numbers[j]:
        i = mid + 1
      else:
        j -= 1
    return numbers[i]
```
