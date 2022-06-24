n = int(input("請輸入n:"))
k = int(input("請輸入k:"))
a = n
b = 0

while True:
    b = b + (n//k)
    n = n//k
    if n < k:
        break
print("Peter可以抽",a+b,'支紙菸')