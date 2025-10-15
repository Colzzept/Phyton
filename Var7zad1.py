n = int(input())
a = []

for i in range(n):
    x = int(input())
    a.append(x)

s = 0
p = 1

for i in range(n):
    if i % 2 ==0:
        s += a[i]
    else:
        p *= a[i]

print(s)
print(p)