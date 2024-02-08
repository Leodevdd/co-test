# https://leetcode.com/problems/number-of-islands/
from collections import deque


class Solution(object):
    def numIslands(self, grid):
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]
        count = 0

        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited[r][c] = True

            while q:
                cur_r, cur_c = q.popleft()
                print(f'r:{cur_r}, c:{cur_c},')

                for i in range(4):
                    next_r = cur_r + dr[i]
                    next_c = cur_c + dc[i]
                    if 0 <= next_r < row_len and 0 <= next_c < col_len:
                        if grid[next_r][next_c] == '1' and visited[next_r][next_c] == False:
                            q.append((next_r, next_c))
                            visited[next_r][next_c] = True

        for i in range(row_len):
            for j in range(col_len):
                # print(grid[i][j])
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    count += 1

        print(f"count: {count}")


Solution().numIslands(grid=[
    ["1", "1", "0", "1", "0"],
    ["1", "0", "1", "0", "1"],
    ["0", "1", "1", "0", "1"],
    ["1", "0", "0", "1", "1"]
]
)
