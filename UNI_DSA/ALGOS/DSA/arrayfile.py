A: list[int] = [None]*7
N: int = 0
LB: int = 0
Size: int = 7
operations: int = 10

class Array:
#                               GLOBAL VARIABLES

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
                    count = 0
                    for i in range(LB, N + LB):
                        if A[i] == Item:
                            count += 1
                    print(f"Item {Item} found {count} times")


    def LinearSearch(Item):
                for i in range(LB, N + LB):
                    if A[i] == Item:
                        print(f"Item {Item} found at position {i}")
                        return
                print(f"Item {Item} not found")


    # def CountLinearSearch(Item):
    #             count = 0
    #             positions = []
    #             for i in range(LB, N + LB):
    #                 if A[i] == Item:
    #                     count += 1
    #                     positions.append(i)
    #             if count > 0:
    #                 print(f"Item {Item} found {count} times at positions {positions}")
    #             else:
    #                 print(f"Item {Item} not found")


    def MultiLinearSearch(Items):
                for Item in Items:
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
    def Searching():
        global N, LB
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
                    count = 0
                    for i in range(LB, N + LB):
                        if A[i] == Item:
                            count += 1
                    print(f"Item {Item} found {count} times")


        def LinearSearch(Item):
                for i in range(LB, N + LB):
                    if A[i] == Item:
                        print(f"Item {Item} found at position {i}")
                        return
                print(f"Item {Item} not found")    
                
                            
        def MultiLinearSearch(Items):
                for Item in Items:
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
    #                               SORTING FUNCTION


    def Sorting():
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
        def merge(A, LB, m, r, ascending=True):
            n1 = m - LB + 1
            n2 = r - m
            L = [0] * n1
            R = [0] * n2

            for i in range(n1):
                L[i] = A[LB + i]
            for j in range(n2):
                R[j] = A[m + 1 + j]

            i, j, k = 0, 0, LB
            while i < n1 and j < n2:
                if (ascending and L[i] <= R[j]) or (not ascending and L[i] >= R[j]):
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1

            while i < n1:
                A[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                A[k] = R[j]
                j += 1
                k += 1

        def mergeSort(A, LB, r, ascending=True):
            if LB < r:
                m = LB + (r - LB) // 2
                mergeSort(A, LB, m, ascending)
                mergeSort(A, m + 1, r, ascending)
                merge(A, LB, m, r, ascending)

                if not ascending:
                    # Reverse the sorted array for descending order
                    A[LB:r+1] = A[LB:r+1][::-1]

    
        print("......Select one Operation in given below........")
        print("For Bubble Sort press 1")
        print("For Insertion Sort press 2")
        print("For Shell Sort press 3")
        print("For Merge Sort press 4")
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
        elif OP == 4:
            ascending = Order == 1
            mergeSort(A, 0, N - 1, ascending)

        else:
            print("Invalid Option")

        print("\nSorted array in", "ascending" if Order == 1 else "descending", "order:")
        for i in range(N):
            print("%d" % A[i], end=" ")


# #                               MERGING FUNCTION  
    def Merging():
        while True:
                print("1. Merge Two Arrays")
                print("2. Exit")

                choice = int(input("Enter your choice (1 or 2): "))

                if choice == 1:
                    print("Enter elements for the first array:")
                    A = [
                        int(x)
                        for x in input(
                            "Enter elements of the first array separated by space: "
                        ).split()
                    ]
                    print("Enter elements for the second array:")
                    B = [
                        int(x)
                        for x in input(
                            "Enter elements of the second array separated by space: "
                        ).split()
                    ]
                    order = input("Enter order (ascending/descending): ")

                    if order.lower() == "ascending":
                        merged_array = merging(A, B)
                    elif order.lower() == "descending":
                        merged_array = merge_descending(A, B)
                    else:
                        print("Invalid order. Merging in ascending order by default.")
                        merged_array = merging(A, B)

                    print("Merged array:", merged_array)
                elif choice == 2:
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please select 1 or 2.")
def merging(A, B):
            C = []
            i = j = 0

            while i < len(A) and j < len(B):
                if A[i] < B[j]:
                    C.append(A[i])
                    i += 1
                else:
                    C.append(B[j])
                    j += 1

            while i < len(A):
                C.append(A[i])
                i += 1

            while j < len(B):
                C.append(B[j])
                j += 1

            return C

def merge_descending(A, B):
            C = []
            i = len(A) - 1
            j = len(B) - 1

            while i >= 0 and j >= 0:
                if A[i] > B[j]:
                    C.append(A[i])
                    i -= 1
                else:
                    C.append(B[j])
                    j -= 1

            while i >= 0:
                C.append(A[i])
                i -= 1

            while j >= 0:
                C.append(B[j])
                j -= 1

            return C


  