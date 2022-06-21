a=input("輸入N及M")
b=a.split(" ")
c=[]
d=[]
e=""
f=[]
for i in range(int(b[0])):
    c.append(input("輸入矩陣數值第%d列為" %(i+1)))
for j in range(len(c)):
    d.append(c[j].split(" "))
for x in range(int(b[1])):
    for y in range(int(b[0])):
        e+="%s "%(d[y][x])
    f.append(e)
    e=""
for z in range(len(f)):
    print("輸出矩陣數值第%s列為%s" %(int(z)+1,f[z]))