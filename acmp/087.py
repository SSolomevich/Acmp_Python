s = []
n = []
q=input()
while (q!='ENDOFINPUT'):
    s.append(q)
    n.append(len(q))
    q = input()
# res = 0

my_set = set()

for i in range(len(n)):
    for j in range(len(n)):
        for m in range(len(n)):
            if (n[i]==n[j]+n[m]):
                if (s[i]==s[j]+s[m]):
                    # res = res +1

                    my_set.add(s[i])

                    print(s[i])
# print(res)
print(len(my_set))