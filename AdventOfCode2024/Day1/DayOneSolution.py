list_a = []
list_b = []

try:
    with open('data.txt', 'r') as file:
        for line in file:
            # Split each line by whitespace
            idNumber1, idNumber2 = line.strip().split()

            # Convert the string numbers to integers and append it to own lists
            list_a.append(int(idNumber1))
            list_b.append(int(idNumber2))
except FileNotFoundError:
    print("Error: data.txt not found. Please make sure the file is in the same directory")
except ValueError:
    print("Error: Invalid data format in data.txt. Ensure all values are integers.")

# Now We have our 2 lists with ID Numbers:
print("List A: ", list_a)
print("List B: ", list_b)

# Make A copy of the lists:
part1_List_a = list_a.copy()
part1_List_b = list_b.copy()

# Lets sort them from lowest to highest:
part1_List_a.sort()
part1_List_b.sort()

print("List A: ", part1_List_a)
print("List B: ", part1_List_b)

# Lets make another list, to store all the differences into:
differences = []

# Check that each list has same length:
if len(part1_List_a) != len(part1_List_b):
    print("Warning: Lists are not same length! Not going to get accurate results...")
    min_length = min(len(part1_List_a), len(part1_List_b))
else:
    min_length = len(part1_List_a)

# Calculate the difference between two ID Numbers:
for i in range(min_length):
    diff = abs(part1_List_a[i] - part1_List_b[i])
    differences.append(diff)

#print("\nList of Differences:", differences)

# Sum of all differences
total_difference = sum(differences)

print("========================")
print("PART ONE:")
print("Total Sum of Differences:", total_difference)

# Part 2 of this problem:
similarity_score = 0

# Iterate through each number in the first list:
for number_a in list_a:
    # Count how many times 'number_a' appears in list_b:
    count_in_b = list_b.count(number_a)

    # Calculate the score for this number:
    score_for_current_number = number_a * count_in_b

    # Add to the total similarity score
    similarity_score += score_for_current_number

    #print(f"Numner from List A: {number_a}, appears in List B: {count_in_b} times.")
    
print("========================")
print("PART TWO:")
print(f"Final Similarity Score:", similarity_score)
print("========================")
