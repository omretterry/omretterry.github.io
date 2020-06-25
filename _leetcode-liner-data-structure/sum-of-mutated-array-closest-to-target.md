---
layout: default
---

## [1300\. 转变数组后最接近目标值的数组和](https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/)
>Medium

#### 思路
分析题目
* value 值越大整个数组的和越大，value值越小整个数组的和越小
* value的范围在$$ [0, max(arr)] $$
* 确定value后，可能sum不等于target。如何判断sum 最接近target。主要是target上下的方位。解决方案是，取上下的值进行一次比较。如下图，借用[李威威]([https://leetcode-cn.com/u/liweiwei1419/](https://leetcode-cn.com/u/liweiwei1419/))大佬的图:

![](/public/images/sum-of-mutated-array-closest-to-target-1.png)

很显然，这种情况，我们可以使用二分法来进行求解。

尝试写一下代码
* 注意：做题过程中发现一个问题也需要留意，假如上下两个的sum值和target的距离是相同的，我们需要取小的那一个

AC！


#### 代码
python3
```python
class Solution:
  def sumList(self, value ,arr):
    sum = 0
    for i in arr:
      if i >= value:
        sum += value
      else:
        sum += i
    return sum

  def findBestValue(self, arr: List[int], target: int) -> int:
    left = 0
    m = max(arr)
    right = m
    while left < right:
      mid = (left + right) // 2
      if self.sumList(mid,arr) > target:
        right = mid
      else:
        left = mid + 1
    s = self.sumList(left, arr)
    if s == target:
      return left
    elif s < target:
      other_s = self.sumList(left+1, arr)
      if abs(s-target) > abs(other_s-target) and left+1 <= m:
        return left + 1
    else:
      other_s = self.sumList(left-1, arr)
      if abs(s-target) >= abs(other_s-target) and left-1 >= 0:
        return left - 1   
    return left
```


