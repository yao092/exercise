while True:
    a = input('檢測的字串(end 結束)')
    
    if a != 'end':
         b = input('檢測的單一字元')
         print('字元%s出現次數為:%d'%(b,a.count(b)))
    else:
        print('檢測結束')
        break