---
layout: default
---

## [1475\. 商品折扣后的最终价格](https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop/)

#### 思路
首先遍历商品，找到第一个满足条件的商品，计算出优惠后的价格，写入到`结果数组`中

#### 代码
python3
```
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
      result = prices[::]
      for i in range(len(prices)):
        for j in range(i+1, len(prices)):
          if prices[j] <= prices[i]:
            result[i] -= prices[j]
            break
      return result
```

**改进思路** 

看到右边第一个，考虑是否可以用单调栈来求解。需要有一定思考过程，周赛考虑时间因素没有选用这种方案，感兴趣的小伙伴可以尝试一下。