s1 = input()
n = int(s1)
s = 0

while (n > 0):
    s = s + n % 2
    n = n // 2
print(s)