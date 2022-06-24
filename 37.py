x = int(input("請輸入一個數"))
y = []

while True:
    if x == 1:
        s = ""
        for i in range(len(y)):
            s =s + str(y[i])+" "
        print("數列 : "+s)
        print("cycle length :",len(y));
        break

    if x % 2 == 0:
        x = x /2 
        y.append(int(x))

    elif x % 2 == 1:
        x = 3 * x + 1
        y.append(int(x))

    