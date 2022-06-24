a = int(input("小狗有可能跑到的n個地方(2<=a<=10):"))
b = []

for i in range(a):
    b.append(int(input("小明猜想的點與家的距離k(1<=b<=1000:")))
for i in range(len(b)):
    if b[i]%9==0 or b[i]%11==0:
        print("第",str(i+1),"個點", b[i])