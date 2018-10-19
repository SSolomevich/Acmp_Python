import math

s1=input()
s2=input()
s11 = s1.split()
s22 = s2.split()

distance = math.sqrt(math.pow((int(s11[0])-int(s22[0])), 2)+math.pow((int(s11[1])-int(s22[1])), 2))
if (int(s11[2])+int(s22[2])>=distance and int(s11[2])+distance>=int(s22[2]) and int(s22[2])+distance>=int(s11[2])):
    print('YES')
else:
    print('NO')