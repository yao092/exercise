x=input("輸入值為:")
y=x.split(",")
z=sorted(y)
j=sorted(y,reverse=True)
a1=""
a2=""
for i in range(len(y)):
    a1+=j[i]
    a2+=z[i]
print("最大值數列與最小值數列差值為:%s"%(int(a1)-int(a2)))