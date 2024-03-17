def insert(arr, S, N, element, K):
    """Inserts an element into the array at a specified index.

    Args:
        arr: The array to insert into.
        S: The size (maximum capacity) of the array.
        N: The current number of elements in the array.
        element: The element to insert.
        K: The desired index for insertion (0-based).

    Returns:
        A tuple containing:
            - The modified array (if insertion is successful).
            - A boolean indicating success (True) or failure (False).
            - An error message (optional) if insertion fails.

    Raises:
        IndexError: If K is out of bounds (less than 0 or greater than N).
    """

    # Check if array is full
    if N >= S:
        return arr, False, "Array is full! Cannot insert."

    # Check for valid insertion index (0-based and within current elements)
    if K < 0 or K > N:
        raise IndexError(
            "Invalid insertion index. Please provide a value between 0 and {}".format(N))

    # Shift elements to the right to make space for insertion at K
    for i in range(N, K, -1):
        arr[i] = arr[i-1]

    # Insert the element at index K
    arr[K] = element

    # Increment the number of elements
    N += 1

    return arr, True, None  # Return modified array, success flag, and optional error message


# Example usage
arr = [None] * 6  # Initialize array with size 6
N = 0  # Initially no elements

# Insert element 10 at index 0 (beginning)
new_arr, success, error_msg = insert(arr, 6, N, 10, 0)
N += 1  # Increment the number of elements
new_arr, success, error_msg = insert(new_arr, 6, N, 20,1)

if success:
    print("Insertion successful! New array:", new_arr)
else:
    print("Insertion failed:", error_msg)
