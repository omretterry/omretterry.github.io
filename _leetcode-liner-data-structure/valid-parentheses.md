---
layout: default
title: 有效的括号
---

## [20\. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

> Easy

#### 思路

使用**栈**求解，想象一下我们在玩消消乐游戏。

* 将成对的扩号放到字典中，字典键值匹配的说明是可以消除的括号对
* 栈顶元素和当前字符匹配，如果成消掉，就将栈顶元素删除。如果不能消掉就把当前元素入栈
* 最后栈中全部都消掉说明括号有效，如果不能消掉说明不是有效的括号

以上，AC！

#### 代码
python3
```python
class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    pairs = {'{':'}','(':')','[':']'}
    for l in s:
    if len(stack) == 0:
        stack.append(l)
        continue
    pre = stack[-1]
    if pre in pairs and pairs[pre] == l:
        stack.pop()
    else:
        stack.append(l)
    return len(stack) == 0
      
```