a = int(input("請輸入月份"))
b = int(input("請輸入日期"))
d = (a*2+b)%3

if d == 0:
    print("普通")
elif d == 1:
    print("吉")
elif d == 2:
    print("大吉")
else:
    print("大凶")