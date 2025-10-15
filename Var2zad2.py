N = int(input("Введите размер массива: "))
a = []

for i in range(N):
    e = int(input(f"Введите элемент {i+1}: "))
    a.append(e)

b = []  
c = []    

for e in a:
    if e > 0:
        b.append(e)
    else:
        c.append(e)

print(f"Исходный массив: {a}")
print(f"Массив положительных элементов: {b}")
print(f"Массив остальных элементов: {c}")