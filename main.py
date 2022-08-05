from engine.math import translate
from engine.util import print_matrix


m1 = [
    [1, 2, 3],
    [4, 5, 6]
]

m2 = [
    [7, 8],
    [9, 10],
    [11, 12],

]

print_matrix(translate(m1, m2))