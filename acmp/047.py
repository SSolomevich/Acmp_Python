n = int(input())
result=1
s = 1
s3 = 0
for i in range (1,n+1):
    if (n % i == 0 ):
        s2 = str(i)
        for j in range (len(s2)):
            s3 = s3+ int(s2[j])
        if (s3 > s):
            result=i
            s=s3
            s3=0
        else:
            s3 = 0
if (result==1):
    print(n)
else:
    print(result)