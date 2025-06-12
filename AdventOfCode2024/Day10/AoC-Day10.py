from collections import deque

def parse_grid(lines):
    return [[int(ch) for ch in line.strip()] for line in lines]

def get_neighbors(x, y, max_x, max_y):
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < max_x and 0 <= ny < max_y:
            yield nx, ny

def find_reachable_9s(grid, start_x, start_y):
    visited = set()
    q = deque()
    q.append((start_x, start_y, 0))  # x, y, current_height
    visited.add((start_x, start_y))
    found_nines = set()
    max_x, max_y = len(grid), len(grid[0])

    while q:
        x, y, h = q.popleft()
        for nx, ny in get_neighbors(x, y, max_x, max_y):
            if (nx, ny) not in visited:
                if grid[nx][ny] == h + 1:
                    visited.add((nx, ny))
                    if grid[nx][ny] == 9:
                        found_nines.add((nx, ny))
                    else:
                        q.append((nx, ny, h + 1))
    return found_nines

def calculate_total_score(grid):
    total_score = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                reachable_9s = find_reachable_9s(grid, x, y)
                total_score += len(reachable_9s)
    return total_score

# Example usage
with open("data.txt") as f:
    lines = f.readlines()

grid = parse_grid(lines)
total = calculate_total_score(grid)
print("Total score:", total)
