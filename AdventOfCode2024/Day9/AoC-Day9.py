def solve_disk_fragmenter():
    # Read the single-line disk map input from 'data.txt'
    try:
        with open('data.txt', 'r') as f:
            disk_map_str = f.readline().strip()
    except FileNotFoundError:
        print("Error: 'data.txt' not found. Please ensure the input file is in the correct directory.")
        return None

    # Step 1: Parse the disk map string into a list representing disk blocks.
    # Each element will be the file ID (0, 1, 2...) or -1 for free space.
    disk = []
    file_id_counter = 0
    is_file_length = True # Flag to alternate between file length and free space length

    for char_digit in disk_map_str:
        length = int(char_digit)
        if is_file_length:
            # Add file blocks with the current file ID
            for _ in range(length):
                disk.append(file_id_counter)
            file_id_counter += 1 # Increment file ID for the next file encountered
        else:
            # Add free space blocks (-1)
            for _ in range(length):
                disk.append(-1)
        is_file_length = not is_file_length # Toggle the flag for the next digit

    # Step 2: Compact the disk using two pointers.
    current_free_idx = 0 # Pointer for the leftmost free space block
    current_file_idx = len(disk) - 1 # Pointer for the rightmost file block

    while True:
        # Advance current_free_idx to find the next leftmost free space.
        while current_free_idx < len(disk) and disk[current_free_idx] != -1:
            current_free_idx += 1
        
        # Advance current_file_idx to find the next rightmost file block.
        while current_file_idx >= 0 and disk[current_file_idx] == -1:
            current_file_idx -= 1
        
        # Check the stop condition for compaction:
        # 1. current_free_idx has gone past the end of the disk (no more free space).
        # 2. current_free_idx has caught up with or passed current_file_idx. This means all file blocks
        #    are now contiguous at the beginning, and any remaining free spaces are at the very end.
        if current_free_idx >= len(disk) or current_free_idx >= current_file_idx:
            break
        
        # If not stopped, a move is necessary:
        # Get the file ID from the rightmost file block's position.
        file_id_to_move = disk[current_file_idx]
        
        # Place this file block into the leftmost free space.
        disk[current_free_idx] = file_id_to_move
        
        # Mark the old position of the moved block as free space.
        disk[current_file_idx] = -1
        
        # The pointers will automatically be in correct positions for the next iteration
        # when the `while` loops at the start of the next iteration execute.

    # Step 3: Calculate the filesystem checksum.
    checksum = 0
    for pos, file_id in enumerate(disk):
        if file_id != -1: # Only include file blocks, skip free space (-1)
            checksum += (pos * file_id)
            
    return checksum

# --- Execution ---

# For testing with the example from the problem description (2333133121414131402)
# The expected checksum for this example is 1928.
# To run this specific example:
# # You would uncomment this section and temporarily write the example string to 'data.txt'
# # or modify the function to accept a string instead of a filepath for testing.
# example_disk_map_str = "2333133121414131402"
# # Temporarily write to a file for testing the function structure
# with open("example_disk_map.txt", "w") as f:
#     f.write(example_disk_map_str)
# example_checksum = solve_disk_fragmenter("example_disk_map.txt")
# print(f"Example Checksum: {example_checksum} (Expected: 1928)")


# To run with your actual puzzle input from 'data.txt':
actual_checksum = solve_disk_fragmenter()
if actual_checksum is not None:
    print(f"Resulting filesystem checksum: {actual_checksum}")
