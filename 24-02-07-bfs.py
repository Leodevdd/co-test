from collections import deque

grid = [
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 0, 1, 1],
]
row_len = len(grid)
col_len = len(grid[0])
visited = [[False] * col_len for _ in range(row_len)]

dr = [1, 0, -1, 0, 1, -1, 1, -1]
dc = [0, 1, 0, -1, -1, 1, 1, -1]
def bfs(r, c):
    q = deque()
    distance = 0
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        cur_r, cur_c, cur_distance = q.popleft()
        print(f'r:{cur_r}, c:{cur_c}, d:{cur_distance}')

        for i in range(8):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                if grid[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    q.append((next_r, next_c, cur_distance + 1))
                    visited[next_r][next_c] = True

bfs(0,0)