---
layout: default
title: 递增子序列
---

## [491\. 递增子序列](https://leetcode-cn.com/problems/increasing-subsequences/)

> Medium

#### 思路

* 回溯的套路题
* 选中一个数字之后，下一步的选择只能再这个字后面的字中进行选择。
* 使用**回溯法**求解，按照回溯的套路，定义一个`path`变量，用于记录当前选择的路径，定义`res`表示最终需要返回的结果，定义`curIndex`表示当前所处的位置，应为这样才能在下一层选择的时候知道处于哪一个节点

尝试写一下代码，AC！

最后应为有重复节点，这边选择了再最后去重，也可以在递归中用一个变量记录走过的点，如果遇到相同的进行*剪枝*，在过程中去重

#### 代码
python3
```python
class Solution:
    def helper(self, nums, curIndex, path, res):
      if curIndex >= len(nums):
        return 
 
      if len(path) > 1:
        res.append(path)

      for i in range(curIndex + 1,len(nums)):
        if curIndex == -1 or nums[i] >= nums[curIndex]:
          path.append(nums[i])
          self.helper(nums, i, path[::], res)
          path.pop()
      return

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
      res = []
      self.helper(nums, -1, [], res)
      return list(set([tuple(x) for x in res]))
```