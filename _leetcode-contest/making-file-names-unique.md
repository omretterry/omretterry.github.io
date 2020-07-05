---
layout: default
title: 保证文件名唯一
---

## [1487\. 保证文件名唯一](https://leetcode-cn.com/problems/making-file-names-unique/)

> Medium

#### 思路

分享一下我的思路

使用一个容器保存已经创建的文件名，如果文件已经存在，在文件后添加文件后缀。这个过程中，使用一个计数对象，用于记录后缀的数字

**问题** 这道题思路不难想，但是容器的选择很重要，不然就会TLE。这边选择Hash Map来进行优化

最终AC！

#### 代码
python3
```python
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
      r = []
      s = set()
      cache = collections.defaultdict(int)
      for n in names:
        tn = n
        k = cache[n] if cache[n] != 0 else 1
        while tn in s:
          tn = n + "(" + str(k) + ")"
          k += 1
        cache[n] = k
        s.add(tn)
        r.append(tn)
      return r
```