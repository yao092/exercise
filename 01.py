x = input('輸入正整數：')
y = []

for a in range(len(x)):
    for b in range(a+1):
        c = int(x[b : len(x)-a+b])
        if c % 2 == 1 :
            d= []
            for e in range(1,c+1):
                if c % e == 0 :
                    d.append(e)
            if len(d) == 2 :
                y.append(c)
                

if len(y) == 0:
    print('子字串最大的質數值是：No prime found')
elif len(y) == 1 and 1 in y:
    print("子字串中最大的質數值是 : No prime found")
else:
    print("子字串中最大的質數值是 : ",max(y))