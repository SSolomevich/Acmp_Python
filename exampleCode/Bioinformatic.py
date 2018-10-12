# x=int(input())
# h=int(input())
# m=int(input())

# c= (h*60+m+x)
# d=5<7
# print(c//60)
# print(c%60)
# print(d)

# x = 5
# y = 10
# print(y > x * x or y >= 2 * x and x < y)

# a=int(input())
# b=int(input())
# h=int(input())
# if a<=h<=b:
#     print('Это нормально')
# elif h<a:
#     print('Hедосып')
# else :
#     print('Пересып')

# y=int(input())
# if (y%4==0 and y%100!=0):
#     print('Високосный')
# elif(y%400==0):
#     print('Високосный')
# else:
#     print('Обычный')


#
# a='123'
# b='42'
# print(a+b)
#
# gen=input()
# genom=gen.upper()
# cnst=0
# for nucle in gen:
#     cnst=cnst+1
# countg=genom.count('G')
# countc=genom.count('C')
# result=((countg+countc)/cnst)*100
# print(result)
#
# a=int(input())
# b=int(input())
# c=int(input())
#
#
# p=(a+b+c)/2
#
# s=(p*(p-a)*(p-b)*(p-c))**0.5
# print(s)

# a=int(input())
# if (-15<a<=12 or 14<a<17 or 19<=a):
#     print(True)
# else:
#     print(False)



# s=int(input())
# sum=s**2
# while (s!=0):
#     a=int(input())
#     s+=a
#     sum=sum+a**2
# print(sum)



# a=int(input())
#
# n=0
# s=0
# while (s!=a):
#     n=n+1
#     for i in range (n):
#         # print(n,' ')
#         print(n, end=" ")
#         s+=1
#         if s==a:
#             break
#     if s == a:
#         break




# lst = [int(i) for i in input().split()]
# a = int(input())
# lstRes = []
# count=0
# for i in lst:
#     if i==a:
#         lstRes.append(count)
#     count+=1
# if len(lstRes)==0:
#     print('Отсутствует')
# else:
#     lstRes.sort()
#     for i in lstRes:
#         print(i, end=" ")

# lst = [int(i) for i in input().split()]
# u=1
# a = [[lst[j] for j in range(len(lst))] for j in range(len(lst))]
# for i in range(u,len(lst)):
#     lst = [int(i) for i in input().split()]
#     a = [[lst[j] for j in range(len(lst))] for u in range(len(lst))]
#     u+=1
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         print(a[i][j], end=" ")




# c = input()
# if c == 'end':
#    print()
# else:
#     lst = [int(j) for j in c.split()]
#     n = len(lst)
#     a = []
#     m=1
#     a.append(lst)
#     while True:
#     # for i in range(1,n):
#         r = input()
#         if r=='end':
#             break
#         else:
#             lst = [int(j) for j in r.split()]
#             a.append(lst)
#             m+=1
#
#     b=[[0]*n for i in range(m)]
#
#     for i in range(n):
#         for j in range(m):
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     if 0 <= ai < n and 0 <= aj < m:
#                         # a[i][j] =  0
#                         if (-1<i<n-1 and -1<j<m-1 ):
#                             b[i][j] =  a[i-1][j]+ a[i+1][j]+ a[i][j-1]+ a[i][j+1]
#                         elif (i == n-1 and -1<j<m-1):
#                             b[i][j] = a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][j + 1]
#                             # print('e')
#                         elif (j == n - 1 and -1 < i < m - 1):
#                             b[i][j] = a[i - 1][j] + a[i+1][j] + a[i][j - 1] + a[i][0]
#                             # print('y')
#                         elif (j == n - 1 and i == m-1):
#                             b[i][j] = a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][0]
#                             # print('i')
#
#     for i in range(n):
#         for j in range(m):
#
#                 print(b[i][j] , end=' ')
#
#         print()











# def update_dictionary(d, key, value):
#     key2=key*2
#     if d.get(key)!=None:
#         d[key].append(value)
#     elif d.get(key)==None and d.get(key2)!=None:
#         d[key2].append(value)
#     elif d.get(key)==None and d.get(key2)==None:
#         d[key2] = [value]
#
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)
# update_dictionary(d, 2, -2)
# print(d)
# update_dictionary(d, 1, -3)
# print(d)

# d = {}
# lst1 = input().lower()
# lst = [i for i in lst1.split()]
#
# for i in lst:
#     if d.get(i) != None:
#         d[i] = (d[i]+1)
#     elif d.get(i)==None :
#         d[i] = 1
#
# for key,value in d.items():
#     print(key, value)



res=[]
resD1=0
resD2=0
resD3=0
cnt=0

with open('C:\\text1.txt', 'r') as doc:
    initial_list = doc.readlines()
    for i in initial_list:
        s = i.strip().split(';')
        res.append((int(s[1])+int(s[2])+int(s[3]))/3)
        resD1+=int(s[1])
        resD2 += int(s[2])
        resD3 += int(s[3])
        cnt+=1
res.append(resD1/cnt)
res.append(resD2/cnt)
res.append(resD3/cnt)

print(res)
ouf = open('C:\\text2.txt', 'w')
for i in range(len(res)-3):
    ouf.write(str(res[i])+'\n')
ouf.write(str(res[-3])+' '+str(res[-2])+' '+str(res[-1]))









