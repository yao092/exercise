from tkinter import Y


x=int(input("請輸入階層值M:"))
y=0
sum=1

while True:
    y+=1
    sum*=y
    if sum > x:
        print("超過M為%d的最小階層N值為%d" % (x,y))
        break    