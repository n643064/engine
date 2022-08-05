def translate(m1, m2):
    out = []
    m2 = switch(m2)
    for row in m1:
        r = []
        for column in m2:
            c = 0
            for i in range(0, len(row)):
                c += row[i] * column[i]
            r.append(c)
        out.append(r)
    return out


def switch(m):
    m2 = []
    for i in range(0, len(m[0])):
        c = []
        for row in m:
            c.append(row[i])
        m2.append(c)
    return m2



"""
    [ x y z ]
    [ a b c ]
    [ 1 2 3 ]

"""