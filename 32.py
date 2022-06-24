x = int(input("請輸入小明現在擁有多少錢"))
y = int(input("請輸入販賣機有幾種飲料"))
p = []
c= 0

for i in range(y):
    p.append(int(input("請輸入第"+str(i+1)+"種飲料的價錢")))
    if p[i] <= x :
        c += 1

print("小明可以買",c,"種飲料")