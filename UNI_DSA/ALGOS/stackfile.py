LB=0
size = 4
my_stack=[None] * size
top = LB-1


class Stack:

    """
    This class implements a stack data structure with push, pop, delete,
    size, and display functionality, while avoiding the use of specific built-in functions.
    """
   
    def push(item):
        global LB, my_stack, top, size

        if top == size + LB - 1:
            print("Stack overflow")
            return top  # Indicate stack overflow

        top += 1
        my_stack[top] = item
        print("Pushed:", item)
        display_stack()  # Display stack contents after push
        return my_stack  # Return the updated stack

    def pop():
        global my_stack, LB, top

        if top == LB - 1:
            print("Stack underflow")
            return top  # Indicate stack underflow

        item = my_stack[top]
        top -= 1
        print("Popped:", item)
        display_stack()  # Display stack contents after pop
        return item

    def delete(item):
        global my_stack, LB, top

        if top == LB - 1:
            print("Stack is empty.")
            return None

        found = False

        # Iterate from top to bottom, overwriting elements with None if the item is found
        for i in range(top, LB - 1, -1):
            if my_stack[i] == item:
                found = True
                my_stack[i] = None  # Overwrite the item with None

        # Update top by counting the number of deleted items
        if found:
            num_deleted = 0
            for i in range(top, LB - 1, -1):
                if my_stack[i] is None:
                    num_deleted += 1
            top -= num_deleted
            print("Deleted item(s):", item)  # Pluralize "item" if multiple deleted
            display_stack()  # Display stack contents after deletion
            return item
        else:
            print("Item not found in the stack.")
            return None


def display_stack():
    global my_stack, LB, top

    if top == LB - 1:
        print("Stack is empty.")
        return

    print(".........Stack contents Top to Bottom :")
    for i in range(top, LB - 1, -1):
        print(my_stack[i])

   