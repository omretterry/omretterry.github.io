---
layout: default
---

## [两个盒子中球的颜色数相同的概率](https://leetcode-cn.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)

#### 思路
根据Hard必死定律，周赛没做出来，继续拜读大佬解题
**阅读理解** 
* 这道题的中文翻译稍微有点容易出现误解，还是需要多读几遍理解意思
* 大概意思是：有两个盒子，需要把球随机的放到这两个盒子当中
* 最后计算两个盒子中颜色数相同情况的概率
* 题目要求 `请计算「两个盒子中球的颜色数相同」的情况的概率。`，比如说盒子1有3种颜色，盒子2也有三种颜色，不管颜色是什么。 这种情况都是符合条件的

**分析**
* 所有的可能性，就是全排列的组合数，如下：（图片来自[huahua](https://space.bilibili.com/9880352?from=search&seid=1276580199457930821)大佬，我是[huahua](https://space.bilibili.com/9880352?from=search&seid=1276580199457930821)大佬的小迷弟，大家可以关注一波）![](../images/screenshot_1591350866551.png)
对于示例2，应该有`$ 4! $`种可能性，但是1，2重复，这边需要去重，一共就为12中可能，如上图。全排列+去重，联想到 [47\. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)。
* 可以取出全排列的数量，然后在除以相同颜色的数量阶乘乘积，得到去重之后的排列组合数。
* 接着从中遍历出满足题目要求的，颜色数量相同的情况，进行比较得出答案

不出意外的TLE（苦），偶然发现 [国际版暴力解法](https://leetcode-cn.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/solution/zhuan-ge-guo-ji-ban-ben-de-bao-li-jie-fa-you-mei-d/)，居然可以AC！而且代码非常简洁，大佬牛批！

#### 代码
python3
```
class Solution:
    def multinomial(self, n):
        return factorial(sum(n))/prod([factorial(i) for i in n])
  
    def getProbability(self, balls):
        k, n, Q = len(balls), sum(balls)// 2, 0
        arrays = [range(0,i+1) for i in balls]
        t = list(product(*arrays))
        for i in range(len(t)):
            if sum(t[i]) == n and t[i].count(0) == t[-i-1].count(0):
                Q += self.multinomial(t[i]) * self.multinomial(t[-i-1]) 

        return Q / self.multinomial(list(balls))
```

本题TLE优化方案，可以使用**动态规划**进行求解。dp正在研究中，大家请耐心等待（菜鸡的挣扎）
未完待续。。。
