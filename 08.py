x =int(input("輸入第一行正整數為?"))
y = input("第二行中數列中的數字為: ").split()
a = [] 
b = []

for j in range(x):
    c = 0 
    for k in range(x):
        if y[j] ==y[k] :
            c += 1
    a.append(c)

if sum(a) == x :
    print("每個數字剛好只出現一次")
else :
    for j in range(x):
        if a[j] == max(a):
            if y[j] not in b:
                b.append(y[j])
    ans = ""
    for k in range(len(b)):
        ans += b[k]
        if k != (len(b)-1):
            ans += ','
    print("最大出現次數的數字為",ans)
    print()
    print("出現次數為",max(a))