# Global array
arr = []
LB = 0
size = 0

# Traverse algorithm


def traverse():
    global arr, LB, size
    if size == 0:
        print("Array is empty.")
    else:
        print("Array elements:")
        for i in range(LB, LB + size):
            print(arr[i], end=" ")
        print()

# Insertion algorithm


def insertion():
    global arr, LB, size
    if size >= len(arr):
        print("Array is full. Cannot insert more elements.")
        return

    element = int(input("Enter the element to insert: "))
    index = int(input("Enter the index to insert the element at: "))

    if index < 0 or index > size:
        print("Invalid index. Please provide a value between 0 and", size)
        return

    # Shift elements to the right to make space for insertion at index
    for i in range(LB + size - 1, LB + index - 1, -1):
        arr[i + 1] = arr[i]

    # Insert the element at index
    arr[LB + index] = element

    # Increment the size
    size += 1
    print("Element inserted successfully.")

# Menu function


def menu():
    global arr, LB, size
    while True:
        print("\nMENU")
        print("1. Traverse")
        print("2. Insertion")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            traverse()
        elif choice == 2:
            insertion()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Main function


def main():
    global arr, LB, size
    size = int(input("Enter the size of the array: "))
    LB = int(input("Enter the lower bound of the array: "))
    arr = [0] * size

    menu()


if __name__ == "__main__":
    main()
