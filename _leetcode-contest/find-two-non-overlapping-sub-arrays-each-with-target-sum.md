---
layout: default
title: 找两个和为目标值且不重叠的子数组
---

## [1477\. 找两个和为目标值且不重叠的子数组](https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)

#### 思路

**（由于测试用例不完全）周赛时AC了，但是实际代码是有问题的** 说一下我的思路吧:

* 看到连续子串和，第一反应是可以使用前缀和算法，方便我们进行连续字串的比较
* 首先构造前缀和数组，再遍历前缀和
* 遍历获取和为`target`的字串的坐标，使用`[start,end]`方式记录
* 排除相交字串，相交的意思是前一个字串的end小于后一个字串的start
* 最后取最短的两个字串，构成字串对，返回两个字串的长度和

#### 代码（WA）
python3
```python
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
      presum = [0] * len(arr)
      temp = 0
      for i in range(len(arr)):
        presum[i] = temp + arr[i]
        temp += arr[i]
      presum = [0] + presum
      
      j = 0
      k = 1
      queue = []
      while j < len(presum) and k < len(presum):
        if presum[k] - presum[j] == target:
          if len(queue) > 0:
            # print(queue[-1], [j,k])
            if queue[-1][1] > j:
              if (queue[-1][1] - queue[-1][0]) > (k - j):
                queue.pop()
                queue.append([j,k])
            else:
              queue.append([j,k])
          else:
            queue.append([j,k])
          j += 1
        elif presum[k] - presum[j] < target:
          k += 1
        else:
          j += 1
      if len(queue) < 2:
        return -1
      else:
        sq = sorted([x[1]-x[0] for x in queue])
        return sq[0] + sq[1]
```

##### 问题
上面的思路有一个漏洞，我是在遍历的过程中，遇到了相交的字串，就直接把之前的字串pop掉了。这明显是错误的。

如：`[[1,5], [3,6], [5,7]` 这种情况，当我的到`[3,6]`这一组的时候，我发现和`[1,5]`相交了，我就直接把`[1,5]`，去掉了。实际`[1,5]`和`[5,7]`不相交，所以这种做法是有问题的

**改进代码**

先记录所有和为target的字串，然后在遍历比较

尝试改一下代码，TLE！

#### 代码（TLE）
python3
```python
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
      presum = [0] * len(arr)
      temp = 0
      for i in range(len(arr)):
        presum[i] = temp + arr[i]
        temp += arr[i]
      presum = [0] + presum
      
      j = 0
      k = 1
      queue = []
      while j < len(presum) and k < len(presum):
        if presum[k] - presum[j] == target:
          if len(queue) > 0:
            queue.append([j,k])
          else:
            queue.append([j,k])
          j += 1
        elif presum[k] - presum[j] < target:
          k += 1
        else:
          j += 1

      r = []
      for i in range(len(queue) - 1):
        for j in range(i, len(queue)):
          if (queue[i][1] <= queue[j][0]):
            r.append((queue[j][1] - queue[j][0]) + (queue[i][1] - queue[i][0]))
      return -1 if len(r) == 0 else min(r)
```

超时的原因是最后有双for遍历和为`target`字串的操作，最坏情况$$O(n^2)$$，爆炸

**改进思路**

* 题目中有一个隐藏条件，数组中所有的数都是正整数，前缀和肯定是递增的。我们可以直接使用滑动窗口
* 使用辅助数组, `min_length[i]`表示，到i为止，之前所能找到的，和为`target`的最短的字串
* 当我们找到了一个和为`target`的子串`[start,end]`时，这个字串的长度再加上`min_length[i]`的长度，就是我们可能的结果
* 接着遍历，在获取到满足条件的字串时，再次获取可能的结果，和之前的结果比较，取较小的那个
* 遍历完成，即可获取最终的结果

尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def minSumOfLengths(self, arr: List[int], target: int) -> int:
    min_length = [math.inf] * len(arr)
    presum = 0 #前缀和
    start = 0 #字串的起始下标,end表示字串的结束下标
    cur_min = math.inf #当前见过的最小长度
    result = math.inf
    for end in range(len(arr)):
      presum += arr[end]
      while presum > target:
        presum -= arr[start]
        start += 1
      if presum == target:
        cur_len = end - start + 1
        if end > 0 and min_length[start-1] != math.inf:
          result = min(result, cur_len + min_length[start-1])
        cur_min = min(cur_len, cur_min)
      min_length[end] = min(min_length[end], cur_min)
    return -1 if result == math.inf else result
```