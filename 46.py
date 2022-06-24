list=['金','銀','銅','優']
x=int(input('輸入比數n:'))
dict={}

for i in range(0,x):
    c=int(input(list[i]))
    dict[list[i]]=c
for m,n in dict.items():
    print(m+'牌得到',x,'面')