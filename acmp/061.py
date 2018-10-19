n1 = input().split(' ')
n2 = input().split(' ')
n3 = input().split(' ')
n4 = input().split(' ')
res=0
if (int(n1[0])+int(n2[0])+int(n3[0])+int(n4[0])>int(n1[1])+int(n2[1])+int(n3[1])+int(n4[1])):
    print(1)
elif (int(n1[0])+int(n2[0])+int(n3[0])+int(n4[0])<int(n1[1])+int(n2[1])+int(n3[1])+int(n4[1])):
    print(2)
else:
    print('DRAW')
