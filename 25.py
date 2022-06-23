a,b=input("請輸入考試次數及學生數：").split()
a,b=int(a),int(b)
c=input("每次考試所占的比率").split()
c=list(map(float,c))
m=[]

for i in range(b):
    m_input=input().split()
    m.append(m_input)

for i in range(len(m)):
    m[i]=list(map(int,m[i]))

n=[]

for i in range(b):
    x=0
    for j in range(a):
        x=x+m[i][j]*c[j]
    n.append(x)

z=0

for i in range(b):
    z+=n[i]
print("全班的總平均為：",round((z/3),2))