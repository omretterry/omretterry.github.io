---
layout: default
title: 被围绕的区域
---

## [130\. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)

> Medium

#### 思路

看到这道题，感觉有点像岛屿数量。`X`是海洋的话，海洋中间的岛屿会沉。碰到边界的岛屿不会沉没。

* 使用**染色法**，从边界的点作为起点出发，如果是岛屿的话，就找上下左右四个方向上，连接的岛屿。
* 将这些连着边的岛屿设置成`A`，和原来的岛屿作区分
* 用`visited`记录已经访问过的节点，进行剪枝
* 最后将所有的`A`处理成`O`，将原来所有的`O`替换成`X`

以上，尝试一下代码，AC！

#### 代码
python3
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
      if len(board) == 0:
        return []
      dirs = [(0,-1),(0,1),(-1,0),(1,0)]
      rows = len(board)
      cols = len(board[0])

      def dfs(board, r, c, visited):
        board[r][c] = 'A'
        visited.add((r,c))
        for d in dirs:
          nr = r + d[0]
          nc = c + d[1]
          if nr < rows and nc < cols and nr >= 0 and nc >= 0 and (nr,nc) not in visited:
            if board[nr][nc] == 'O':
              dfs(board,nr,nc,visited)
        return 

      r = len(board)
      c = len(board[0])
      visited = set()
      for i in range(r):
        if board[i][0] == 'O':
          dfs(board, i, 0,visited)
        if board[i][c-1] == 'O':
          dfs(board, i, c-1,visited)
      for j in range(c):
        if board[0][j] == 'O':
          dfs(board,0,j,visited)
        if board[r-1][j] == 'O':
          dfs(board,r-1,j,visited)
          
      for i in range(r):
        for j in range(c):
          if board[i][j] == 'A':
            board[i][j] = 'O'
          elif board[i][j] == 'O':
            board[i][j] = 'X'
```