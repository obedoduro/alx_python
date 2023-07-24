for i in range(10):
    for j in range(i + 1, 9):
        print("{}{}, ".format(i, j), end = '')
    if i == 9:
        print("{}{} ".format(j, i), end = '')
