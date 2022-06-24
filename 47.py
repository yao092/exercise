x=int(input("輸入筆數n: "))
y=["金","銀","銅","優"]
l=[]

for i in range(4):
    a=int(input(y[i]))
    if a>x:
        a=x
    l.append(a)

for i in range(4):
    print(str(y[i])+"牌得到"+str(l[i])+"面")