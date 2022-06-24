a = input("甲方的數字:")
b = input("乙方的數字:")
c = ''

for i in range(len(a)):
    if a[i] == '1' and b[i] == '5':
        c += '贏'
    elif a[i] == '2' and b[i] == '1':
        c += '贏'
    elif a[i] == '3' and b[i] == '2':
        c += '贏'
    elif a[i] == '4' and b[i] == '3':
        c += '贏'
    elif a[i] == '5' and b[i] == '4':
        c += '贏'
    elif a[i] == '1' and b[i] == '2':
        c += '輸'
    elif a[i] == '2' and b[i] == '3':
        c += '輸'
    elif a[i] == '3' and b[i] == '4':
        c += '輸'
    elif a[i] == '4' and b[i] == '5':
        c += '輸'
    elif a[i] == '5' and b[i] == '1':
        c += '輸'
    else:
        c += '和'
print(c)