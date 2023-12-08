#Bài 2
import math
a= float(input('Nhap a: '))
b= float(input('Nhap b: '))
c= float(input('Nhap c: '))
if a==0:
    if b==0:
        if c==0:
            print ('Phuong trinh co vo so nghiem')
        else:
            print ('Phuong trinh vo nghiem')
    else:
        print ('Phuong trinh co 1 nghiem la: ',-b/c)
else:
    dt=b**2-4*a*c
    if dt<0:
        print ('Phuong trinh vo nghiem')
    else:
        x1= (-b+math.sqrt(dt))/2*a
        x2= (-b-math.sqrt(dt))/2*a
        print ('Phuong trinh co 2 nghiem lan luot la: ',x1,x2)
