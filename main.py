from engine.math import translate
from engine.util import print_matrix


m1 = [
    (1, 2, 3),
    (4, 5, 6)
]

m2 = [
    (2, 3),
    (2, 3),
    (2, 3)
]

print_matrix(translate(m1, m2))