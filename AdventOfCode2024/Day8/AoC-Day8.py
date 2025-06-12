import collections
import itertools

def solve_resonant_collinearity(filepath='data.txt'):
    """
    Calculates the number of unique antinode locations within the map boundaries.
    """
    map_lines = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                map_lines.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None

    num_rows = len(map_lines)
    if num_rows == 0:
        return 0
    num_cols = len(map_lines[0])
    if num_cols == 0:
        return 0

    # Group antennas by their frequency (character)
    # Stores: { 'frequency_char': [(r1, c1), (r2, c2), ...], ... }
    antenna_map = collections.defaultdict(list)
    for r in range(num_rows):
        for c in range(num_cols):
            char = map_lines[r][c]
            if char != '.': # '.' indicates an empty space, not an antenna
                antenna_map[char].append((r, c))

    antinodes_set = set() # This set will store unique (row, col) tuples of antinodes

    # Iterate through each unique frequency found on the map
    for freq in antenna_map:
        antennas_for_freq = antenna_map[freq]

        # Antinodes are formed by *pairs* of antennas, so we need at least two antennas
        if len(antennas_for_freq) < 2:
            continue

        # Get all unique pairs of antennas for the current frequency
        # itertools.combinations(iterable, r) returns r-length tuples of elements
        # from the input iterable, without replacement, sorted order.
        for p1, p2 in itertools.combinations(antennas_for_freq, 2):
            r1, c1 = p1
            r2, c2 = p2

            # Calculate Antinode 1: Where P1 is the midpoint of (Antinode, P2)
            # This means Antinode is (2*P1 - P2)
            antinode_r1 = 2 * r1 - r2
            antinode_c1 = 2 * c1 - c2
            
            # Calculate Antinode 2: Where P2 is the midpoint of (Antinode, P1)
            # This means Antinode is (2*P2 - P1)
            antinode_r2 = 2 * r2 - r1
            antinode_c2 = 2 * c2 - c1

            # Check if Antinode 1 is within the map boundaries
            if 0 <= antinode_r1 < num_rows and 0 <= antinode_c1 < num_cols:
                antinodes_set.add((antinode_r1, antinode_c1))

            # Check if Antinode 2 is within the map boundaries
            if 0 <= antinode_r2 < num_rows and 0 <= antinode_c2 < num_cols:
                antinodes_set.add((antinode_r2, antinode_c2))
    
    return len(antinodes_set)

# --- Execution ---

# Test with the example input from the problem description
example_data = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
# Write example data to a temporary file for testing
with open("example_day8_data.txt", "w") as f:
    f.write(example_data.strip())

example_result = solve_resonant_collinearity("example_day8_data.txt")
print(f"Example result: {example_result}") # Expected: 14

# Now, solve with your actual puzzle input from 'data.txt'
actual_result = solve_resonant_collinearity('data.txt')
if actual_result is not None:
    print(f"Actual puzzle result: {actual_result}")
