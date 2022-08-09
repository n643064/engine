def multiply(m1, m2, should_switch=False):
    out = []
    if should_switch:
        m2 = switch(m2)
    for row in m1:
        r = []
        for column in m2:
            r.append(dot_product(row, column))
        out.append(r)
    return out

def dot_product(a1, a2):
    out = 0
    for i in range(len(a1)):
        out += a1[i]*a2[i]
    return out

def switch(m):
    m2 = []
    for i in range(0, len(m[0])):
        c = []
        for row in m:
            c.append(row[i])
        m2.append(c)
    return m2

