---
layout: default
---

## [238\. 除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self/)

>Medium

#### 思路

**题目几点要求**
* 不能使用**除法**
* 时间复杂度为$$ O(n) $$，换句话说，就是一层遍历，不能用循环嵌套。但是我们可以多次遍历
* 除自身以外的乘积，我们可以分解为：元素左侧的乘积 * 元素右侧的乘积
* 假如是边界，侧边没有元素我们给1，应为乘积不受影响
* 题目进阶让我们在常数空间中操作，这样我们要用一个骚操作，使用dp中滚动数组的思想，减少空间复杂度
* 利用滚动数组的思想，以左侧为例，向右移动一位，历史的乘积在乘上当前元素左侧的数据，也就是移动新增的一位，就是当前节点左侧所有元素的乘积

```python
left → right
#1
value    1  2  3  4
         ↑
left     1 
right

#2
value    1  2  3  4
            ↑
left     1  1 
right

#3
value    1  2  3  4
               ↑
left     1  1  2
right

#4
value    1  2  3  4
                  ↑
left     1  1  2  6
right

left ← right
#1
value    1  2  3  4
                  ↑
left     1  1  2  6
right             1

#2
value    1  2  3  4
               ↑
left     1  1  2  6
right          4  1

#3
value    1  2  3  4
            ↑
left     1  1  2  6
right      12  4  1

#4
value    1  2  3  4
                  ↑
left     1  1  2  6
right   24 12  4  1

--------------------
left * right
result 24  12  8  6
```

实际我们也不需要两个数组，只需在一个数组上进行操作即可。
综上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      result = [1] * len(nums)
      for i in range(1, len(nums)):
        result[i] = result[i-1] * nums[i-1]
      k = 1
      for j in range(len(nums)-1, -1, -1):
        result[j] *= k
        k *= nums[j]
      return result
```