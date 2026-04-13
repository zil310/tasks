# ax^2 + bx + c = 0
a = float(input("введите значение а:"))
b = float(input("введите значение b:"))
c = float(input("введите значение с:"))
if a != 0:
    D = b**2 - (4*a*c)
    z = -b / (2*a)
    if D > 0:
        x1 = z + D**0.5 / (2*a)
        x2 = z - D**0.5 / (2*a)
        print(round(x1,2),round(x2,2))
    if D == 0:
        print(round(z,2))
    if D < 0:
        iks= abs(D) / (2*a)
        text1 = f"x1= {z:.2f} + {iks:.2f}*i"
        text2 = f"x2= {z:.2f} - {iks:.2f}*i"
        print(text1,text2)
elif b != 0 :
    if c != 0:
        x = -b/c
        print(round(x,2))
    else:
        print('x=0')
elif c !=0:
    print('нет корней')
else:
    print('любой икс')






