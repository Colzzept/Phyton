def r(a,b):
    if a<b:
        return a
    return r(a-b,b)

a=int(input("Введите a: "))
b=int(input("Введите b: "))
print(r(a,b))