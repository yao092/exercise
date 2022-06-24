m=list(input('請輸入第一組數字：'))
n=list(input('請輸入第二組數字：'))

while True:
    x=0
    y=0
    for i in range(len(m)):
        if m[i]==n[i]:
            x+=1
        else:
            y+=1
    if x==len(m):
        print("%dA%dB" %(x,y)+'全對')
        break
    else:            
        print("%dA%dB" %(x,y)+'加油')
        n=list(input('請輸入第二組數字：'))