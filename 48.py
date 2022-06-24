x = int(input("輸入筆數n:"))
y={}

for i in range(4):
    e,c=input().split()
    y[e]=c
w=input("輸入欲查詢的單字")
print(w,'中文意思為',y[w])