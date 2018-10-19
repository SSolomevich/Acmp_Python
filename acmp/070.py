s1 = input()
s2 = int(input())
y = 0

def multiply_anything(sth, size):
    return ''.join(["%s" % sth for s in range(size)])
if (s2 > 0):
    s3=''
    # s3 = s1 * s2
    # s3=multiply_anything(s1, s2)
    # n = s1.encode()
    # s3 = bytearray('string', 'ascii')
    # s3 = n*s2
    i=0
    while (len(s3)<1024 and i<s2):
    # for i in range(s2):
        s3=s3+s1
        i=i+1

    if (len(s3) > 1023):
        print(s3[:1023])
    else:
        print(s3)
elif (s2 < 0):


    s3 = s1[:int(len(s1) / (-s2))]

    if (float(len(s1)) / (-s2) != len(s3) or len(s1) / (-s2) == 0 or len(s3) == 0):
        print('NO SOLUTION')

    else:

        # for i in range(0, len(s1), int(len(s1) / (-s2))):
        #
        #     if (s3 != s1[i:i + int((len(s1) / (-s2)))]):
        #         y = 1
        #         break
        s4 = s3*(-s2)
        if (s4!=s1):
            y=1
        if (y == 0):
            if (len(s3) > 1023):
                print(s3[:1023])
            else:
                print(s3)

        else:
            print('NO SOLUTION')