def vtormaximal(max1=0, max2=0):
    n = int(input())
    if n == 0:
        return max2
    if n > max1:
        return vtormaximal(n, max1)
    elif n > max2:
        return vtormaximal(max1, n)
    else:
        return vtormaximal(max1, max2)
print("Введите последовательность:")
print(vtormaximal())