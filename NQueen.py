from math import *

x = {}
n = int(4)  # Chess Board n*n and number of columns


def clear_future_blocks(k):
    # Initialise k row dict for chess board n*n
    for i in range(k, n + 1):
        x[i] = None  # future clear row
    # print(x)


def place(k, i):
    if (i in x.values()):  # if queen is placed in same column
        return False
    j = 1  # position in that column
    while (j < k):  # if queen is placed in diagonal
        if abs(x[j] - i) == abs(j - k):
            return False
        j += 1
    return True


def NQueens(k):  # K Number of moves
    for i in range(1, n + 1):  # NUMBER OF POSSIBLE SOLUTION
        clear_future_blocks(k)  # clear row
        if place(k, i):  # k queen in  i col
            x[k] = i  # can place queen in that position
            if (k == n):
                for j in x:
                    print(x[j], end=' ')
                print('\n-------')
            else:
                NQueens(k + 1)


NQueens(1)  # here 1 queen to placed
