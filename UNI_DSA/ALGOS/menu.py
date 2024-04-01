A = []
N = 0
LB = 0
Size = 7
operations = 4


def Traverse():
    global N, LB
    for i in range(LB, N+LB):
        print(A[i])
    print()


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
                print(A[i])
            print()


def Deletion():
    pass


for i in range(operations):
    print("Select one Operation in given below")
    print("For Traversing press 1")
    print("For Insertion press 2")
    print("For Deletion press 3")
    print("For Exit press 4")
    OP = int(input())
    if OP == 1:
        print(OP,":Traverse Selected")
        Traverse()
    elif OP == 2:
        print(OP,":Insetion Selected")
        Insertion()
    elif OP == 3:
        print(OP,":Deletion Selected") 
        Deletion()
    elif OP == 4:
        print(OP,":Traverse Selected") 
        break
    else:
        print("Invalid Option")
