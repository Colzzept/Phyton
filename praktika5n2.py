s = input("введите строку: ")
n = len(s)
c = n // 2
z = s[:c].replace('п', '.') + s[c:]
print(z)