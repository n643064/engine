from math import sin, cos, radians, pi
from engine.math import multiply
def print_matrix(m):
    s = 4
    for row in m:
        print("[ ", end="")
        for e in row:
            l = len(str(e))
            s = max(l, s)
            print(e, end=" " * (s - l+1))
        print("]")

def project(model, p_matrix):
    model2 = []
    for p in model:
        model2.append((multiply(p, p_matrix)))
    return model2


def read_model(path):
    try:
        file = open(path, "r")
    except FileNotFoundError:
        print("Couldn't open model file: " + path + ".")
        return None
    except Exception as e:
        print("An exception has occurred when opening model file.")
        return None
    m = []
    for line in file.readlines():
        if not line.startswith("("):
            continue
        p1, p2 = line.replace("(", "").replace(")", "").replace(" ", "").split(":")
        p1 = p1.split(",")
        p2 = p2.split(",")
        start, end = [], []
        for s in p1:
            start.append(int(s))
        start.append(1)
        for s in p2:
            end.append(int(s))
        end.append(1)
        m.append((start, end))

    return m

def rotate_x(m, a):
    r_m = [
        (1, 0, 0),
        (0, cos(radians(a)), -sin(radians(a))),
        (0, sin(radians(a)), cos(radians(a)))
    ]
    return multiply(m, r_m)

def rotate_y(m, a):
    r_m = [
        (cos(radians(a)), 0, sin(radians(a))),
        (0, 1, 0),
        (-sin(radians(a)), 0, cos(radians(a)))
    ]
    return multiply(m, r_m)

def rotate_z(m, a):
    r_m = [
        (cos(radians(a)), -sin(radians(a)), 0),
        (sin(radians(a)), cos(radians(a)), 0),
        (0, 0, 1)
    ]
    return multiply(m, r_m)
