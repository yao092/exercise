a = []

while True:
    b = input("請輸入事項(若已無事項，請輸入end):")
    a.append(b)
    if b == 'end':
        for i in range(len(a)-1):
            print('%d. %s' %(i+1,a[i]))
        break