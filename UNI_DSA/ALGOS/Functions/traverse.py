#                               TRAVERSAL CODE
# This function is used to traverse the array from the given lower bound to the upper bound.
from arrayfile import A, N, LB


def Traverse():
    global N, LB
    for i in range(LB, N+LB):
        print(A[i], end=',')
    print("...........................")
