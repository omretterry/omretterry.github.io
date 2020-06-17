---
layout: default
---

## [739\. 每日温度](https://leetcode-cn.com/problems/daily-temperatures/)

> Medium

#### 思路

要求多少天后温度比现在高，我们使用双for爆破，遍历日期，在遍历一遍之后的日期，进行比较。TLE！

#### 代码（TLE）

python3
```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
      result = [0] * len(T)
      for i in range(len(T)):
        for j in range(i,len(T)):
          if T[j] > T[i]:
            result[i] = j - i
            break
      return result
```

**更新思路** 


学习一波大佬们的解题，获取新知识：**单调栈**


[李威威](https://leetcode-cn.com/u/liweiwei1419/)大神的回答是这样的：
```txt
分析这一类问题的思路是：
1.使用暴力解法
2.分析出过程中数据是先进后出的，所以使用栈
3.分析出为什么要维护栈中数据的单调性
4.栈内一般也会同时保存下标
5.多做题巩固
```
一般问题问左边第一个大的小的，右边第一个大的小的，我们可以想一下处是否能用单调栈求解。


回到这道题，用暴力解法我们看到遍历的时候数据先是暂存的，当遇到一个比自己大的数字是，这个结果就确认了，然后可以往下遍历。我们可以使用`递减栈`来存放温度和下标，当一个新来的温度比当前栈顶数据大时。出栈，并记录当前的下标之差，即过去天数多少钱，温度比当前出栈的大


如下，吴师兄解题中的动画。非常清晰，一目了然。


[https://leetcode-cn.com/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/](https://leetcode-cn.com/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/)

使用单调栈求解，AC！

#### 代码

python3
```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
      stack = []
      result = [0] * len(T)
      for i,t in enumerate(T):
        while len(stack) and t > stack[-1][1]:
          result[stack[-1][0]] = i - stack[-1][0]
          stack.pop()  
        stack.append([i,t])
      return result
```