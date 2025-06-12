def parse_disk_map(disk_map):
    blocks = []
    file_id = 0
    i = 0
    while i < len(disk_map):
        length = int(disk_map[i])
        if i % 2 == 0:
            # File block
            blocks.extend([str(file_id)] * length)
            file_id += 1
        else:
            # Free space
            blocks.extend(['.'] * length)
        i += 1
    return blocks

def move_whole_files(blocks):
    file_positions = {}
    i = 0
    while i < len(blocks):
        if blocks[i] != '.':
            fid = blocks[i]
            start = i
            while i < len(blocks) and blocks[i] == fid:
                i += 1
            end = i
            file_positions[int(fid)] = (start, end)
        else:
            i += 1

    for fid in sorted(file_positions.keys(), reverse=True):
        start, end = file_positions[fid]
        length = end - start

        # Search for space before the file that fits the file
        for i in range(0, start - length + 1):
            if all(blocks[j] == '.' for j in range(i, i + length)):
                # Move file
                for j in range(start, end):
                    blocks[j] = '.'
                for j in range(i, i + length):
                    blocks[j] = str(fid)
                break

    return blocks

def calculate_checksum(blocks):
    return sum(i * int(ch) for i, ch in enumerate(blocks) if ch != '.')

# Read disk map from file
with open('data.txt', 'r') as f:
    disk_map = f.read().strip()

blocks = parse_disk_map(disk_map)
blocks = move_whole_files(blocks)
checksum = calculate_checksum(blocks)
print(f"Filesystem checksum: {checksum}")
