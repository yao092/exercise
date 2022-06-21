x = list(input("輸入一整數序列為 :").split())
y = []

for j in range(len(x)):
    z = 0 
    for k in range(len(x)):
        if x[j] == x[k] :
            z += 1
        
    y.append(z)

if max(y) > len(x)/2 :
    print("過半元素為:",x[y.index(max(y))])
else:
    print("過半元素為: NO")