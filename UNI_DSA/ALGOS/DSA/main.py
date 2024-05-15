from arrayfile import Array  
from stackfile import Stack  
from queuefile import Queue  
    
print("how many times you want to do operations")
total_operations=int(input())
    
def array():
    for i in range(total_operations):
        print("Select one Operation in given below")
        print("For Traversing press 1")
        print("For Insertion press 2")
        print("For Searching press 3")
        print("For Sorting press 4")
        print("For Merging press 5")
        print("For Deletion press 6")
        print("For Exit press 7")
        print("...........................")
        OP = int(input())
        if OP == 1:
            print(OP, ":Traverse Selected")
            Array.Traverse()
        elif OP == 2:
            print(OP, ":Insetion Selected")
            Array.Insertion()
        elif OP == 3:
            print(OP, ":Searching Selected")
            Array.Searching()
        elif OP == 4:
            print(OP, ":Sorting Selected")
            Array.Sorting()
        elif OP == 5:
            print(OP, ":Merging Selected")
            Array.Merging()
        elif OP == 6:
            print(OP, ":Deletion Selected")
            Array.Deletion()
        elif OP == 7:
            print("Exiting...")
            break
        else:
            print("Invalid Option")



    

def stack():
    try:
        for i in range(total_operations):
            print("............Select the choices given Below..........")
            print("1:PUSH")
            print("2:POP")
            print("3:EXIT")
            
            choice = int(input())
            if choice == 1:
                print("which item you want to push")
                item = int(input())
                Stack.push(item)
            elif choice == 2:
                Stack.pop()
            elif choice == 3:
                print('Exiting..')
                break
            else:
                print("Invalid choice")
        
    except ValueError as e:
        print(f"Error: {e}")
        
        
def queue():
    try:
        for i in range(total_operations):
            print(".................which one do you want:")
            print("1:simple queue")
            print("2:circular queue")
            print("3:Exit")
            choice = int(input())
            if choice == 1:
                print("1:queue insert")
                print("2:queue delete")
                op = int(input())
                if op == 1:
                    print("Enter the item to be  insert in simple queue")
                    item = int(input())
                    Queue.Q_insertion(item)
                if op == 2:
                    Queue.Q_deletion()
            elif choice == 2:
                print("1:circular insert:")
                print("2:circular delete:")
                op = int(input())
                if op == 1:
                    print("Enter the item to be insert circular")
                    item = int(input())
                    Queue.CQ_insertion(item)
                if op == 2:
                    Queue.CQ_deletion()
            elif choice == 3:
                break
            else:
                print("invalid choice")    
    except ValueError as e:
       print(f"Error: {e}")        
        
class Main:
        print('Starting up the application......')
        print('----------------------------------------------------------------')
        print("Which operation do you want to do?...")
        print("1:ARRAY")
        print("2:STACK")
        print("3:QUEUE")
        print("4:EXIT")
        
        choice = int(input())
        while choice != 4:  # Loop until user chooses to exit the main menu
                if choice == 1:
                    array()
                elif choice == 2:
                    stack()  # Assuming you have a stack function defined
                elif choice == 3:
                    queue()  # Assuming you have a queue function defined
                else:
                    print("Invalid choice")

                print("\nDo you want to perform another operation?")
                print("1: ARRAY")
                print("2: STACK")
                print("3: QUEUE")
                print("4: EXIT")
                choice = int(input())

        print("Exiting...")
            
