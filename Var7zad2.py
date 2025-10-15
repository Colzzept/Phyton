n = int(input("Введите размер массива: "))
a = []

print("Введите элементы масс\ива:")
for i in range(n):
    x = int(input())
    a.append(x)

mi = 0
ma = 0

for i in range(n):
    if a[i] < a[mi]:
        mi = i
    if a[i] > a[ma]:
        ma = i

t = a[mi]
a[mi] = a[ma]
a[ma] = t

print("Результат:")
for x in a:
    print(x)