---
layout: default
title: git worktree 日常使用教程
---

### git worktree 日常使用教程

#### 什么是`git worktree`
git worktree 是git提供的连接到统一仓库的多个工作树，一个主仓库可以引出多个不同分支的工作树并行开发

#### 为什么要使用`git worktree`
开发中经常会遇到，不用的需求和功能在不同的分支上。当在开发新功能时，需要修改其他分支的功能，频繁的切换分支就相当麻烦，这时就可以使用`git worktree`

#### `git worktree` vs `git clone` 
`git worktree` 在表现结果上来看和`git clone`很接近。但是`git worktree`会同步本地仓库，本质上使用的是一个仓库。`git clone` 等于重开一个本地仓库，每次`clone` 也比较耗时

#### 如何使用
一下列出，常用的`git worktree`使用方法

**1.添加`worktree`**

```bash 
git worktree add [新路径] [分支]
```

操作之后会在只定路径生成新的目录，效果和`clone`一样，然后就可以在新目录上操作了

![](/public/images/2020-12-10-git-worktree-jiao-chen-1.png)

**2.列出所有`worktree`**

```bash
git worktree list
```

![](/public/images/2020-12-10-git-worktree-jiao-chen-2.png)

**3.删除`worktree`**
> 直接删除目录

然后执行

```bash
git worktree prune
```

![](/public/images/2020-12-10-git-worktree-jiao-chen-3.png)

**注意**

当存在worktree是某一个分支时，另一个worktree不能切到当前分支，如下图

![](/public/images/2020-12-10-git-worktree-jiao-chen-4.png)

**以上，轻松加愉快，可以嗨起来了**