import collections
import itertools
import math

def solve_resonant_collinearity_part2(filepath='data.txt'):
    """
    Calculates the number of unique antinode locations within the map boundaries
    according to the Part Two rules.
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

    # Group antennas by their frequency character
    # Stores: { 'frequency_char': [(r1, c1), (r2, c2), ...], ... }
    antenna_map = collections.defaultdict(list)
    for r in range(num_rows):
        for c in range(num_cols):
            char = map_lines[r][c]
            if char != '.': # '.' indicates an empty space, not an antenna
                antenna_map[char].append((r, c))

    # This set will store unique lines found for each frequency.
    # A line is uniquely identified by (sdr, sdc, constant_value).
    # `sdr`, `sdc` are simplified direction vector components.
    # `constant_value` comes from the line equation: `sdc * r - sdr * c = constant_value`
    unique_lines_by_freq = collections.defaultdict(set)

    # Iterate through each unique frequency to find all unique lines formed by its antennas
    for freq in antenna_map:
        antennas_for_freq = antenna_map[freq]

        # Lines are formed by *pairs* of antennas; need at least two antennas
        if len(antennas_for_freq) < 2:
            continue

        # Get all unique pairs of antennas for the current frequency
        for p1, p2 in itertools.combinations(antennas_for_freq, 2):
            r1, c1 = p1
            r2, c2 = p2

            dr = r2 - r1 # Change in row
            dc = c2 - c1 # Change in column

            if dr == 0 and dc == 0: # If points are identical, skip (shouldn't happen with combinations)
                continue
            
            # Calculate the greatest common divisor to simplify the direction vector
            common_divisor = math.gcd(abs(dr), abs(dc))
            sdr = dr // common_divisor # Simplified change in row
            sdc = dc // common_divisor # Simplified change in column

            # Canonicalize the simplified step vector (sdr, sdc)
            # This ensures that (1,1) and (-1,-1) are treated as the same direction, etc.
            if sdr < 0 or (sdr == 0 and sdc < 0):
                sdr = -sdr
                sdc = -sdc
            
            # Calculate the canonical constant for the line equation: sdc * r - sdr * c = constant_value
            # This constant is unique for each line.
            constant_value = sdc * r1 - sdr * c1
            
            unique_lines_by_freq[freq].add((sdr, sdc, constant_value))

    antinodes_set = set() # This set will store all unique (row, col) coordinates of antinodes

    # Now, for each unique line identified, find all grid points on it that are within bounds
    for freq in unique_lines_by_freq:
        for sdr, sdc, constant_value in unique_lines_by_freq[freq]:
            # Handle horizontal lines (sdr == 0)
            if sdr == 0:
                # Equation: sdc * r = constant_value
                # Since sdc is canonicalized to 1 (or -1, but for sdr=0 it's 1), r = constant_value / sdc
                # Check if the calculated row is within bounds
                fixed_r = constant_value // sdc # sdc will be 1 or -1 here
                if 0 <= fixed_r < num_rows:
                    # All columns in this row are antinodes for this line
                    for current_c in range(num_cols):
                        antinodes_set.add((fixed_r, current_c))
            
            # Handle vertical lines (sdc == 0)
            elif sdc == 0:
                # Equation: -sdr * c = constant_value => sdr * c = -constant_value
                # Since sdr is canonicalized to 1, c = -constant_value / sdr
                fixed_c = -constant_value // sdr # sdr will be 1 here
                if 0 <= fixed_c < num_cols:
                    # All rows in this column are antinodes for this line
                    for current_r in range(num_rows):
                        antinodes_set.add((current_r, fixed_c))
            
            # Handle diagonal lines (sdr != 0 and sdc != 0)
            else:
                # Iterate through all possible rows in the grid
                for r_iter in range(num_rows):
                    # From `sdc * r_iter - sdr * c_iter = constant_value`, solve for c_iter:
                    # sdr * c_iter = sdc * r_iter - constant_value
                    # c_iter = (sdc * r_iter - constant_value) / sdr
                    numerator_c = sdc * r_iter - constant_value
                    if numerator_c % sdr == 0: # Check if c_iter is an integer
                        c_iter = numerator_c // sdr
                        # If c_iter is within column bounds, add it to antinodes_set
                        if 0 <= c_iter < num_cols:
                            antinodes_set.add((r_iter, c_iter))
                
                # Iterate through all possible columns in the grid (redundant but safe way to catch all points)
                # The set will automatically handle any duplicate points added.
                for c_iter in range(num_cols):
                    # From `sdc * r_iter - sdr * c_iter = constant_value`, solve for r_iter:
                    # sdc * r_iter = constant_value + sdr * c_iter
                    # r_iter = (constant_value + sdr * c_iter) / sdc
                    numerator_r = constant_value + sdr * c_iter
                    if numerator_r % sdc == 0: # Check if r_iter is an integer
                        r_iter = numerator_r // sdc
                        # If r_iter is within row bounds, add it to antinodes_set
                        if 0 <= r_iter < num_rows:
                            antinodes_set.add((r_iter, c_iter))

    return len(antinodes_set)

# --- Execution ---

# Test with the example input from Part Two's description (which is the original example map)
original_example_map_str = """
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
with open("example_day8_part2_test_data.txt", "w") as f:
    f.write(original_example_map_str.strip())

example_result_part2 = solve_resonant_collinearity_part2("example_day8_part2_test_data.txt")
print(f"Example result (Part 2): {example_result_part2}") # Expected: 34

# Now, calculate the result for your actual puzzle input from 'data.txt'
actual_result_part2 = solve_resonant_collinearity_part2('data.txt')
if actual_result_part2 is not None:
    print(f"Actual puzzle result (Part 2): {actual_result_part2}")
