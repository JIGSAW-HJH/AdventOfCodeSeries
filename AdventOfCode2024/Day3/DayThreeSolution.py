import re

def extract_valid_muls(data):
    # This regex captures ONLY valid mul(X,Y) patterns with 1-3 digit integers
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)

    total = 0
    for x_str, y_str in matches:
        x = int(x_str)
        y = int(y_str)
        total += x * y
    return total

# Example corrupted memory
print("Test run:")
data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
result = extract_valid_muls(data)
print("Total:", result)

with open("data.txt") as f:
    data = f.read()

print("Part 1 Answer:", extract_valid_muls(data))


def sum_enabled_mul_results(memory: str) -> int:
    # Pattern for valid mul(X,Y)
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    # Pattern for do() and don't()
    control_pattern = r"\bdo\(\)|don't\(\)"
    
    # Combine into one regex to match either mul(...) or control instruction
    pattern = f"({mul_pattern})|({control_pattern})"
    
    total = 0
    mul_enabled = True  # Initially enabled
    
    # Use re.finditer to preserve order of occurrences
    for match in re.finditer(pattern, memory):
        if match.group(0) == "do()":
            mul_enabled = True
        elif match.group(0) == "don't()":
            mul_enabled = False
        elif match.group(1):  # It's a valid mul(...)
            if mul_enabled:
                x = int(match.group(2))
                y = int(match.group(3))
                total += x * y

    return total

print(f"Part 2 Answer: {sum_enabled_mul_results(data)}")

