x=input("測試的資料量:")
for i in range(int(x)):
    y=input("輸入父母以女的血型空格隔開").split()
    z=[y[0].lower(),y[1].lower()]
    j=y[2].lower()
    if "a" in z and "b" in z:
        print("YES")
    elif "ab" in z and "a" in z or "ab" in z and "b" in z or z[0]==z[1]=="ab":
        if j !="o": print("YES")
        else: print("IMPOSSIBLE")
    elif z[0]==z[1]=="o":
        if j=="o": print("YES")
        else: print("IMPOSSIBLE")
    elif "o" in z and "a" in z or z[0]==z[1]=="a":
        if j=="a" or j=="o": print("YES")
        else: print("IMPOSSIBLE")
    elif "o" in z and "b" in z or z[0]==z[1]=="b":
        if j=="b" or j=="o": print("YES")
        else: print("IMPOSSIBLE")
    elif "o" in z and "ab" in z:
        if j=="a" or j=="b":print("YES")
        else:print("IMPOSSIBLE")