def insert_element(arr, size, x, pos):
    arr.append(None)  # Increase the size of the array
    i = size
    while i > pos:
        arr[i] = arr[i - 1]  # Move elements forward
        i -= 1
    arr[pos] = x  # Insert the new element

# Example usage:
my_array = [12, 16, 20, 40, 50, 70]
new_element = 26
position = 3
insert_element(my_array, len(my_array), new_element, position)

print("Array after insertion:", my_array)

def traverse_array(arr):
    for i in range(len(arr)):
        print(f"arr[{i}] = {arr[i]}")

# Example usage:
my_array = [53, 99, -11, 5, 102]
print("Array elements:")
traverse_array(my_array)
