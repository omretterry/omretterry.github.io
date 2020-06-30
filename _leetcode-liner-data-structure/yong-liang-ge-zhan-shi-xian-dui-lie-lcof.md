---
layout: default
title: 用两个栈实现队列
---

## [剑指 Offer 09\. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

> Easy

#### 思路

* 栈和队列的区别，栈是前进后出，后进先出，是一个有底的杯子；队列，是先进先出，是一根管子
* 使用两个栈来实现队列的功能，我们可以想象成是两个杯子
* 加东西的时候我们往一个杯子里边加东西，要拿杯底的东西时，我们可以将一个杯子里的东西倒到另外一个杯子里
* 这时杯底的东西就到了面上，然后我们就可以拿到原来杯底的东西了
* 如果连续取底部的东西，我们可以不用倒回来，一直取。直到要再往里面加东西

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class CQueue:

    def __init__(self):
      self.putStack = []
      self.getStack = []

    def appendTail(self, value: int) -> None:
      if len(self.getStack) != 0:
        while len(self.getStack):
          self.putStack.append(self.getStack[-1])
          self.getStack.pop()
      self.putStack.append(value)

    def deleteHead(self) -> int:
      if len(self.getStack) == 0:
        if len(self.putStack) == 0:
          return -1
        while len(self.putStack):
          self.getStack.append(self.putStack[-1])
          self.putStack.pop()
      head = self.getStack[-1]      
      self.getStack.pop()
      return head
```

**优化** 

上面的代码每次要新增的时候都倒回原来的杯子，再添加，但是我们可以不用倒回去。

新增的就直接往杯子1里面加，需要取的时候再倒到要取的杯子里就行了

尝试优化一下代码，AC！

#### 代码
python3
```python
class CQueue:

    def __init__(self):
      self.putStack = []
      self.getStack = []

    def appendTail(self, value: int) -> None:
      self.putStack.append(value)

    def deleteHead(self) -> int:
      if len(self.getStack):
        return self.getStack.pop()
      if not len(self.putStack):
        return -1
      while len(putStack):
        self.getStack.append(self.putStack.pop())
      return self.getStack.pop()
```