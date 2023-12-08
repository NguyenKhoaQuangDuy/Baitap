#Bài 1
x= float(input('Nhap so km di chuyen: '))
if x<0:
    print ('Lỗi')
    exit ()
elif x<=1:
    t=15000
elif x<=5:
    t=15000+13500*(x-1)
elif x<=120:
    t= 15000+4*13500+(x-5)*11000
else:
    t= 0.9*(15000+4*13500+(x-5)*11000)
print ("so tien phai tra la: ",t,'dong')






