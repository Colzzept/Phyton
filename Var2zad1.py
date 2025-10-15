N = int(input("Введите размер массива N: "))

arr = []
for i in range(N):
    e = int(input(f"Введите элемент {i+1}: "))
    arr.append(e)

a = arr[0]
b = 0

for i in range(1, N):
    if arr[i] < a:
        a = arr[i]
        b = i

print(f"Массив: {arr}")
print(f"Минимальный элемент: {a}")
print(f"Индекс минимального элемента: {b}")