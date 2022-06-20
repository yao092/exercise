x=int(input("輸入X座標"))
y=int(input("輸入Y座標"))
a=x**2+y**2

if x>0 and y>0:
    print("該點位於第一象限，離原點距離為根號%d"%(a))
elif x<0 and y>0:
    print("該點位於第二象限，離原點距離為根號%d"%(a))
elif x<0 and y<0:
    print("該點位於第三象限，離原點距離為根號%d"%(a))
elif x>0 and y<0:
    print("該點位於第四象限，離原點距離為根號%d"%(a))
elif x==0 and y!=0:
    print("該點位於y軸上，離原點距離為根號%d"%(a))
elif x!=0 and y==0:
    print("該點位於x軸上，離原點距離為根號%d"%(a))
else:
    print("該點位於原點")