s = input()
l = ['q', 'w', 'e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

for i in range(len(l)-1):
    if (s==l[i]):
        print(l[i+1])
if (s=='m'):
    print('q')