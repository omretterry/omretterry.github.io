---
layout: default
---

## [通过翻转子数组使两个数组相等](https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/)

#### 思路

既然可以元素两两交换，那就是等于说可以随便怎么换。所以排序之后两数组相等就ok，AC！

#### 代码

python3
```python
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
```
