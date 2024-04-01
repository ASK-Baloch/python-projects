A = []
N = 0
LB = 0
Size = 7
operations = 5


def Traverse():
    global N, LB
    for i in range(LB, N+LB):
        print(A[i], end=',')
    print("...........................")


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
            A.insert(K, Item)
            N += 1
            print("Now the array elements are ")
            for i in range(N):
                print(A[i], end=',')
            print("...........................")


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
        print(OP,":Binary Single Search.....")
        Item = int(input("Enter the item you want to search: "))
        BinarySearch(Item)
    elif OP == 2:
        print(OP,":Binary Multi Search.....")
        Items = list(map(int, input("Enter the items you want to search, separated by space: ").split()))
        MultiBinarySearch(Items)
    elif OP == 3:
        print(OP,":Linear Single Search.....")
        Item = int(input("Enter the item you want to search: "))
        LinearSearch(Item)
    elif OP == 4:
        print(OP,":Linear Multi Search.....")
        Items = list(map(int, input("Enter the items you want to search, separated by space: ").split()))
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

def MultiBinarySearch(Items):
    for Item in Items:
        BinarySearch(Item)

def LinearSearch(Item):
    for i in range(LB, N + LB):
        if A[i] == Item:
            print(f"Item {Item} found at position {i}")
            return
    print(f"Item {Item} not found")

def MultiLinearSearch(Items):
    for Item in Items:
        LinearSearch(Item)


for i in range(operations):
    print("Select one Operation in given below")
    print("For Traversing press 1")
    print("For Insertion press 2")
    print("For Searching press 3")
    print("For Deletion press 4")
    print("For Exit press 5")
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
        print(OP, ":Deletion Selected")
        Deletion()
    elif OP == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Option")
