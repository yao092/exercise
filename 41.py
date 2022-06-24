x=int(input('搭了幾次電梯:'))
y=1
s=0

for i in range(0,x):
    t=int(input(i+1))
    if t-y>0:
        s=(t-y)*20+s
        y=t
    elif t-y<0:
        s=s+(y-t)*10
        y=t
        
print(s,'元')