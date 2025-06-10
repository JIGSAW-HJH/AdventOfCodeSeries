import collections # Used for deque in topological sort

rules_list = []
pages_list = []

def read_and_filter_data(filename='data.txt'):
    # Clear global lists to ensure fresh data if function is called multiple times
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
                
    # No return value needed if populating global lists directly, but often good practice.
    # For now, it matches your previous structure.
    return rules_list, pages_list

def is_update_correctly_ordered(update, all_rules):
    """
    Checks if a given update list adheres to the provided rules.
    A rule (X, Y) means X must appear before Y if both are in the update.
    """
    update_set = set(update) # For efficient O(1) average time complexity lookups

    for rule_x, rule_y in all_rules:
        # Check if both pages involved in the rule are present in the current update
        if rule_x in update_set and rule_y in update_set:
            # If both are present, find their order
            index_x = update.index(rule_x)
            index_y = update.index(rule_y)

            # If rule_x appears AFTER rule_y, the rule is violated
            if index_x > index_y:
                return False # This update is not correctly ordered

    return True # If no rules were violated, the update is correctly ordered

def get_middle_page_number(update):
    """
    Returns the middle page number of an update list.
    Assumes the list has an odd number of elements (as per problem description example).
    """
    if not update:
        return None # Handle empty list if it's a possibility
    
    middle_index = len(update) // 2
    return update[middle_index]


def topological_sort_update(update_pages, all_rules):
    """
    Topologically sorts a list of pages based on relevant rules.
    This generates one valid order that satisfies all dependencies.
    
    Args:
        update_pages: A list of integers representing the pages in the current update.
        all_rules: A list of tuples (X, Y) where X must precede Y.
    Returns:
        A list of pages in a correct topological order, or None if a cycle is detected
        (though the problem implies no cycles will exist for valid inputs).
    """
    
    # 1. Build the graph and calculate in-degrees for pages in the current update
    graph = collections.defaultdict(list) # Adjacency list: page -> [pages it precedes]
    in_degree = collections.defaultdict(int) # page -> count of prerequisites
    
    # Initialize in-degrees for all pages that are part of this update to 0
    # and ensure they are present as keys in the in_degree map.
    for page in update_pages:
        in_degree[page] = 0 

    # Filter rules to only include those relevant to the current update
    # and build the graph and in-degrees.
    update_set = set(update_pages) # For efficient lookup
    for rule_x, rule_y in all_rules:
        if rule_x in update_set and rule_y in update_set:
            # Add edge from rule_x to rule_y
            graph[rule_x].append(rule_y)
            # Increment in-degree of rule_y
            in_degree[rule_y] += 1

    # 2. Initialize a queue with all nodes that have an in-degree of 0
    #    These are the starting points (pages with no prerequisites within this update).
    queue = collections.deque()
    for page in update_pages: 
        if in_degree[page] == 0:
            queue.append(page)

    # 3. Perform the topological sort
    sorted_order = []
    while queue:
        # Dequeue a node
        current_page = queue.popleft()
        sorted_order.append(current_page)

        # For each neighbor (page that current_page precedes)
        for neighbor in graph[current_page]:
            in_degree[neighbor] -= 1 # Decrement its in-degree
            # If its in-degree becomes 0, it has no more prerequisites, so enqueue it
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    # 4. Check for cycles
    # If the number of sorted elements is less than the total unique elements in the update,
    # it means there was a cycle. The problem context usually guarantees no cycles for valid inputs.
    if len(sorted_order) != len(update_pages):
        print(f"Warning: Cycle detected in update {update_pages}. Cannot sort.")
        return None 
        
    return sorted_order

# --- Main Logic ---

# Read the data from the file. This populates the global rules_list and pages_list.
read_and_filter_data('data.txt') 

# Variables to store results for both parts of the problem
total_middle_pages_sum_correct_original = 0 
total_middle_pages_sum_fixed_incorrect = 0

incorrectly_ordered_updates_to_fix = []

print("--- Initial Check and Categorization of Updates ---")

for i, current_update in enumerate(pages_list):
    if is_update_correctly_ordered(current_update, rules_list):
        middle_page = get_middle_page_number(current_update)
        total_middle_pages_sum_correct_original += middle_page
        # print(f"Update {i+1} (pages: {current_update}) is CORRECTLY ordered. Middle page: {middle_page}")
    else:
        # print(f"Update {i+1} (pages: {current_update}) is NOT correctly ordered.")
        incorrectly_ordered_updates_to_fix.append(current_update)

print(f"\nSum of middle page numbers from originally CORRECTLY ordered updates: {total_middle_pages_sum_correct_original}")
print(f"Number of updates that need fixing: {len(incorrectly_ordered_updates_to_fix)}")


print("\n--- Fixing and Processing Incorrectly Ordered Updates ---")

for i, incorrect_update in enumerate(incorrectly_ordered_updates_to_fix):
    # print(f"\nAttempting to fix update {i+1} (Original: {incorrect_update})")
    
    fixed_order = topological_sort_update(incorrect_update, rules_list)
    
    if fixed_order:
        new_middle_page = get_middle_page_number(fixed_order)
        total_middle_pages_sum_fixed_incorrect += new_middle_page
        # print(f"  Fixed order: {fixed_order}. New middle page: {new_middle_page}")
    else:
        print(f"  Could not fix update {incorrect_update} (possibly due to cycle).")

print(f"\nSum of middle page numbers from FIXED incorrectly ordered updates: {total_middle_pages_sum_fixed_incorrect}")
