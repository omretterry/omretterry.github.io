---
layout: default
---

## [1471\. 数组中的 k 个最强值](https://leetcode-cn.com/problems/the-k-strongest-values-in-an-array/)

#### 思路
说下我的思路
* 先算出中位数
* 遍历数组，算出每个数和中位数的差值，保存
* 同时保存下标，应为当差值相同是，下标也要作为权重的判断依据
* 将数组按规则进行排序
* 返回前k个值

AC！

#### 代码
python
```
class Solution:
    def getStrongest(self, arr, k):
      s = sorted(arr)
      mindex = (len(s) - 1) // 2
      mvalue = s[mindex]
      temp = []
      for i in s:
        temp.append([abs(i-mvalue),i])
      def sorttemp(s1,s2):
        if s1[0] < s2[0]:
          return 1
        if s1[0] > s2[0]:
          return -1
        if s1[0] == s2[0] and s1[1] > s2[1]:
          return -1
        return 1
      return [x[1] for x in sorted(temp, sorttemp)[:k]]
```

#### 代码（大佬精简版）
python
```
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr = sorted(arr)
        mid = arr[(n - 1) // 2]
        def mykey(x):
            return (abs(x - mid), x)
        arr = sorted(arr, key=mykey)
        return arr[n - k:]
```

**改进思路** 

使用**排序+双指针**
* 先将数组排序，算出中位数
* 两个指针分别指向排好序的数组的两端
* 应为和中位数的差值最大，也就是距离最远，肯定是越靠近两端的约大
* 比较两个指针的值和下标，分别向中间靠近，得到前k个值，即结果

周赛时考虑上面一种方法写起来较快，而且没有TLE。双指针方法，没有尝试，代码暂略。感兴趣的小伙伴可以尝试一下。