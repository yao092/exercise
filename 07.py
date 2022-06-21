x = int(input("請輸入月租費形式："))
y = int(input("請輸入通話時間："))

if x == 186 :
    z = round(y*0.09)
    if z<=186 :
        print("通話費為：186")
    else :
        if z <= (186*2):
            z = round(z*0.9)
            print("通話費為：" , z)
        elif z > (186*2):
            z = round(z*0.8)
            print("通話費為：" , z)
elif x == 386 :
    z = round(y*0.08)
    if z<=186 :
        print("通話費為：386")
    else :
        if z <= (386*2):
            z = round(z*0.8)
            print("通話費為：" , z)
        elif z > (386*2):
            z = round(z*0.7)
            print("通話費為：" , z)
elif x == 586 :
    z = round(y*0.07)
    if z<=186 :
        print("通話費為：586")
    else :
        if z <= (586*2):
            z = round(z*0.7)
            print("通話費為：" , z)
        elif z > (586*2):
            z = round(z*0.6)
            print("通話費為：" , z)
elif x == 986 :
    z = round(y*0.06)
    if z<=986 :
        print("通話費為：986")
    else :
        if z <= (986*2):
            z = round(z*0.6)
            print("通話費為：" , z)
        elif z > (986*2):
            z = round(z*0.5)
            print("通話費為：" , z)