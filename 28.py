x=input("請輸入第一列: ")
y=input("請輸入第二列: ")
a=x.split(" ")
b=y.split(" ")

det=(int(a[0])*int(b[1]))-(int(a[1])*int(b[0]))
print(str(int(b[1])/det)+" "+str(int(b[0])/-det))
print(str(int(a[1])/-det)+" "+str(int(a[0])/det))