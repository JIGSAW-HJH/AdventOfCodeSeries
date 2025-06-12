import itertools

def solve_equation(numbers, operators):
    """
    Evaluates an expression with numbers and operators from left to right.
    numbers: list of integers
    operators: list of characters ('+' or '*')
    """
    if not numbers:
        return 0 # Or handle as error
    
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i+1]
        elif operators[i] == '*':
            result *= numbers[i+1]
        else:
            raise ValueError(f"Unknown operator: {operators[i]}")
    return result

def can_equation_be_true(line):
    """
    Parses a line and checks if any operator combination makes the equation true.
    Returns the test value if true, 0 otherwise.
    """
    parts = line.split(':')
    test_value = int(parts[0].strip())
    numbers_str = parts[1].strip().split()
    numbers = [int(n) for n in numbers_str]

    if len(numbers) == 0:
        return 0 # No numbers to evaluate

    if len(numbers) == 1:
        # If there's only one number, it must equal the test value
        return test_value if numbers[0] == test_value else 0

    num_operators = len(numbers) - 1
    
    # Generate all combinations of operators ('+', '*')
    # For example, if num_operators is 2, this will generate [('+', '+'), ('+', '*'), ('*', '+'), ('*', '*')]
    for op_combination in itertools.product(['+', '*'], repeat=num_operators):
        if solve_equation(numbers, list(op_combination)) == test_value:
            return test_value # Found a combination that works

    return 0 # No combination worked

def calculate_total_calibration_result(input_data):
    """
    Calculates the sum of test values for equations that can be made true.
    """
    total_calibration_result = 0
    for line in input_data.strip().split('\n'):
        if line.strip(): # Ensure line is not empty
            total_calibration_result += can_equation_be_true(line)
    return total_calibration_result

# Example usage with the provided input:
example_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

example_result = calculate_total_calibration_result(example_input)
print(f"Example Total Calibration Result: {example_result}")

# Now, we need to load your actual puzzle input.
# Assuming the actual puzzle input is in a file named 'puzzle_input.txt'
# Replace 'puzzle_input.txt' with the actual path to your input file.
try:
    with open('data.txt', 'r') as f:
        puzzle_input = f.read()
    
    actual_result = calculate_total_calibration_result(puzzle_input)
    print(f"Actual Puzzle Total Calibration Result: {actual_result}")

except FileNotFoundError:
    print("Error: 'puzzle_input.txt' not found. Please provide your actual puzzle input file.")
    print("If you provide the puzzle input directly, I can calculate the actual result.")
