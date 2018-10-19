# n=int(input())
# q=0
# a=1
# c=1
# while (a!=n and c<99999):
#     a=c
#     s = str(c)
#     j=len(s)
#     for i in range(j):
#         # if (i>0):
#         a=a*int(s[i])
#             # print(a)
#     a=a/c
#     c=c+1
#
# # print(a)
# if (c==99999):
#     print(-1)
# elif(c==1):
#     print(1)
# else:
#     print(c-1)

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac

n=int(input())

a = primfacs(n)
print(a)