def menu():
    """Displays the menu and prompts the user for a choice."""
    while True:
        print("\nMenu:")
        print("1. Traverse") 
        print("2. Insertion")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Invalid choice. Please try again.")


# def traverse(arr):
#     """Prints all elements of the array."""
#     print("Array elements:")
#     for element in arr:
#         print(element)
def traverse(arr, S):
    if S == 0:
        print("Array is empty.")
    else:
        print("Array elements:")
        for i in range(LB, LB + S):
            print(arr[i], end=" ")
        print()


def insert(arr, S, N, LB):
    """Inserts an element into the array at a specified index."""
    while True:
        try:
            element = int(input("Enter the element to insert: "))
            K = int(input("Enter the index (starting from {}): ".format(LB)))
            arr, success, error_msg = insert_at_index(arr, S, N, element, K)
            if success:
                print("Insertion successful!")
            else:
                print(error_msg)
            break  # Exit the loop if successful or error occurs
        except ValueError:
            print("Invalid input. Please enter integers only.")


def insert_at_index(arr, S, N, element, K):
    """Helper function to handle insertion logic and index validation."""
    if N >= S:
        return arr, False, "Array is full!"
    if K < LB or K > N:
        raise IndexError(
            "Invalid index! Please enter a value between {} and {}".format(LB, N))
    # Shift elements to make space
    for i in range(N-1, K-1, -1):
        arr[i+1] = arr[i]
    # Insert the element at index K
    arr[K] = element
    N += 1  # Increment the number of elements
    return arr, True, None


# Global array and variables
arr = []
S = 0  # Size of the array
N = 0  # Number of elements currently in the array
LB = 0  # Lower bound (index of the first element)

# Get array size and lower bound from user
while True:
    try:
        S = int(input("Enter the size of the array: "))
        LB = int(input("Enter the lower bound of the array: "))
        arr = [None] * S  # Initialize array with None values
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")

# Main loop
while True:
    choice = menu()
    if choice == 1:
        traverse(arr,S)
    elif choice == 2:
        insert(arr, S, N, LB)
    else:
        break  # Exit the program
