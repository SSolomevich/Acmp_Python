n=int(input())
s=input().split(' ')
res=-1
for i in range(n):
    if (int(s[i])<=437):
      res=i+1
      break
if(res>-1):
    print('Crash '+str(res))
else:
    print('No crash')