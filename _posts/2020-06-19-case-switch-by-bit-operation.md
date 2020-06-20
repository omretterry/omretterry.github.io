---
layout: default
title: 使用位运算进行大小写转换
---

#### 使用位运算进行大小写转换

**纯粹是炫技，了解就好**

```java

To Lower Case

('a' | ' ') = 'a'
('A' | ' ') = 'a'


To Upper Case

('b' | '_') = 'B'
('B' | '_') = 'B'

Switch Case

('d' ^ ' ') = 'D'
('D' ^ ' ') = 'd'
```

**Python用户的痛苦**

python中的str类型是不能直接使用位运算操作的

所以只能这样。。。
```python
chr(ord('A') ^ ord(' '))
```

算了算了，还是用`lower()`、`upper()`吧，我不配。