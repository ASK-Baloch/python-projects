LB=0
N=0
S=8
F=LB-1
R=LB-1
A=[None] *S
stk=[None] *size
size=4
Q=[None]* size
CQ=[None]*size
top=LB-1
def menu():
    global LB,N,A
    print("type arr for array dst:\n type stk for stack:\n type que for QUEUE:\n type cq for circular queue :\n")
    dst= input("enter your choice ")
    if dst.lower() =='arr':
        print("Select 1 for traverse:\n2 for insertion:\n3 for deletion:\n4 for lin_sin_search:\n5 for lin_mul_search\n6 for bin_sin_search:\n7 for bin_mul_search:\n8 for bubble_sort:\n9 for selection Sort\n10 for insertion sort:\n11 for shell sort")
        choice= input("ENter your choice:") 
        choice=int(choice)
        if choice==1:
            traverse()
    
        elif choice==2:
            item=int(input("Enter the item to be inserted:"))
            k=int(input("enter the index:"))
            insertion(k,item)

        elif choice==3:
            I=int(input("Enter the index at which value to be delete!"))
            deletion(I)
            print("Array elements after deletion are ",traverse())
    
        elif choice==4:
            lin_sin_search( )

        elif choice==5:
            item=int(input("Enter the item to be searched"))
            lin_mul_search(item)    

        elif choice==6:
            print("Array must be sorted before calling binary search function")
            bubble_sort()
            item=int(input("Enter the item to be searched"))
            bin_sin_search(item)

        elif choice==7:
            print("Array must be sorted before calling binary search function")
            bubble_sort()
            item=int(input("Enter the item to be searched"))
            bin_mul_search(item)  

        elif choice==8:
            bubble_sort()    

        elif choice==9:
            selection_sort()

        elif choice==10:
            insertion_sort()    

        elif choice==11:
            shell_sort()  

    elif dst.lower()=='stk':       
        Ch=input("Slect push or pop: ",end=" ")
        if Ch.lower()=='push':
            Item=int(input("Enter item to be pushed: "))
            push(Item)
            print(stk)

        else:
            pop()
            print(stk)   


    elif dst.lower()=='que':
        ch=int(input("Slect 1 for Q_insertion and 2 for Q_deletion:"))
        if ch==1:
            item=int(input("enter element to be inserted:  "))
            Q_insertion(item)
            print(Q)

        else:
           Q_deletion()  
           print(Q)   
    
    elif dst.lower()=='cq':
        c=int(input(" type 1 for CQ_insertion and 2 for CQ_deletion"))
        if c==1:
            item=int(input("Enter item to be inserted"))
            CQ_insertion(item)
            print(CQ)

        else:
             CQ_deletion()
             print(CQ)

    run_again=input("do you want to run it again: (y/n)")
    if run_again.lower()=="y":
        menu()
    else:
        print("Exiting the program")
    
def traverse():
    global A,N,LB
    l = len(A)  
    print(f"Length of array is {l}")
    print("Array elements are:")
    for i in range(LB, N + LB):
        print(A[i])
    return A

def insertion(k, item):
    global N ,A,LB
    if N == S:
        print("No more insertion as array is full")
        return A
    if k < LB or k > N + LB:
        print("Invalid index")
        return A
    for i in range(N + LB - 1, k - 1, -1):
        A[i + 1] = A[i]
    A[k] = item
    N += 1
    return traverse()

def deletion( I):
    global N,LB,A
    if N == 0:
        print("No deletion as array is empty")
        return A

    if I < LB or I > N + LB - 1:
        print("Given index is invalid")
        return A

    for i in range(I, N + LB):
        A[i] = A[i+1]
    N -= 1
    return  N

def lin_sin_search( ):
    global A, LB, N
    item = int(input("Enter the element to search: "))
    found = False
    for i in range(LB, N + LB):
        if A[i] == item:
            found = True
            break
    if found:
        print(f"Element {item} found at index {i}")
    else:
        print(f"Element {item} not found")

 

def lin_mul_search(item):
    global A,LB,N
    count=0
    for i in range(LB,N+LB):
        if A[i]==item:
            count+=1
    if count==0:
                print(f"Item {item} not found n array")
                return A
    print(f"item {item} found for {count } times") 
    return item 
    
def bin_sin_search(item):
    global A,N,LB
    low=LB
    high=N+LB-1
    while(low<=high):
        mid=(low+high) // 2
        if A[mid]==item:
            print(f"Item {item} found in array")
            return item
        elif A[mid]>item:
            high=mid-1

        else:
            low=mid+1

    print(f"item {item} not found in array")
    return A

def bin_mul_search(item):
    global A,LB,N
    low=LB
    high=N+LB-1
    count=0
    while(low<=high):
        mid=int((low+high)/2)
        if A[mid]==item:
            count+=1
            left=mid-1
            right=mid+1
            while(left>=LB)and (A[left]==item):
                count+=1
                left-=1
            while(right<len(A))and(A[right]==item) :
                count+=1
                right+=1

            return A
        elif A[mid]>item:
            low=mid+1
        else:
            high=mid-1
    return -1                       


def bubble_sort():
    global A,LB,N
    choice=int(input("Selct 1 for ascending and 2 for descending order:"))
    if choice==1:
        print("Ascending order sortion")
        last = N + LB - 1
        for i in range(LB, last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        last-=1
        return A
    else:
        print("Descending order")
        last=N+LB-1
        for i in range(LB,last):
            if A[i]<A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
            last-=1
        return A        

def selection_sort( ):
    global A,LB,N
    choice=int(input("Selct 1 for ascending and 2 for descending order:"))
    if choice==1:
        print("Ascending order sortion") 
        first=LB
        while(first < len(A)-1):
            minloc=first
            for i in range(first+1,N+LB):
                if A[minloc]>A[i]:
                    minloc=i
            A[minloc]=A[first]
            first+=1
        return A     
    else:
        print("Descending order") 
        first=LB
        while(LB,len(A)-1):
            minloc=first
            for i in range(first+1,N+LB):
                if A[minloc]<A[i]:
                    minloc=i
            A[minloc]=A[first]
            first+=1
        return A             

def insertion_sort( ):
   global A,LB,N
   choice=int(input("Selct 1 for ascending and 2 for descending order:"))
   if choice==1:
        print("Ascending order sortion")  
        last=LB+1
        while(LB<len(A)):
            L=A[last]
            i=last-1
            while(i>=LB)and(A[i]>L):
                A[i+1]=A[i]
            A[i+1]=L
            last+=1
        return A            
           
   else:
        print("Descending  order sortion") 
        last=LB+1
        while(LB<len(A)):
            L=A[last]
            i=last-1
            while(i>=LB)and(A[i]<L):
                A[i+1]=A[i]
            A[i+1]=L
            last+=1
        return A             
                    
def shell_sort():
    global A,LB,N
    choice=int(input("Selct 1 for ascending and 2 for descending order:"))
    if choice==1:
        print("Ascending order sortion") 
        Gap=N//2
        while(Gap!=0):
            for last in range(LB+Gap,N+LB):
                L=A[last]
                i=last-Gap
                while(i>=LB)and (A[i]>L):
                    A[i+Gap]=A[i]
                    i=i-Gap
                A[i+Gap]=L
            Gap=Gap//2
        return A
    else:
        print("Descending order") 
        Gap=N//2
        while(Gap!=0):
            for last in range(LB+Gap,N+LB):
                L=A[last]
                i=last-Gap
                while(i>=LB)and (A[i]<L):
                    A[i+Gap]=A[i]
                    i=i-Gap
                A[i+Gap]=L
            Gap=Gap//2
        return A 
                          
def push(Item):
    global   LB,stk,top,size 
    if top==size +LB-1:
        print("Stack is full")
        return top
    top+=1
    stk[top]=Item
    return stk

def pop():
    global stk,LB,top
    if top==LB-1:
        print("Stack is empty")
        return top
    
    item=stk[top]
    top-=1
    return item,stk,top

def Q_insertion(item):
    global Q,LB,F,R
    if (R==size +LB-1):
        print("Queue is full, no insertion")
        return R
    if (R==LB-1):
        R=LB
        F=LB
    else:
        R+=1

    Q[R]=item  
    return Q

def Q_deletion():
    if F==LB-1:
        print("Q is empty")
        return Q
    item=Q[F]
    if(F==R):
        F=LB-1
        R=LB-1
    else:
        F+=1

    return Q    

def CQ_insertion(item):
    global F,R,size,CQ
    if ((F==LB)and(R==size +LB-1))or(F==R-1):
        print("No more insertion cause it's full")
        return CQ
    
    if R==LB-1:
        R+=1
        F+=1
    elif R==size+LB-1:
        R=LB
    else:
        R+=1

    CQ[R]=item
    return CQ    

def CQ_deletion():
    global CQ,LB,size,F
    if (F==LB-1):
        print("Q is empty ")
        return CQ
    
    item=CQ[F]

    if(F==R):
        F=LB-1
        R=LB-1
    elif (F==size+LB-1):
        F=LB
    else:
        F+=1

    return CQ            
    
        
            
menu()