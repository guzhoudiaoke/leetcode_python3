class Solution(object):
    def numIslands1(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(r, c):
            if grid[r][c] != '1':
                return

            grid[r][c] = '@'
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r+dr, c+dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                    dfs(r+dr, c+dc)


        if len(grid) == 0:
            return 0

        if len(grid[0]) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    ans += 1
        return ans


    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(r, c):
            if grid[r][c] != '1':
                return

            grid[r][c] = '@'
            if r+1 < rows:
                dfs(r+1, c)
            if r-1 >= 0:
                dfs(r-1, c)
            if c+1 < cols:
                dfs(r, c+1)
            if c-1 >= 0:
                dfs(r, c-1)


        if len(grid) == 0:
            return 0

        if len(grid[0]) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    ans += 1
        return ans



    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(r, c):
            grid[r][c] = '@'
            if r+1 < rows and grid[r+1][c] == '1':
                dfs(r+1, c)
            if r-1 >= 0 and grid[r-1][c] == '1':
                dfs(r-1, c)
            if c+1 < cols and grid[r][c+1] == '1':
                dfs(r, c+1)
            if c-1 >= 0 and grid[r][c-1] == '1':
                dfs(r, c-1)


        if len(grid) == 0:
            return 0

        if len(grid[0]) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    ans += 1
        return ans

        
sol = Solution()
grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
print(sol.numIslands(grid))


grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(sol.numIslands(grid))
