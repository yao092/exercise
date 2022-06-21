x = int(input("輸入組數:"))
y = []

for a in range(x):
    y.append(input(f"第{a+1}組:"))

m = []
n = []

for i in range(x):
    m.append(int(y[i][0]))
    n.append(int(y[i][2]))

z = []

for j in range(x):
    z.append(m[j]*250 + n[j]*175)
    print(f"第{j+1}組應收費用:{z[j]}")