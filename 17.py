m = []
x1, y1 = input("第一個矩陣大小:").split()
x1, y1 = int(x1), int(y1)
for i in range(x1):
    n= input().split()
    n= list(map(int, n))
    m.append(n)

a= []
x2, y2 = input("第二個矩陣大小:").split()
x2, y2 = int(x2), int(y2)
for i in range(x2):
    b = input().split()
    b = list(map(int, b))
    a.append(b)

if x1 == x2 and y1 == y2:
    z = []
    for i in range(x1):
        z.append([])
        for j in range(y1):
            z[i].append(m[i][j]+a[i][j])
else:
    print("兩個矩陣無法相加")