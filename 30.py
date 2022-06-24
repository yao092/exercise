o = ['1','2',"3","4"]

while True:
    x=0
    y=0
    z =list(input('猜四位數字:'))
    if z.count('0')==4:
        print('結束')
        break
    
    if len(z)==4:
        for i in range(4):
            if (o[i]==z[i]):
                x+=1
            elif(o.count(z[i])==1 and o[i]!=z[i]):
                y+=1
        print(str(x)+'A',str(y)+"B")
    elif len(z)!=4:
        print('輸入錯誤')
    if x==4:
        break