a=21
b=21

border=0.5

print(1/2)

for j in range(1, a):
    for k in range(1, b):
        if(j<k):
            c=1.0
            for i in range(15):
                c=c*(j/k)
                if(c<1/2):
                    c=c*2
                    if((1-c)*100<border):
                        print("{0:2d}: {1:.5f}   誤差:{2:.4}%  組合:[{3}, {4}]".format(i, c, (1-c)*100, j, k))
                else:
                    if((1-c)*100<border):
                        print("{0:2d}: {1:.5f}   誤差:{2:.4}%  組合:[{3}, {4}]".format(i, c, (1-c)*100, j, k))
