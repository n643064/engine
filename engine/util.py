def print_matrix(m):
    for row in m:
        print("[ ", end="")
        for e in row:
            print(e, end=" ")
        print("]")