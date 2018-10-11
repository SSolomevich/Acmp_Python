a=int(input())
summ=0
for b in range(a):
    if (b>0 and  a%b==0):
        summ=summ+b
print(summ+a)
