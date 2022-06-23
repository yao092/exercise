x = int(input("請輸入陣列大小"))
a =[[]for i in range(x)]
b =[]

for i in range(x):
    a[i] = input("請輸入第"+str(i+1)+"列數值").split()
    b.extend(a[i])

for i in range(len(b)):
    b[i] = int(b[i])
b.sort();b.reverse()

for i in range(3):
    
    for j in range(x):
        if str(b[i]) in a[j]:
            print("(",j,",",a[j].index(str(b[i])),")" ,end="")
