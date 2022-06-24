x=int(input('x:'))
y=int(input('y:'))
z=int(input('z:'))
o=y**2-4*x*z

if o>0:
    a=(-y + o**0.5) / 2*x
    b=(-y - o**0.5) / 2*x
    print("%d\n%d"%(a,b))
elif o==0:
    a=-y/2*x
    print(int(a))
elif o<0:
    print(0)