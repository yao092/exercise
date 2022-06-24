x=int(input('請輸入n值:'))
y={}
for i in range(x):
    m=input('請輸入姓名:')
    n=input('請輸入電子郵件:')
    y[m]=n
z=input('請輸入要查詢電子郵件的姓名:')
print(z+'電子郵件帳號為'+y.get(z,'不存在'))