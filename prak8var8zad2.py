n = int(input())
m = int(input())
matr = []
for i in range(n):
    a = list(map(int, input().split()))
    matr.append(sorted(a))
for a in matr:
    print(*a)