s1=input().split(':')
s2=input().split(':')
h=int(s1[0])
m=int(s1[1])
s=int(s1[2])
ss1 = h*3600+m*60+s
ss2 = 0
if (len(s2)==1):
    ss2 = int(s2[0])
elif(len(s2)==2):
    ss2 = int(s2[1])+int(s2[0])*60
elif (len(s2) == 3):
    ss2 = int(s2[2]) + int(s2[1]) * 60 +int(s2[0])*3600
sRes=ss1+ss2
# print(ss2)
# print(sRes)
d=sRes//86400
h=(sRes-d*86400)//3600
m=(sRes-d*86400-h*3600)//60
s=sRes-d*86400-h*3600-m*60
# print(s)
sR=''
mR=''
hR=''
if(h<10):
    hR='0'+str(h)
else:
    hR=str(h)
if(m<10):
    mR='0'+str(m)
else:
    mR=str(m)
if(s<10):
    sR='0'+str(s)
else:
    sR=str(s)
if (d==0):
    print(hR+':'+mR+':'+sR)
else:
    print(hR + ':' + mR + ':' + sR + '+'+str(d)+' days')


