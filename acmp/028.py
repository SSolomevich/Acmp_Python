a = input().split()
b = input().split()
result_1=0
result_2=0

if (int(a[0])==int(a[2])):
    result_1 = int(a[0])+int(a[0]) - int(b[0])
    result_2 = int(b[1])
else:
    result_2 = int(a[1])+int(a[1]) - int(b[1])
    result_1 = int(b[0])
print(str(result_1)+' '+str(result_2))