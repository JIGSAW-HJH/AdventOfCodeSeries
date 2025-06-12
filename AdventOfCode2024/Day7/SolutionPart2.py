import itertools

def solve_equation(numbers, operators):
    """
    Evaluates an expression with numbers and operators from left to right,
    including addition (+), multiplication (*), and concatenation (||).
    
    numbers: list of integers
    operators: list of strings ('+', '*', '||')
    """
    if not numbers:
        return 0 # Should not occur with valid puzzle input
    
    # Start the result with the first number in the list
    result = numbers[0]
    
    # Iterate through the operators and apply them left-to-right
    for i in range(len(operators)):
        op = operators[i]
        next_num = numbers[i+1]
        
        if op == '+':
            result += next_num
        elif op == '*':
            result *= next_num
        elif op == '||':
            # Concatenation: convert both current result and next number to strings,
            # combine them, and then convert the new string back to an integer.
            result = int(str(result) + str(next_num))
        else:
            raise ValueError(f"Unknown operator: {op}")
            
    return result

def can_equation_be_true(line):
    """
    Parses a single equation line and checks if any combination of
    '+', '*', or '||' operators can make the equation true.
    
    Returns the test value if a valid combination is found, otherwise returns 0.
    """
    parts = line.split(':')
    test_value = int(parts[0].strip())
    numbers_str = parts[1].strip().split()
    numbers = [int(n) for n in numbers_str]

    # If there are no numbers, it cannot be true
    if len(numbers) == 0:
        return 0

    # If there's only one number, it must match the test value directly
    if len(numbers) == 1:
        return test_value if numbers[0] == test_value else 0

    # Determine the number of operator positions (always one less than the number of numbers)
    num_operator_positions = len(numbers) - 1
    
    # Define all possible operators including concatenation
    possible_operators = ['+', '*', '||']
    
    # Generate all possible combinations of operators for the given number of positions
    # For example, if num_operator_positions is 2, it will generate ('+', '+'), ('+', '*'), ('+', '||'), etc.
    for op_combination in itertools.product(possible_operators, repeat=num_operator_positions):
        # Evaluate the expression with the current operator combination
        if solve_equation(numbers, list(op_combination)) == test_value:
            return test_value # If it matches the test value, this equation is true

    return 0 # No combination worked for this equation

def calculate_total_calibration_result(input_data_filepath):
    """
    Reads equations from the specified file and calculates the sum of test values
    for all equations that can be made true with the available operators.
    """
    total_calibration_result = 0
    try:
        with open(input_data_filepath, 'r') as f:
            for line in f:
                if line.strip(): # Process non-empty lines
                    total_calibration_result += can_equation_be_true(line)
    except FileNotFoundError:
        print(f"Error: The file '{input_data_filepath}' was not found.")
        print("Please ensure 'data.txt' is in the same directory as your script, or provide the correct path.")
        return None # Return None to indicate an error state

    return total_calibration_result

# --- Main execution for Part Two ---

# First, let's verify with the example input from Part Two
example_input_part2_str = """
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

# To test the example, we'll write it to a temporary file
with open("example_part2_test_data.txt", "w") as f:
    f.write(example_input_part2_str.strip())

example_result_part2 = calculate_total_calibration_result("example_part2_test_data.txt")
print(f"Example Total Calibration Result (Part 2): {example_result_part2}") # Expected: 11387

# Now, calculate the result for your actual puzzle input from 'data.txt'
your_data_file_path = 'data.txt' 
print(f"\nCalculating actual puzzle result from '{your_data_file_path}'...")
actual_result_part2 = calculate_total_calibration_result(your_data_file_path)

if actual_result_part2 is not None:
    print(f"Actual Puzzle Total Calibration Result (Part 2): {actual_result_part2}")
