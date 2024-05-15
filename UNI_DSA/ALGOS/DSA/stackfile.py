LB=0
size = 4
my_stack=[None] * size
top = LB-1


class Stack:
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

    
def display_stack():
    global my_stack, LB, top

    if top == LB - 1:
        print("Stack is empty.")
        return

    print(".........Stack contents Top to Bottom :")
    for i in range(top, LB - 1, -1):
        print(my_stack[i])

   