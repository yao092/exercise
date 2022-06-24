a=int(input("共T筆測試資料(1<=T<=20):"))

for m in range(a):
    b=[]
    a=0
    for j in range(0,4):
        b.append(int(input()))
    if b[1]-b[0]==b[2]-b[1]==b[3]-b[2]:
        b.append(b[3]+b[3]-b[2])
        for m in range(len(b)):
         print("%d"%(b[m]),end=" ")
        print("\n此為等差數列")
    elif b[1]/b[0]==b[2]/b[1]==b[3]/b[2]:
        b.append(b[3]*b[2]/b[1])
        for m in range(len(b)):
         print("%d"%(b[m]),end=" ")
        print("\n此為等比數列")
    else:
        print('這不是數列')