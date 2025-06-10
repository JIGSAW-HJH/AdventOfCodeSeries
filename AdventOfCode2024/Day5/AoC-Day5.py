rules_list = []
pages_list = []

def read_and_filter_data(filename='data.txt'):
    # Using global lists directly as requested by your script,
    # but returning them is generally better practice for modularity.
    # We need to clear them if the function might be called multiple times
    # in the same program execution, to avoid appending duplicate data.
    rules_list.clear()
    pages_list.clear()
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip() # Remove leading/trailing whitespace including newlines
            if not line:
                continue # Skip empty lines
            
            if '|' in line:
                # This is a pipe-separated line (page ordering rules)
                parts = line.split('|')
                try:
                    # Convert parts to integers and store as a tuple
                    rules_list.append((int(parts[0]), int(parts[1])))
                except ValueError:
                    print(f"Warning: Could not parse pipe data line: {line}")
            elif ',' in line:
                # This is a comma-separated line (pages to produce in an update)
                parts = line.split(',')
                try:
                    # Convert all parts to integers
                    pages_list.append([int(p) for p in parts])
                except ValueError:
                    print(f"Warning: Could not parse pages data line: {line}")
            else:
                print(f"Warning: Skipping unrecognised line format: {line}")
                
    return rules_list, pages_list

def is_update_correctly_ordered(update, all_rules):
    """
    Checks if a given update list adheres to the provided rules.
    A rule (X, Y) means X must appear before Y if both are in the update.
    """
    
    # Create a set of pages in the current update for efficient lookup
    update_set = set(update)

    for rule_x, rule_y in all_rules:
        # Check if both pages involved in the rule are present in the current update
        if rule_x in update_set and rule_y in update_set:
            # If both are present, check their order
            # Find the index of rule_x and rule_y in the update list
            index_x = update.index(rule_x)
            index_y = update.index(rule_y)

            # If rule_x appears AFTER rule_y, the rule is violated
            if index_x > index_y:
                return False # This update is not correctly ordered

    return True # If no rules were violated, the update is correctly ordered

def get_middle_page_number(update):
    """
    Returns the middle page number of an update list.
    Assumes the list has an odd number of elements (as per example).
    """
    if not update:
        return None # Handle empty list case if necessary
    
    # The middle index for an odd-length list is len // 2
    # For a list of length 5, indices are 0, 1, 2, 3, 4. Middle is 2 (5 // 2)
    # For a list of length 3, indices are 0, 1, 2. Middle is 1 (3 // 2)
    middle_index = len(update) // 2
    return update[middle_index]

# --- Main Logic ---

# Read the data from the file
# The global lists rules_list and pages_list will be populated by this call.
read_and_filter_data('data.txt') 

# Initialize sum for middle page numbers of correctly ordered updates
total_middle_pages_sum = 0
correctly_ordered_updates_count = 0

print("Processing updates...")

for i, current_update in enumerate(pages_list):
    # Check if the current update is correctly ordered according to all rules
    if is_update_correctly_ordered(current_update, rules_list):
        correctly_ordered_updates_count += 1
        middle_page = get_middle_page_number(current_update)
        total_middle_pages_sum += middle_page
        print(f"Update {i+1} (pages: {current_update}) is CORRECTLY ordered. Middle page: {middle_page}")
    else:
        print(f"Update {i+1} (pages: {current_update}) is NOT correctly ordered.")

print(f"\nTotal correctly ordered updates found: {correctly_ordered_updates_count}")
print(f"Sum of middle page numbers from correctly ordered updates: {total_middle_pages_sum}")
