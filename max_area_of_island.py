class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, area = 0, 0
        visited = set()
        def dfs(grid: List[List[int]], i: int, j: int):
            
            if not 0 <= i < len(grid):
                return
            if not 0 <= j < len(grid[i]):
                return
            
            if grid[i][j] == 0:
                return
            
            if (i, j) in visited:
                return
            
            visited.add((i, j))
            
            grid_up = grid[i-1][j] if 0 <= i-1 < len(grid) else 0
            grid_down = grid[i+1][j] if 0 <= i+1 < len(grid) else 0
            grid_left = grid[i][j-1] if 0 <= j-1 < len(grid[i]) else 0
            grid_right = grid[i][j+1] if 0 <= j+1 < len(grid[i]) else 0
            nonlocal area
            area += 1
            if grid_up == 1 and (i-1, j) not in visited:
                dfs(grid, i-1, j)
            if grid_down == 1 and (i+1, j) not in visited:
                dfs(grid, i+1, j)
            if grid_left == 1 and (i, j-1) not in visited:
                dfs(grid, i, j-1)
            if grid_right == 1 and (i, j+1) not in visited:
                dfs(grid, i, j+1)
            
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                area = 0
                if grid[i][j] == 1:
                    dfs(grid, i, j)
                    print(area)
                else:
                    continue
                if area > max_area:
                    max_area = area
        
        return max_area