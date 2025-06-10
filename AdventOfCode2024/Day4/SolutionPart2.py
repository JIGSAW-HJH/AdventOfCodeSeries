import re

def solve_part_two():
    word_search_grid = []
    
    # Read file line by line directly (most robust for text files)
    with open("data.txt") as f:
        for line in f:
            cleaned_line = line.strip() 
            if cleaned_line: # Only append non-empty lines (after stripping whitespace)
                word_search_grid.append(list(cleaned_line))

    R = len(word_search_grid) 
    
    # --- START DEBUGGING GRID STRUCTURE ---
    print(f"\n--- Debugging Grid Structure ---")
    print(f"Total rows (R): {R}")

    if R == 0:
        print("Grid is empty after parsing. Cannot proceed.")
        print("--- End Debugging Grid Structure ---\n")
        print("Part Two Answer: 0 (Grid is empty)")
        return
    
    # Assuming first row is representative for initial C, but will use individual row lengths for safety
    C = len(word_search_grid[0]) 
    print(f"Columns in first row (C): {C}")

    print(f"\nFirst 5 rows (or fewer if grid is small):")
    for i in range(min(5, R)):
        # Print actual length of each row and its first few characters
        print(f"  Row {i} (length {len(word_search_grid[i])}): {''.join(word_search_grid[i][:min(10, len(word_search_grid[i]))])}...") 

    print(f"\nLast 5 rows (or fewer):")
    for i in range(max(0, R-5), R):
        # Print actual length of each row and its first few characters
        print(f"  Row {i} (length {len(word_search_grid[i])}): {''.join(word_search_grid[i][:min(10, len(word_search_grid[i]))])}...") 
    
    # Check for jagged rows and any truly empty rows
    has_jagged_rows = False
    has_empty_rows = False
    for r_idx, row in enumerate(word_search_grid):
        if len(row) != C:
            print(f"  WARNING: Row {r_idx} has inconsistent length {len(row)}, expected {C} (from first row).")
            has_jagged_rows = True
        if not row: # Check if a row itself is an empty list
            print(f"  CRITICAL WARNING: Row {r_idx} is an empty list ([]).")
            has_empty_rows = True

    if not has_jagged_rows:
        print("  All rows appear to have consistent length (based on first row).")
    if not has_empty_rows:
        print("  No rows are empty lists (after stripping/filtering).")
    print(f"--- End Debugging Grid Structure ---\n")
    # --- END DEBUGGING GRID STRUCTURE ---


    xmas_pattern_count = 0

    # Iterate through possible center positions (r, c) for the 'A' character.
    # 'r' from 1 to R-2, 'c' from 1 to C-2, ensuring 3x3 pattern can be formed.
    # If R < 3 or C < 3, these ranges will be empty, and the loops won't run,
    # correctly returning 0 count.
    for r in range(1, R - 1): 
        for c in range(1, C - 1): 
            
            # Condition 1: The character at the current center position must be 'A'
            if word_search_grid[r][c] == 'A':
                
                # --- CRITICAL BOUNDARY CHECKS FOR THE 4 CORNERS ---
                # These checks are *absolutely necessary* to prevent IndexError,
                # especially if the grid is indeed jagged (rows have different lengths).
                
                # Top-Left (r-1, c-1)
                # Check if the target column (c-1) is valid for the row (r-1)
                if not (0 <= c-1 < len(word_search_grid[r-1])):
                    # print(f"DEBUG: Skipping ({r},{c}) - TL out of bounds for row {r-1}") # Optional debug
                    continue
                
                # Top-Right (r-1, c+1)
                # Check if the target column (c+1) is valid for the row (r-1)
                if not (0 <= c+1 < len(word_search_grid[r-1])):
                    # print(f"DEBUG: Skipping ({r},{c}) - TR out of bounds for row {r-1}") # Optional debug
                    continue
                
                # Bottom-Left (r+1, c-1)
                # Check if the target column (c-1) is valid for the row (r+1)
                if not (0 <= c-1 < len(word_search_grid[r+1])):
                    # print(f"DEBUG: Skipping ({r},{c}) - BL out of bounds for row {r+1}") # Optional debug
                    continue
                
                # Bottom-Right (r+1, c+1)
                # Check if the target column (c+1) is valid for the row (r+1)
                if not (0 <= c+1 < len(word_search_grid[r+1])):
                    # print(f"DEBUG: Skipping ({r},{c}) - BR out of bounds for row {r+1}") # Optional debug
                    continue
                # --- END CRITICAL BOUNDARY CHECKS ---
                
                # If we've reached this point, all 5 characters needed for the X-MAS pattern
                # are guaranteed to be within valid bounds of their respective rows.
                char_tl = word_search_grid[r-1][c-1] 
                char_tr = word_search_grid[r-1][c+1] 
                char_bl = word_search_grid[r+1][c-1] 
                char_br = word_search_grid[r+1][c+1] 

                # Conditions for the two diagonals forming "MAS" or "SAM"
                diag1_valid = False
                if (char_tl == 'M' and char_br == 'S') or \
                   (char_tl == 'S' and char_br == 'M'):
                    diag1_valid = True
                
                diag2_valid = False
                if (char_tr == 'M' and char_bl == 'S') or \
                   (char_tr == 'S' and char_bl == 'M'):
                    diag2_valid = True
                
                if diag1_valid and diag2_valid:
                    xmas_pattern_count += 1
                    
    print(f"Part Two Answer: {xmas_pattern_count}")

# Call the function for Part Two
solve_part_two()
