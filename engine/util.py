def print_matrix(m):
    s = 4
    for row in m:
        print("[ ", end="")
        for e in row:
            l = len(str(e))
            s = max(l, s)
            print(e, end=" " * (s - l+1))
        print("]")