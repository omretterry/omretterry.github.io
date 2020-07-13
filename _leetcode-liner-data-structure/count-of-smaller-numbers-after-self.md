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