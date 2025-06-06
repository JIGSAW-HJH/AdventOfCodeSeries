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


# Lets sort them from lowest to highest:
list_a.sort()
list_b.sort()

print("List A: ", list_a)
print("List B: ", list_b)

# Lets make another list, to store all the differences into:
differences = []

# Check that each list has same length:
if len(list_a) != len(list_b):
    print("Warning: Lists are not same length! Not going to get accurate results...")
    min_length = min(len(list_a), len(list_b))
else:
    min_length = len(list_a)

# Calculate the difference between two ID Numbers:
for i in range(min_length):
    diff = abs(list_a[i] - list_b[i])
    differences.append(diff)

print("\nList of Differences:", differences)

# Sum of all differences
total_difference = sum(differences)

print("Total Sum of Differences:", total_difference)

