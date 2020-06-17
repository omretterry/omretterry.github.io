---
layout: default
---

## [1472\. 设计浏览器历史记录](https://leetcode-cn.com/problems/design-browser-history/)

#### 思路
周赛看到这道题都乐了，感觉对不起他的5分这个分数。感觉主要考察阅读理解。那首先就**阅读理解**一下
* 记录浏览器的访问记录，可以前进可以后退
* 后退返回之前的页面
* 前进访问返回前的页面
* 假如在当前页跳到一个新的页面，那之前的前进页就都作废。就是这时候就前进不了了

我们只要使用两个变量：
* **队列** 用于存放记录
* **当前页面索引** 用于存放当前访问的页面是哪个
* 接着处理一下*返回之后，转跳到新页面需要更新队列的情况*
* 考虑边界情况

AC！

#### 代码
python
```
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.queue = []
        self.queue.append(homepage)
        self.curindex = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if self.curindex < (len(self.queue) - 1):
          self.queue = self.queue[:self.curindex + 1][::]
        self.queue.append(url)
        self.curindex = len(self.queue) - 1


    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.curindex - steps < 0:
          self.curindex = 0
          return self.queue[0]
        else:
          self.curindex -= steps
          return self.queue[self.curindex]


    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.curindex + steps > len(self.queue) - 1:
          self.curindex = len(self.queue) - 1
          return self.queue[(len(self.queue) - 1)]
        else: 
          self.curindex += steps
          return self.queue[self.curindex]

```