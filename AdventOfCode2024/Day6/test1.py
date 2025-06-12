from collections import defaultdict
file_path = 'test.txt'
grid = []

def read_grid(file_path):
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f]
        return grid

def find_start(grid):
    for c in range(len(grid[0])):
        for r in range(len(grid[0])):
            if grid[r][c] == '^':
                return r, c, '^'
            elif grid[r][c] == '>':
                return r, c, '>'
            elif grid[r][c] == 'V':
                return r, c, 'V'
            elif grid[r][c] == '<':
                return r, c, '<'
    return None

def simulate_guard_movement(current_ypos, current_xpos, grid):
    # Check surroundings for any obstructions while before moving:
    if grid[current_ypos][current_xpos] == '^':
        # If facing up, check only space above it:
        if current_ypos > 0 and grid[current_ypos - 1][current_xpos] == '.':
            # Move one step in the same direction
            grid[current_ypos][current_xpos] = '.'
            current_ypos -= 1
            grid[current_ypos][current_xpos] = '^'
        elif current_ypos > 0 and grid[current_ypos - 1][current_xpos] == '#':
            # Obstacle in the way, need to turn right by 90 degrees
            grid[current_ypos][current_xpos] = '>'

    elif grid[current_ypos][current_xpos] == '>':
        # If facing right, check only space to the right:
        if current_xpos + 1 < len(grid[0]) and grid[current_ypos][current_xpos + 1] == '.':
            grid[current_ypos][current_xpos] = '.'
            current_xpos += 1
            grid[current_ypos][current_xpos] = '>'
        elif current_xpos + 1 < len(grid[0]) and grid[current_ypos][current_xpos + 1] == '#':
            grid[current_ypos][current_xpos] = 'V'

    elif grid[current_ypos][current_xpos] == 'V':
        # If facing down, check only space below it:
        if current_ypos + 1 < len(grid) and grid[current_ypos + 1][current_xpos] == '.':
            grid[current_ypos][current_xpos] = '.'
            current_ypos += 1
            grid[current_ypos][current_xpos] = 'V'
        elif current_ypos + 1 < len(grid) and grid[current_ypos + 1][current_xpos] == '#':
            grid[current_ypos][current_xpos] = '<'

    elif grid[current_ypos][current_xpos] == '<':
        # If facing left, check only space to the left:
        if current_xpos > 0 and grid[current_ypos][current_xpos - 1] == '.':
            grid[current_ypos][current_xpos] = '.'
            current_xpos -= 1
            grid[current_ypos][current_xpos] = '<'
        elif current_xpos > 0 and grid[current_ypos][current_xpos - 1] == '#':
            grid[current_ypos][current_xpos] = '^'
    else:
        print("Something went wrong!!")
    

    print("Done moving guard.")
    return grid

guard_positions = []
guard_information = {
    'x':0,
    'y':0,
    'dir':'^'
    }

grid = read_grid(file_path)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print(f'Total Rows:    {len(grid)}')    # Gets total number of ROWS
print(f'Total Columns: {len(grid[0])}') # Gets total number of COLUMNS in a ROW

start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")

start_row1, start_col1, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")

start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")

start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")

start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")

start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")

print("Moving Right NOW...")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
start_row, start_col, direction = find_start(grid)
print(f'Starting Point: Row: {start_row} Column: {start_col}\n\n')
guard_information['x'] = start_row
guard_information['y'] = start_col
guard_information['dir'] = direction
guard_positions.append(guard_information.copy())

grid = simulate_guard_movement(start_row, start_col, grid)
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
print(grid[5])
print(grid[6])
print(grid[7])
print(grid[8])
print(grid[9])
print("\n")
                 
print(guard_positions)
print(len(guard_positions))
