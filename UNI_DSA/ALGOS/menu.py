#                              IMPORTS
# from Functions.traverse import Traverse
# adding comment . New code should be added and add more algos 
# like more sorting algos and searching algos.merge sort ascending and descdening order
# quick sort ascending and descending order

#                               GLOBAL VARIABLES
A: list[int] = [None]*7
N: int = 0
LB: int = 0
Size: int = 7
operations: int = 10

#                               TRAVERSAL CODE


def Traverse():
    global N, LB
    for i in range(LB, N+LB):
        print(A[i], end=',')
    print("...........................")
#                               INSERTION FUNCTIONS


def Insertion():
    global N, LB, Size
    print('Enter the element you want to insert:')
    Item = int(input())
    print('Enter the index where you want insertion')
    K = int(input())

    if N == Size:
        print("Overflow")
    else:
        if K < LB or K > N + LB:
            print("K is Invalid")
        else:
            #             Extend the list if necessary
            # if N + LB == len(A):
            #     A.append(0)
            # for i in range(N, K, -1):
            #     A[i] = A[i - 1]
            # A[K] = Item
            # N += 1
            #             Shift elements to the right to make room for the new element or initialize array with NONE first
            i = N
            while i > K:
                A[i] = A[i - 1]
                i -= 1

            # Insert the new element
            A[K] = Item
            N += 1
            print("Now the array elements are ")
            for i in range(N):
                print(A[i], end=',')
            print("...........................")
#                               DELETION FUNCTION


def Deletion():
    global N, LB
    print('Enter the index where you want deletion')  # position to delete
    K = int(input())

    if N == 0:
        print("Underflow")
    else:
        if K < LB or K > N + LB - 1:
            print("K is Invalid")
        else:
            for i in range(K, N + LB - 1):
                A[i] = A[i + 1]
            N -= 1
            print("Now the array elements are ")
            for i in range(N):
                print(A[i], end=',')
            print("...........................")
#                               SEARCHING FUNCTIONS


def Searching():
    global N, LB
    print("Select one Operation in given below")
    print("For Single Binary Search press 1")
    print("For Multi Binary Search press 2")
    print("For Single Linear Search press 3")
    print("For Multi Linear Search press 4")
    print("...........................")
    OP = int(input())

    if OP == 1:
        print(OP, ":Binary Single Search.....")
        Item = int(input("Enter the item you want to search: "))
        BinarySearch(Item)
    elif OP == 2:
        print(OP, ":Binary Multi Search.....")
        Items = list(map(int, input(
            "Enter the item you want to count: ").split()))
        MultiBinarySearch(Items)
    elif OP == 3:
        print(OP, ":Linear Single Search.....")
        Item = int(input("Enter the item you want to search: "))
        LinearSearch(Item)
    elif OP == 4:
        print(OP, ":Linear Multi Search.....")
        Items = list(map(int, input(
            "Enter the items you want to count: ").split()))
        MultiLinearSearch(Items)
    else:
        print("Invalid Option")


def BinarySearch(Item):
    low = LB
    high = N + LB - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] < Item:
            low = mid + 1
        elif A[mid] > Item:
            high = mid - 1
        else:
            print(f"Item {Item} found at position {mid}")
            return
    print(f"Item {Item} not found")


def CountBinarySearch(Item):
    count = 0
    for i in range(LB, N + LB):
        if A[i] == Item:
            count += 1
    print(f"Item {Item} found {count} times")


def MultiBinarySearch(Items):
    for Item in Items:
        CountBinarySearch(Item)


def LinearSearch(Item):
    for i in range(LB, N + LB):
        if A[i] == Item:
            print(f"Item {Item} found at position {i}")
            return
    print(f"Item {Item} not found")


def CountLinearSearch(Item):
    count = 0
    positions = []
    for i in range(LB, N + LB):
        if A[i] == Item:
            count += 1
            positions.append(i)
    if count > 0:
        print(f"Item {Item} found {count} times at positions {positions}")
    else:
        print(f"Item {Item} not found")


def MultiLinearSearch(Items):
    for Item in Items:
        CountLinearSearch(Item)


#                               SORTING FUNCTION


def Sorting():
    print("Select one Operation in given below")
    print("For Bubble Sort press 1")
    print("For Insertion Sort press 2")
    print("For Shell Sort press 3")
    OP = int(input())
    print("For Ascending Order press 1")
    print("For Descending Order press 2")
    Order = int(input())

    if OP == 1:
        BubbleSort(Order)
    elif OP == 2:
        InsertionSort(Order)
    elif OP == 3:
        ShellSort(Order)
    else:
        print("Invalid Option")


def BubbleSort(Order):
    global A, N
    for i in range(N):
        for j in range(0, N-i-1):
            if (Order == 1 and A[j] > A[j+1]) or (Order == 2 and A[j] < A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
    print("Sorted array is:", A)


def InsertionSort(Order):
    global A, N
    for i in range(1, N):
        key = A[i]
        j = i-1
        while j >= 0 and ((Order == 1 and key < A[j]) or (Order == 2 and key > A[j])):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    print("Sorted array is:", A)


def ShellSort(Order):
    global A, N
    gap = N // 2
    while gap > 0:
        for i in range(gap, N):
            temp = A[i]
            j = i
            while j >= gap and ((Order == 1 and A[j-gap] > temp) or (Order == 2 and A[j-gap] < temp)):
                A[j] = A[j-gap]
                j -= gap
            A[j] = temp
        gap //= 2
    print("Sorted array is:", A)


#                               MAIN FUNCTION
for i in range(operations):
    print("Select one Operation in given below")
    print("For Traversing press 1")
    print("For Insertion press 2")
    print("For Searching press 3")
    print("For Sorting press 4")
    print("For Deletion press 5")
    print("For Exit press 6")
    print("...........................")
    OP = int(input())
    if OP == 1:
        print(OP, ":Traverse Selected")
        Traverse()
    elif OP == 2:
        print(OP, ":Insetion Selected")
        Insertion()
    elif OP == 3:
        print(OP, ":Searching Selected")
        Searching()
    elif OP == 4:
        print(OP, ":Sorting Selected")
        Sorting()
    elif OP == 5:
        print(OP, ":Deletion Selected")
        Deletion()
    elif OP == 6:
        print("Exiting...")
        break
    else:
        print("Invalid Option")


                    # MORE ALGOS WILL BE HERE