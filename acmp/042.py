# def count(n, k):
#     if n == 0:
#         c = 1
#         for i in range(len(a) - 1):
#             print(a[i], end="+")
#             c = c*a[i]
#         print(a[len(a) - 1])
#         global cnt
#
#         c = c*a[len(a) - 1]
#         if (c>cnt):
#             cnt=c
#
#     for i in range(k, n + 1):
#
#         a.append(i)
#         count(n - i, i)
#
#         a.pop(len(a) - 1)
#
#
# b=[]
# a = []
# cnt = 1
#
# n = int(input())
# count(n, 1)
# print(cnt)
n = int(input())
res = 1
while (n>0):
    if (n-3>4):
        res = res * 3
        n = n - 3
    elif (n==7):
        res = res * 4 *3
        n = n - 7
    elif (n==6):
        res = res * 3 *3
        n = n - 6
    elif (n==5):
        res = res * 2 *3
        n = n - 5
    elif (n==4):
        res = res * 4
        n = n - 4
    elif (n==3):
        res = res * 3
        n = n - 3
    elif (n==2):
        res = res * 2
        n = n - 2
    else:
        break
print(res)


















