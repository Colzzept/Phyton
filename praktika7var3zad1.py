import math
def treugol(a):
    return math.sqrt(3) / 4 * a ** 2
def shestiug(a):
    return 6 * treugol(a)
a = float(input())
print(shestiug(a))