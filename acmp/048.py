# from _pydecimal import Decimal
#
# n = int(input())
# a=0
# result = 1
# while (a == 0):
#     a=n%10
#     n = n/10
#     result = result*10
# result = Decimal(result/10)
# print(result)

s = input()
res = '1'
for i in range(len(s)-1,0,-1):
    if (s[i]=='0'):
        res = res + '0'
    else:
        break
print(res)