a=6
b=7

c=1

print(1/2)

for i in range(20):
    c=c*(a/b)
    if(c<1/2):
        c=c*2
        print("{0:2d}: {1:.5f}      誤差:{2:.4}%".format(i, c, (1-c)*100))
    else:
        print("{0:2d}: {1:.5f}      誤差:{2:.4}%".format(i, c, (1-c)*100))
