def merge(A, low, mid, high):
    B = [0] * 10
    C = [0] * 10

    nl = mid - low + 1
    nr = high - mid

    k = 0

    for i in range(low, mid + 1):
        B[k] = A[i]
        k += 1

    k = 0

    for i in range(mid + 1, high + 1):
        C[k] = A[i]
        k += 1

    A[0] = low
    B[0] = low
    C[0] = low

    while A[0] <= (A[N] + low - 1) and B[N] <= (N + low - 1):
        if A[0] < B[0]:
            C[0] = A[0]
        else:
            C[0] = B[0]
            B[0] = B[0] + 1

        C[0] = C[0] + 1

    if A[0] > (A[N] + low - 1):
        while B[0] <= (N + low - 1):
            C[0] = B[0]
            B[0] = B[0] + 1
            C[0] = C[0] + 1
    else:
        while A[0] > (A[N] + low - 1):
            C[0] = A[0]
            A[0] = A[0] + 1
            C[0] = C[0] + 1

    return

def merging_2_arrays_ascending():
    B = [0] * 10
    C = [0] * 10

    A[0] = lb
    B[0] = lb
    C[0] = lb

    while A[0] <= (A[N] + lb - 1) and B[N] <= (N + lb - 1):
        if A[0] < B[0]:
            C[0] = A[0]
        else:
            C[0] = B[0]
            B[0] = B[0] + 1

        C[0] = C[0] + 1

    if A[0] > (A[N] + lb - 1):
        while B[0] <= (N + lb - 1):
            C[0] = B[0]
            B[0] = B[0] + 1
            C[0] = C[0] + 1
    else:
        while A[0] > (A[N] + lb - 1):
            C[0] = A[0]
            A[0] = A[0] + 1
            C[0] = C[0] + 1

    return

def merging_2_arrays_descending():
    B = [0] * 10
    C = [0] * 10

    A[0] = lb
    B[0] = lb
    C[0] = lb

    while A[0] <= (A[N] + lb - 1) and B[N] >= (N + lb - 1):
        if A[0] < B[0]:
            C[0] = A[0]
        else:
            C[0] = B[0]
            B[0] = B[0] + 1

        C[0] = C[0] + 1

    if A[0] > (A[N] + lb - 1):
        while B[0] <= (N + lb - 1):
            C[0] = B[0]
            B[0] = B[0] + 1
            C[0] = C[0] + 1
    else:
        while A[0] > (A[N] + lb - 1):
            C[0] = A[0]
            A[0] = A[0] + 1
            C[0] = C[0] + 1

    return

def merge_sort_sub(A, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort_sub(A, low, mid)
        merge_sort_sub(A, low, mid)
        merge(A, low, mid, high)

    return

def merge_sort(A, lb, N):
    low = lb
    high = N + lb - 1
    merge_sort_sub(A, low, high)

    return

def mergesort_menu():
    """
    Presents a menu to the user for choosing sorting operations.
    """

    while True:
        print("\nMenu:")
        print("1. Merge Sort")
        print("2. Merge Two Arrays")
        print("3. Exit")  # Other options commented out for now

        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            # Merge sort
            A = [int(x) for x in input("Enter elements of array separated by space: ").split()]
            low = 0
            high = len(A) - 1
            order = input("Enter order (ascending/descending): ")

            if order.lower() == 'ascending':
                sorted_array = merge_sort(A)
            elif order.lower() == 'descending':
                sorted_array = merge_sort_descending(A)
            else:
                print("Invalid order. Sorting in ascending order by default.")
                sorted_array = merge_sort(A)

            print("Sorted array:", sorted_array)

        elif choice == 2:
            # Merge two arrays
            print("Enter elements for the first array:")
            A = [int(x) for x in input("Enter elements of first array separated by space: ").split()]
            print("Enter elements for the second array:")
            B = [int(x) for x in input("Enter elements of second array separated by space: ").split()]
            order = input("Enter order (ascending/descending): ")

            if order.lower() == 'ascending':
                merged_array = merge(A, B)
            elif order.lower() == 'descending':
                merged_array = merge_descending(A, B)
            else:
                print("Invalid order. Merging in ascending order by default.")
                merged_array = merge(A, B)

            print("Merged array:", merged_array)

        elif choice == 3:
            print("Exiting...")
            break
