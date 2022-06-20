x = int(input("輸入度數(正整數)"))

if 0< x <121:
    print("Summer months:%.2f" % (x*2.10))
    print("Non-Summer months:%.2f" % (x*2.10))
elif 120 < x < 331:
    print("Summer months:%.2f" % ((x-120)*3.02+120*2.10))
    print("Non-Summer months:%.2f" % ((x-120)*2.68+120*2.10))
elif 330 < x < 501:
    print("Summer months:%.2f" % ((x-330)*4.39+(330-120)*3.02+120*2.10))
    print("Non-Summer months:%.2f" % ((x-330)*3.61+(330-120)*2.68+120*2.10))
elif 500 < x < 701:
    print("Summer months:%.2f" % ((x-500)*4.97+(500-330)*4.39+(330-120)*3.02+120*2.10))
    print("Non-Summer months:%.2f" % ((x-500)*4.01+(500-330)*3.61+(330-120)*2.68+120*2.10))
else:
    print("Summer months%.2f" % ((x-700)*5.63+(700-500)*4.97+(500-330)*4.39+(330-120)*3.02+120*2.10))
    print("Non-Summer months:%.2f" % ((x-700)*4.50+(700-500)*4.01+(500-330)*3.61+(330-120)*2.68+120*2.10))