---
layout: default
---

## [1470\. 重新排列数组](https://leetcode-cn.com/problems/shuffle-the-array/)

#### 思路

签到题一般没什么难度，元素个数为2n个，我们只用遍历n，然后交叉着添加到新数组中。AC！

#### 代码

python3
```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
      result = []
      for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
      return result
```