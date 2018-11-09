from math import sqrt
s = input().split(' ')
resX=0
resY=0
n12 = (int(s[0])-int(s[2]))*(int(s[0])-int(s[2]))+(int(s[1])-int(s[3]))*(int(s[1])-int(s[3]))
n23 = (int(s[2])-int(s[4]))*(int(s[2])-int(s[4]))+(int(s[3])-int(s[5]))*(int(s[3])-int(s[5]))
n31 = (int(s[4])-int(s[0]))*(int(s[4])-int(s[0]))+(int(s[5])-int(s[1]))*(int(s[5])-int(s[1]))

if ((n31+n23)==(n12)):
    resX = int(s[0]) + int(s[2]) - int(s[4])
    resY = int(s[1]) + int(s[3]) - int(s[5])
elif((n31+n12)==(n23)):
    resX = int(s[2]) + int(s[4]) - int(s[0])
    resY = int(s[3]) + int(s[5]) - int(s[1])
elif((n23+n12)==(n31)):
    resX = int(s[0]) + int(s[4]) - int(s[2])
    resY = int(s[1]) + int(s[5]) - int(s[3])

print (str(resX)+' '+str(resY))