from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]
        q = deque()
        distance = 1
        q.append((0, 0, distance))
        visited[0][0] = True

        # directions
        # 4 8 3
        # 7   5
        # 2 6 1
        dr = [1, -1, 1, -1, 1, 0, -1, 0]
        dc = [1, 1, -1, -1, 0, 1, 0, -1]

        # exception: top-right cell
        if row_len == 1 and col_len == 1:
            return 1 if grid[0][0] == 0 else -1
        elif grid[0][0] == 1:
            return -1


        while q:
            cur_r, cur_c, distance = q.popleft()

            for i in range(len(dr)):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                # exception: out of range
                if 0 <= next_r < row_len and 0 <= next_c < col_len:
                    # select next cell
                    if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        # bottom-right cell
                        if next_r == row_len - 1 and next_c == col_len - 1:
                            return distance + 1

                        q.append((next_r, next_c, distance + 1))
                        visited[next_r][next_c] = True

        return -1


a = Solution()
print(a.shortestPathBinaryMatrix(grid=[[0]]))
