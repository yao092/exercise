x= input("輸入一組四位數字為:")
y = []
for i in range(4):
    y.append((int(x[i])+7)*0.1)

z = [0,0,0,0]
z[0] = y[2]
z[1] = y[3]
z[2] = y[0]
z[3] = y[1]

print("輸出加密後的數字為:",end="")
for k in range(4):
    if z[k] >= 1:
        z[k] = z[k] - 1
    z[k] = int(z[k] * 10)
    print(z[k],end="")