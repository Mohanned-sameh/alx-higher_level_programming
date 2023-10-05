def magic_calculation(a, b):
from magic_caluclation_102 import add, sub

if a < b:
    c = add(a, b)
    for i in range(4, 6):
        c = add(c, i)
        return (c)
    return (sub(c, b))