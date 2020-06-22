---
layout: default
title: 模式匹配
---

## [面试题 16.18\. 模式匹配](https://leetcode-cn.com/problems/pattern-matching-lcci/)

> Medium

#### 思路

* 从示例开始分析，`a`的可能性是从空字符串到整个`value`字符串。同样`b`也是
* 以示例1为例，`pattern[0]` 为`a`，我们先列出`a`的可能性
* 当`a`确定了之后，我们再看`pattern[1]`，`pattern[1]`为`b`
* `b`没有确定过，所以`b`的可能性是从上一个确定的字符串剩下的开始到整个`value` 
* 下一个`pattern[2]`还是`b`，`b`已经确定过了，我们用`b`匹配剩下的内容。发现不一样，说明`b`的值确定的不正确，需要重新确认
* 指导整个`pattern`都与`value`都匹配完成

**显然使用递归来求解**

* 确定了`a`或`b`对应的子串之后，将剩下的`pattern`和`value`，抛给下一层递归
* 递归终止条件，`pattern`和`value` 都为空，表示匹配完成；确定了的子串，和剩下的`value`不匹配，终止，返回上层重新选择
* 有个变量要存放匹配过的`a`或`b`的子串
* `a`和`b`对应的子串应该不相同

尝试写一下代码,AC！

#### 代码
python3
```python
class Solution:
  def helper(self, pattern, value, match):
    if pattern == '' and value != '':
      return False
    if pattern == '' and value == '' :
      return True
    p = pattern[0]
    if match[p] != None:
      if value.startswith(match[p]):
        return self.helper(pattern[1:], value.replace(match[p], '', 1), match)
      else:
        return False
    for m in range(len(value) + 1):
      w = value[0:m]
      if match['a'] == w or match['b'] == w: #a或b已经匹配到了
        continue
      match[p] = w
      if (self.helper(pattern[1:], value.replace(match[p], '', 1), match)):
        return True
    
      match[p] = None
    return False

  def patternMatching(self, pattern: str, value: str) -> bool:
    return self.helper(pattern, value, {'a':None, 'b':None})
```