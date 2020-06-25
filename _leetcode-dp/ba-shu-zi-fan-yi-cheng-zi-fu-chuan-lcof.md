---
layout: default
---

## [面试题46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)

> Medium

#### 思路

首先分析一下题目，对于例子`12258`

* 第一个字母可以选`1` 或 `12`，`122` 选不了了，因为`122` 超过了$$ [0, 25] $$ 范围。
* 如果第一个字母选了`1`，第二个可选`2`或`22`来翻译；如果第一个拿个`12`来翻译，第二个可以选`2`或`25`来翻译。
* 明显的，我们选择形成了一个树状的结构，如下图

![](/public/images/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof-1.png)

* 树的最后的子节点的个数，即我们最终的可翻译的方法。
* 可看到分支很多都是相同的，比如图中`2258`的子分支也出现在`258`的子分支当中，使用记忆化递归
* 中间有个小陷阱，有`0`的情况需要考虑进去

尝试使用递归求解，AC！

#### 代码
python3
```python
class Solution:
    @lru_cache(None)
    def dfs(self, res):
      if res == '':
        return 1
      if int(res) < 10:
        return 1
      result = 0
      if int(res[0:2]) < 26 and int(res[0:2]) > 9:
        result += self.dfs(res[2:])
      result += self.dfs(res[1:])
      return result
      
    def translateNum(self, num: int) -> int:
      return self.dfs(str(num))
```

细心的小伙伴发现我们这道题放在了dp类别中，我们这题也可以使用动态规划来做。（很多的dp题，我们都可以先考虑记忆化递归的方法，然后再转化成bottom-up 动态规划方法，这样个人感觉思路会比较清晰）

#### 转换思路

* 我们从上面的图可以看到，我们可以从最后的`8`为最小的元素，从下向上计算
* 使用这种方式计算，所有上层的结果都可以从我们已有的结果中获取
* 其实这就是bottom-up的思想
* 对于我们这题，从前到后翻译和从后到前翻译，对于结果没有影响。上图中的自底向上，是从最后一个数字来考虑。暂时先忘了他，我们还是按正常思维从前到后来思考dp方法
* 构建dp数组，`dp[i]`表示翻译到第i个数字时，可能的翻译数量
* 对于`dp[i]`来说，有两种可能性：可能是从`dp[i-1]`然后再加上第`i`个数字翻译过来，也有可能从`dp[i-2]`然后再加上第`i-1`和`i`个数字，组成的翻译
* 第`i-1`和第`i`个数子组成的数字，在`[10,25]`返回内才满足上述的第二种可能性
* 通过上述思考我们可以得到**状态转移方程** ：

![](/public/images/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-2.png)


* `dp[0] = 1`, 为了符合通项，我们设置0的情况的值为1
尝试编写一下代码，AC！

#### 代码
python3
```python
class Solution:
    def translateNum(self, num: int) -> int:
      dp = [0] * (len(str(num)) + 1)
      dp[0] = 1
      dp[1] = 1
      for i in range(2, len(str(num)) + 1):
        temp = int(str(num)[i-2:i])
        if temp > 9 and temp < 26:
          dp[i] += dp[i-2]
        dp[i] += dp[i-1]
      print(dp)
      return dp[-1]
```

