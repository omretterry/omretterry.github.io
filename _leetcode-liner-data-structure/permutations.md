---
layout: default
---

## [46\. 全排列](https://leetcode-cn.com/problems/permutations/)

>Medium

#### 思路

先在纸上推演一下这道题的解法：
```text
#1 确定 1 ：
#2    2  or  3
#3    3  or  2  

#1 确定 2 ：
#2    1  or  3
#3    3  or  1 

#1 确定 3 ：
#2    1  or  2
#3    2  or  1 
```

暴力解法的for循环嵌套数量是根据数组长度来决定的，现在是不可行的。通过上面的演算过程，我们也能想到，应该使用递归在求解：先定下一个，打开后面的门，再定一个打开后面的门，打开后最后，然后在一扇一扇门回来。


**递归终止条件**我们使用一个数组在记录，现在选到了第几个数字，开到了哪一扇门，当这个数组长度等于我们的元素个数时结束，开到了最后一扇门。


以上，AC！


#### 代码
python3
```python
class Solution:
    def helper(self, nums, result, cur, i):
      cur.append(i)
      if len(cur) == len(nums):
        result.append(cur)
      for n in nums:
        if n not in cur:
          self.helper(nums,result,cur[::],n)
    def permute(self, nums: List[int]) -> List[List[int]]:
      result = []
      for n in nums:
        self.helper(nums, result, [], n)
      return result
```