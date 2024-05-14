# Define queue size
size = 4

# Initialize queues with None values
Q = [None] * size
CQ = [None] * size

# Variables for queue operations (no built-in functions)
LB = 0  # Lower bound (index of the first element)
F = LB - 1  # Front (initially empty)
R = LB - 1  # Rear (initially empty)
class Queue:

   def Q_insertion(item):
    global Q, LB, F, R

    # Check for full queue
    if (R == size + LB - 1):
        print("Queue is full, no insertion")
        return Q

    # Handle empty queue or wrap-around case
    if (R == LB - 1):
        R = LB
        F = LB
    else:
        R += 1

    # Insert item at the rear
    Q[R] = item

    print("Queue after insertion:", Q)
    return Q


def Q_deletion():
    """Deletes an item from the queue (linear queue).

    Returns:
        The updated queue or a message if the queue is empty.
    """

    global Q, LB, F, R

    # Check for empty queue
    if (F == LB - 1):
        print("Queue is empty")
        return Q

    # Remove item from the front
    item = Q[F]

    # Handle single-element queue or wrap-around case
    if (F == R):
        F = LB - 1
        R = LB - 1
    else:
        F += 1

    print("Queue after deletion:", Q)
    return item


def CQ_insertion(item):
    """Inserts an item into the circular queue.

    Args:
        item: The item to be inserted.

    Returns:
        The updated queue or a message if the queue is full.
    """

    global F, R, size, CQ

    # Check for full queue (using two conditions)
    if ((F == LB) and (R == size + LB - 1)) or (F == R - 1):
        print("No more insertion cause it's full")
        return CQ

    # Handle empty queue or wrap-around cases
    if (R == LB - 1):
        R += 1
        F += 1
    elif (R == size + LB - 1):
        R = LB
    else:
        R += 1

    # Insert item at the rear
    CQ[R] = item

    print("Circular Queue after insertion:", CQ)
    return CQ


def CQ_deletion():
    """Deletes an item from the circular queue.

    Returns:
        The removed item or a message if the queue is empty.
    """

    global CQ, LB, size, F

    # Check for empty queue
    if (F == LB - 1):
        print("Queue is empty")
        return CQ

    # Remove item from the front
    item = CQ[F]

    # Handle single-element queue or wrap-around cases
    if (F == R):
        F = LB - 1
        R = LB - 1
    elif (F == size + LB - 1):
        F = LB
    else:
        F += 1

    print("Circular Queue after deletion:", CQ)
    return item