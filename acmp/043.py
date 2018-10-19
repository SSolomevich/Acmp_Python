s = input()
l = list(s)
max = 1
a = 0
if (l.count('0')==0):
    print(0)

else:

    for i in range(len(l)):

        if (int(l[i]) == 0 ):

            a = a + 1
            if (a > max):
                max = a
        else:
            a = 0

    print(max)
