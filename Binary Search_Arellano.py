# Gino Arellano
# SBIT-3H

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Sorted list to search in
numbers = [1,2,3,4,5,6]

# Ask user for input
target = int(input("Enter the number you want to search for: "))

# Run the binary search
result = binary_search(numbers, target)

# Show result
if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} not found in the list.")
