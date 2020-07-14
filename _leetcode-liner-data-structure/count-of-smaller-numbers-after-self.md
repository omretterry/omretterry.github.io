---
layout: default
title: 计算右侧小于当前元素的个数
---

## [315\. 计算右侧小于当前元素的个数](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/)

> Hard

### 方法一（暴力）（TLE）

#### 思路

首先想到的方法是暴力解，题目没有给出数据规模。但是作为`Hard`题，暴力解大概率会超时。

尝试一下，果不其然，TLE

#### 代码
python3
```python
class Solution:
  def countSmaller(self, nums: List[int]) -> List[int]:
    r = []
    for i in range(len(nums)):
      t = 0
      for j in range(i, len(nums)):
        if nums[j] < nums[i]:
          t += 1
      r.append(t)
    return r
```

### 方法二（归并排序）

阅读大佬解法，获得新思路，使用**归并排序**求解

这道题本质上说是求**逆序数**，而**逆序数**是**归并排序**的副产物

话不多说，先学一波归并排序：
> [https://www.interviewbit.com/tutorial/merge-sort-algorithm/](https://www.interviewbit.com/tutorial/merge-sort-algorithm/)
> [https://www.jianshu.com/p/3ad5373465fd](https://www.jianshu.com/p/3ad5373465fd)
> [https://www.cnblogs.com/chengxiao/p/6194356.html](https://www.cnblogs.com/chengxiao/p/6194356.html)

学习了**归并排序**之后再回过头看这道题

* 求`逆序数`之所以用归并排序来优化，是因为在归并的`并`的过程中，我们是局部有序的，这样我们就可以直接获得这段中的`逆序数`
* 但是中间这部分的`逆序数`不是完整的，在合并的过程中，数的位置会发生改变。统计的`逆序数`也会发生改变
* 为了解决上面的问题，我们需要一个数组`indexes`用来记录所有元素的索引
* `indexes`的作用是，在排序的过程中，我们交换的不是数字，是下标。只是交换的时候比较的是原来的数字
* 也就是说，我们使用`nums[indexes[i]]`和`nums[indexes[j]]`的比较结果来决定`indexes[i]`和`indexes[j]`的先后顺序

**补充说明**

* 刚接触这题，索引数组的使用想了很久，这部分还是有点绕的
* 首先我们为什么要使用索引数组？因为，如果我们直接用MergeSort的话，数字的位置是会发生改变的。当我们求出了某个数右面的逆序数的话，我们无法定位他在解中的位置。所以我们要定义一个索引数组，来做一个映射
* **要注意的是**当合并操作时，当`right`中的当前数比`left`的数小是，我们需要使用一个计数变量记录一下，`right`后面的数都要加上这个计数，因为`right`中是单调的，后面的数比前面的大，如果一个数比前面的数小，那必然比后面的小

以下视屏，讲的很清晰，看两遍就能理解了

**参考** [happygrilzt](https://happygirlzt.com/)
> [LeetCode 315 Count of Smaller Numbers After Self 中文解释 Chinese Version](https://www.youtube.com/watch?v=AeyUmjk4HGQ) 

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def merge(self,nums, indexes, left, right, res):
    i = 0
    j = 0
    r = []
    rightCount = 0
    while i < len(left) and j < len(right):
      if nums[left[i]] <= nums[right[j]]:
        res[left[i]] += rightCount
        r.append(left[i])
        i += 1
      else:
        rightCount += 1
        r.append(right[j])
        j += 1
    while i < len(left):
      res[left[i]] += rightCount
      r.append(left[i])
      i += 1
    while j < len(right):
      r.append(right[j])
      j += 1
    return r

  def mergeSort(self,nums, indexes, start ,end, res):
    if end-start <= 1:
      return indexes[start:end]
    mid = start + (end-start) // 2
    left = self.mergeSort(nums, indexes, start ,mid, res)
    right = self.mergeSort(nums, indexes, mid , end, res)
    return self.merge(nums,indexes,left,right, res)

  def countSmaller(self, nums: List[int]) -> List[int]:
    indexes = [ i for i in range(len(nums)) ]
    res = [ 0 for i in range(len(nums)) ]
    r = self.mergeSort(nums,indexes, 0,len(nums), res) 
    return res
```
