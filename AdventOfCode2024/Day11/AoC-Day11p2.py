from functools import lru_cache

@lru_cache(maxsize=None)
def count_stones(value, blinks_remaining):
    if blinks_remaining == 0:
        return 1  # a single stone at end
    if value == 0:
        return count_stones(1, blinks_remaining - 1)
    
    digits = str(value)
    if len(digits) % 2 == 0:
        mid = len(digits) // 2
        left = int(digits[:mid])
        right = int(digits[mid:])
        return (
            count_stones(left, blinks_remaining - 1) +
            count_stones(right, blinks_remaining - 1)
        )
    else:
        return count_stones(value * 2024, blinks_remaining - 1)

def total_stones_after_blinks(initial_stones, total_blinks):
    return sum(count_stones(stone, total_blinks) for stone in initial_stones)

# Load your puzzle input
with open("data.txt") as f:
    line = f.read().strip()
    initial_stones = list(map(int, line.split()))

print("Total stones after 6 blinks:", total_stones_after_blinks([125,17], 6)) # Previous example sanity check..
print("Total stones after 75 blinks:", total_stones_after_blinks(initial_stones, 75))
