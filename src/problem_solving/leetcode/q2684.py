from collections import deque
from functools import lru_cache


class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        """
        From a cell (row, col), you can move to any of the cells:
        - (row - 1, col + 1)
        - (row, col + 1)
        - (row + 1, col + 1)
        such that the value of the cell you move to should be strictly bigger than the value of the current cell

        Let's think about how to do this recursively. Then optimize

        The current solution we have will hit a memory limit error
        """
        rows, cols, dirs = len(grid), len(grid[0]), ((0, 1), (1, 1), (-1, 1))

        @lru_cache
        def dp(row: int, col: int) -> int:
            ans = 0
            for drow, dcol in dirs:
                nrow, ncol = row + drow, col + dcol
                if (
                    0 <= nrow < rows
                    and 0 <= ncol < cols
                    and grid[row][col] < grid[nrow][ncol]
                ):
                    ans = max(ans, 1 + dp(nrow, ncol))
            return ans

        return max(dp(i, 0) for i in range(rows))

    def maxMoves_memory_limit(self, grid: list[list[int]]) -> int:
        """
        From a cell (row, col), you can move to any of the cells:
        - (row - 1, col + 1)
        - (row, col + 1)
        - (row + 1, col + 1)
        such that the value of the cell you move to should be strictly bigger than the value of the current cell

        Let's think about how to do this recursively. Then optimize

        The current solution we have will hit a memory limit error
        """
        res = 0

        for i in range(len(grid)):
            res = max(res, self.find_max(grid, i, 0))

        return res

    def find_max(self, grid: list[list[int]], row: int, col: int) -> int:
        """
        We can only go from left to right, but we can go either up or down
        """
        queue = deque()
        queue.append((row, col, 0))

        _max = 0

        while queue:
            crow, ccol, count = queue.popleft()

            prev = grid[crow][ccol]

            for drow, dcol in ((-1, 1), (0, 1), (1, 1)):
                nrow = crow + drow
                ncol = ccol + dcol

                if nrow < 0 or ncol < 0 or nrow >= len(grid) or ncol >= len(grid[0]):
                    continue

                if grid[nrow][ncol] > prev:
                    _max = max(_max, count + 1)
                    queue.append((nrow, ncol, count + 1))

        return _max
