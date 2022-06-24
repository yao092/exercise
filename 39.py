x = int(input("請輸入層數以利輸出菱形"))
y =int(round(x/2,0)) 
print(y)

for i in range(x+1):
    if i <= y :
        for j in range(y-i):
            print(" " ,end="")
        for k in range(2*i-1):
            print("*" ,end="")
    else:
        for j in range(i - y):
            print(" ",end="")
        for k in range(1,(x+3),i-y):
            print("*",end="")
    print()