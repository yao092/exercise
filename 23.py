a = int(input("輸入值n為:"))

if a == -1 :
    pass
elif 0<a<=100:
    print(round(a**3 / 3,1))
else:
    print('輸入100內的正整數')