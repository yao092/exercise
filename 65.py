x = input("請輸入A的好友:").split()
y = input("請輸入B的好友:").split()
n = 0

for i in range(len(x)):
    if x[i] in y:
        n += 1
print(n)