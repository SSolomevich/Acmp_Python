e = '2.7182818284590452353602875'
n = int(input())
if (n==0):
    print(3)
elif (n==25):
    print(e)
else:
    if (int(e[n+2])<5):
        print(e[:n+2])
    else:
        print(e[:n+1]+str(int(e[n+1])+1))