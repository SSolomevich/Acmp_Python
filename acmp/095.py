s = input()
n = int(s)
res1 = n
res2 = 0
while (res1>9):
    a=res1
    res1=0
    res2 = res2+1
    for i in range(len(str(a))):

        res1 = res1+a%10
        a = a//10
        # print(res1)
        # print(a)
print(str(res1)+' '+str(res2))
