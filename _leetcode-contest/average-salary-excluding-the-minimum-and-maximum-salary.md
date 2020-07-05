---
layout: default
title: 去掉最低工资和最高工资后的工资平均值
---

## [1491\. 去掉最低工资和最高工资后的工资平均值](https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/)

> Easy

#### 思路

签到题，直接根据题目意思，先给整个组数求和后去除最大值和最小值，再除以`n-2`

AC!

#### 代码
python3
```python
class Solution:
    def average(self, salary: List[int]) -> float:
      return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
```