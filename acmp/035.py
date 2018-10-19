k = int(input())
a = []
for i in range(k):
    a = input().split()

    d = 19*int(a[1]) + (int(a[0]) + 239)*(int(a[0]) + 366) / 2
    print(int(d))