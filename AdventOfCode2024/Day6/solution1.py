from typing import List, Tuple, Set

DIRECTIONS = ['^', '>', 'v', '<']
DELTAS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

def turn_right(current: str) -> str:
    idx = DIRECTIONS.index(current)
    return DIRECTIONS[(idx + 1) % 4]

def simulate_guard_loop(grid: List[List[str]], y: int, x: int, dir: str) -> bool:
    rows, cols = len(grid), len(grid[0])
    seen_states: Set[Tuple[int, int, str]] = set()

    while True:
        state = (y, x, dir)
        if state in seen_states:
            return True  # Loop detected
        seen_states.add(state)

        dy, dx = DELTAS[dir]
        ny, nx = y + dy, x + dx

        if not (0 <= ny < rows and 0 <= nx < cols):
            return False  # Guard leaves the map

        if grid[ny][nx] == '#':
            dir = turn_right(dir)
        else:
            y, x = ny, nx

def find_guard(grid: List[List[str]]) -> Tuple[int, int, str]:
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val in DIRECTIONS:
                dir = val
                grid[y][x] = '.'  # Clear the guard position
                return y, x, dir
    raise ValueError("Guard not found")

def count_valid_obstacle_positions(grid: List[List[str]]) -> int:
    start_y, start_x, start_dir = find_guard(grid)
    rows, cols = len(grid), len(grid[0])
    count = 0

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] != '.' or (y == start_y and x == start_x):
                continue

            grid[y][x] = '#'  # Temporarily place obstacle
            if simulate_guard_loop(grid, start_y, start_x, start_dir):
                count += 1
            grid[y][x] = '.'  # Restore

    return count


print("opening data.txt file...")
with open('data.txt') as f:
    lines = [list(line.strip()) for line in f if line.strip()]
print("Done reading data.txt file")

result = count_valid_obstacle_positions(lines)
print(result)
print(f"Valid obstacle positions that create loops: {result}")

