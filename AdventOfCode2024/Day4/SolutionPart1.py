import re

def solve():
    word_search_grid = []
    
    # Reads the entire content of the file.
    with open("data.txt") as f: # Ensure this is 'data.txt' for your larger grids
        data = f.read()

    # Splits the content into lines and cleans each line.
    lines = data.strip().split('\n') 
    for line in lines:
        cleaned_line = line.strip() 
        if cleaned_line:
            word_search_grid.append(list(cleaned_line))

    # R (number of rows) is dynamically determined.
    R = len(word_search_grid) 
    if R == 0:
        print(0)
        return
    
    # C is determined by the length of the first row. 
    # This is primarily for debugging/initial dimension knowledge.
    # The loops will use the actual row lengths for robustness.
    C = len(word_search_grid[0]) 

    # --- Debugging Prints for Grid Integrity (Highly Recommended for this issue) ---
    print(f"DEBUG: Constructed Grid Dimensions: R={R}, C={C} (based on first row)")
    for r_idx, row in enumerate(word_search_grid):
        if len(row) != C:
            print(f"DEBUG: WARNING: Row {r_idx} has inconsistent length {len(row)}, expected {C} (from first row). This means your grid is NOT perfectly rectangular!")
            # If you see this warning, your input file needs to be checked for extra spaces or missing characters on lines.
    # --- End Debugging Prints ---

    target_word = "XMAS"
    target_len = len(target_word) 

    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    count = 0

    # Iterate through every cell in the grid
    for r in range(R): 
        # CRITICAL CHANGE HERE: Iterate over columns based on the actual length of the current row (word_search_grid[r])
        # This handles cases where rows might have different lengths.
        current_row_length = len(word_search_grid[r]) 
        for c in range(current_row_length): 
            for i in range(8): 
                current_word = ""
                for k in range(target_len):
                    nr = r + k * dr[i]
                    nc = c + k * dc[i]

                    # CRITICAL CHANGE HERE: Robust Boundary Check
                    # 1. Check if the calculated row index 'nr' is within grid boundaries.
                    if not (0 <= nr < R):
                        break # Out of row bounds, stop building word in this direction

                    # 2. Check if the calculated column index 'nc' is within the bounds
                    #    of the *specific row 'word_search_grid[nr]'* being accessed.
                    #    This handles jagged arrays correctly.
                    if not (0 <= nc < len(word_search_grid[nr])): 
                        break # Out of column bounds for this specific row, stop building word

                    current_word += word_search_grid[nr][nc]

                if len(current_word) == target_len:
                    if current_word == target_word: 
                        count += 1
    
    print(count)

solve()
