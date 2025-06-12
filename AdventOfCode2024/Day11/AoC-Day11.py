def blink(stones):
    result = []
    for stone in stones:
        if stone == 0:
            result.append(1)
        else:
            s = str(stone)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                left = int(s[:mid])
                right = int(s[mid:])
                result.extend([left, right])
            else:
                result.append(stone * 2024)
    return result

def simulate(stones, blinks):
    for _ in range(blinks):
        stones = blink(stones)
    return len(stones)

# Example input
# stones = [125, 17]  # From the example

# Real input: Replace this with your puzzle input as a list of integers
with open("data.txt") as f:
    line = f.read().strip()
    stones = list(map(int, line.split()))

print("Number of stones after 25 blinks:", simulate(stones, 25))
