#4.1

a=float(input())
b=float(input())
if a<b:
    print(b, 'больше')
    print(a, 'меньше')
elif a>b:
    print(a, 'больше')
    print(b, 'меньше')
else:
    print('числа равны')

#4.2

from math import *
x=float(input())
if x>0:
    y=(sin(x))**2
else:
    y=1-2*sin(x**2)
print(y)

#4.3

from math import *
x=float(input())
if x>0:
    y=sin(x**2)
else:
    y=1+2*(sin(x))**2

#4.4

x=float(input())
if x>4:
    print(2)
else:
    print(1)

#4.5

y=float(input())
if y>3:
    print(1)
else:
    print(2)

#4.6a

x=float(input())
if x<=2:
    y=x
else:
    y=2
print(y)

#4.6b

x=float(input())
if x<=3:
    y=-x
else:
    y=-3
print(y)

#4.7

from math import *
x=float(input())
if sin(x)<0:
    k=x**2
else:
    k=abs(x)
if k<x:
    f=k*x
else:
    f=k+x
print(f)

#4.8

from math import *
x=float(input())
if sin(x)>=0:
    k=x**2
else:
    k=abs(x)
if x<k:
    f=abs(x)
else:
    f=k*x
print(f)

#4.9

a=float(input())
b=float(input())
maximum=a
minimum=b
if a<b:
    maximum=b
    minimum=a
print(f'maximum = {maximum}, minimum = {minimum}')

#4.10

a=float(input('v km'))
b=float(input('v futax'))
ma=a*1000
mb=b*0.3048
if ma>mb:
    print(a)
elif ma<mb:
    print(b)
else:
    print('oni ravni')

#4.11

v1=float(input())
v2=float(input())
mv1=v1*10/36
if mv1>v2:
    print(v1)
elif mv1<v2:
    print(v2)
else:
    print('oni ravni')

#4.12

from math import *
r=float(input('radius kruqa'))
a=float(input('storona kvadrata'))
skr=pi*r**2
skv=a**2
if skr>skv:
    print('ploshad kruqa bolshe')
elif skr<skv:
    print('ploshad kvadrata bolshe')
else:
    print('oni ravni')

#4.13

V1=float(input('obyom pervoqo'))
m1=float(input('massa pervoqo'))
V2=float(input('obyom vtoroqo'))
m2=float(input('massa vtoroqo'))
p1=m1/V1
p2=m2/V2
if p1>p2:
    print('plotnost pervoqo bolshe')
elif p1<p2:
    print('plotnost vtoroqo bolshe')
else:
    print('oni ravni')

#4.14

R1=float(input('soprotivlenie pervoqo'))
U1=float(input('napryazhenie pervoqo'))
R2=float(input('soprotivlenie vtoroqo'))
U2=float(input('napryazhenie vtoroqo'))
I1=U1/R1
I2=U2/R2
if I1>I2:
    print('tok pervoqo bolshe')
elif I1<I2:
    print('tok vtoroqo bolshe')
else:
    print('oni ravni')

#4.15

a=float(input())
b=float(input())
c=float(input())
D=b**2-4*a*c
if D>=0:
    print('korni est')
else:
    print('korney net')

#4.16

from math import *
a=float(input())
b=float(input())
c=float(input())
D=b**2-4*a*c
if D>=0:
    x1=(-b+sqrt(D))/(2*a)
    x2=(-b-sqrt(D))/(2*a)
else:
    print('korney net')

#4.17

qodrozh=int(input())
mesrozh=int(input())
qodseq=int(input())
messeq=int(input())
age=qodseq-qodrozh
if mesrozh>messeq:
    age1=age-1
else:
    age1=age
print(age)

#4.18a

import math
S_circle = float(input("площадь круга: "))
S_square = float(input("площадь квадрата: "))
r = math.sqrt(S_circle / math.pi)
a = math.sqrt(S_square)
if 2 * r <= a:
    print("Круг уместится в квадрате.")
else:
    print("Круг не уместится в квадрате.")

#4.18b

import math
S_circle = float(input("площадь круга:"))
S_square = float(input("площадь квадрата:"))
r = math.sqrt(S_circle / math.pi)
a = math.sqrt(S_square)
if a * math.sqrt(2) <= 2 * r:
    print("Квадрат уместится в круге.")
else:
    print("Квадрат не уместится в круге.")

#4.19

import math
S_circle = float(input("площадь круга:"))
S_triangle = float(input("площадь равностороннего треугольника: "))
r = math.sqrt(S_circle / math.pi)
a = math.sqrt((4 * S_triangle) / math.sqrt(3))
r_in = a * math.sqrt(3) / 6
R_out = a * math.sqrt(3) / 3
if r <= r_in:
    print("а) Круг уместится в треугольнике.")
else:
    print("а) Круг не уместится в треугольнике.")

if R_out <= r:
    print("б) Треугольник уместится в круге.")
else:
    print("б) Треугольник не уместится в круге.")

#4.20

x1_1 = float(input('x левого нижнего угла первого прямоугольника:'))
y1_1 = float(input('y левого нижнего угла первого прямоугольника:'))
x2_1 = float(input('x правого верхнего угла первого прямоугольника:'))
y2_1 = float(input('y правого верхнего угла первого прямоугольника:'))
x1_2 = float(input('x левого нижнего угла второго прямоугольника:'))
y1_2 = float(input('y левого нижнего угла второго прямоугольника:'))
x2_2 = float(input('x правого верхнего угла второго прямоугольника:'))
y2_2 = float(input('y правого верхнего угла второго прямоугольника:'))
x_min = min(x1_1, x1_2)
y_min = min(y1_1, y1_2)
x_max = max(x2_1, x2_2)
y_max = max(y2_1, y2_2)
print(f"Координаты минимального прямоугольника, содержащего оба:")
print(f"Левый нижний угол: ({x_min}, {y_min})")
print(f"Правый верхний угол: ({x_max}, {y_max})")




#4.99a

a=float(input())
b=float(input())
if a>b:
    print(a)
if a<b:
    print(b)

#4.99b

a=float(input())
b=float(input())
maximum=a
if a<b:
    maximum=b
print(maximum)

#4.100a

a=float(input())
b=float(input())
if a>b:
    print(f'Большее - {a}, меньшее - {b}')
if a<b:
    print(f'Большее - {b}, меньшее - {a}')

#4.100b


a=float(input())
b=float(input())
maximum=a
minimum=b
if a<b:
    maximum=b
    minimum=a
print(f'Большее - {maximum}, меньшее - {minimum}')

#4.101a

a=float(input())
b=float(input())
c=float(input())
print(max(a,b,c))

#4.101b

a=float(input())
b=float(input())
c=float(input())
print(min(a,b,c))

#4.102a

a=float(input())
b=float(input())
c=float(input())
d=float(input())
print(max(a,b,c,d))

#4.102b

a=float(input())
b=float(input())
c=float(input())
d=float(input())
print(min(a,b,c,d))

#4.103

a=float(input())
if a>=0:
    print(a)
else:
    print(-a)

#4.104a

a=float(input())
b=float(input())
if a>=0:
    a=a
else:
    a=-a
if b>=0:
    b=b
else:
    b=-b
p=(a+b)/2
print(p)

#4.104b

from math import *
a=float(input())
b=float(input())
if a>=0:
    a=a
else:
    a=-a
if b>=0:
    b=b
else:
    b=-b
p=sqrt(a*b)
print(p)

#4.105

a=float(input())
b=float(input())
if a>=0:
    a=a
else:
    a=-a
if b>=0:
    b=b
else:
    b=-b
if a>b:
    a=a/2
print(a)

#4.106

from math import *
a=float(input())
b=float(input())
if sqrt(b)<a:
    b=b*5

#4.107

a=int(input())
b=int(input())
c=int(input())
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)

#4.108

a=float(input())
b=float(input())
c=float(input())
if a>=0:
    a=a**2
if b>=0:
    b=b**2
if c>=0:
    c=c**2
print(a,b,c)

#4.109

a=float(input())
b=float(input())
c=float(input())
if 1.6<=a<=3.8:
    print(a)
if 1.6<=b<=3.8:
    print(b)
if 1.6<=c<=3.8:
    print(c)