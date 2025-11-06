n = int(input())
m = int(input())
matr = []
for i in range(n):
    a = list(map(int, input().split()))
    matr.append(a)
for a in matr:
    minel = min(a)
    for j in range(m):
        if a[j] == minel:
            a[j] = 0 if minel % 2 == 0 else 1

for a in matr:
    print(*a)