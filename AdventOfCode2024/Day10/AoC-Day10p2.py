from functools import lru_cache

def parse_grid(lines):
    return [[int(ch) for ch in line.strip()] for line in lines]

def get_neighbors(x, y, max_x, max_y):
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < max_x and 0 <= ny < max_y:
            yield nx, ny

def calculate_total_rating(grid):
    max_x, max_y = len(grid), len(grid[0])

    @lru_cache(maxsize=None)
    def count_trails(x, y):
        current_height = grid[x][y]
        if current_height == 9:
            return 1  # Reached a 9, one complete trail

        total = 0
        for nx, ny in get_neighbors(x, y, max_x, max_y):
            if grid[nx][ny] == current_height + 1:
                total += count_trails(nx, ny)
        return total

    total_rating = 0
    for x in range(max_x):
        for y in range(max_y):
            if grid[x][y] == 0:
                total_rating += count_trails(x, y)

    return total_rating

# Example usage
with open("data.txt") as f:
    lines = f.readlines()

grid = parse_grid(lines)
total = calculate_total_rating(grid)
print("Total rating:", total)
